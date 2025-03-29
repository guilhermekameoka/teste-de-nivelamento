provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "static_bucket" {
  bucket      = "teste-nivelamento-terraform"
  acl         = "public-read"

  tags = {
    Name = "StaticBucket"
  }
}

resource "aws_s3_bucket_website_configuration" "static_bucket_website" {
  bucket = aws_s3_bucket.static_bucket.id

  index_document {
    suffix = "index.html"
  }
}

resource "aws_lambda_function" "api_lambda" {
  function_name = "flask_api"
  role          = aws_iam_role.lambda_exec.arn
  runtime       = "python3.9"
  handler       = "server.lambda_handler"
  
  filename         = "lambda_function.zip"
  source_code_hash = filebase64sha256(file("lambda_function.zip"))

  environment {
    variables = {
      CSV_PATH = "/tmp/dados.csv"
    }
  }
}

resource "aws_api_gateway_rest_api" "api" {
  name        = "FlaskAPI"
  description = "API para buscar operadoras"
}

resource "aws_api_gateway_resource" "search" {
  rest_api_id = aws_api_gateway_rest_api.api.id
  parent_id   = aws_api_gateway_rest_api.api.root_resource_id
  path_part   = "search"
}

resource "aws_api_gateway_method" "search_get" {
  rest_api_id        = aws_api_gateway_rest_api.api.id
  resource_id        = aws_api_gateway_resource.search.id
  http_method        = "GET"
  authorization      = "NONE"
}

resource "aws_api_gateway_integration" "lambda" {
  rest_api_id             = aws_api_gateway_rest_api.api.id
  resource_id             = aws_api_gateway_resource.search.id
  http_method             = aws_api_gateway_method.search_get.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.api_lambda.invoke_arn
}

resource "aws_api_gateway_deployment" "api_deploy" {
  depends_on  = [aws_api_gateway_integration.lambda]
  rest_api_id = aws_api_gateway_rest_api.api.id
  stage_name  = "prod"
}

resource "aws_lambda_permission" "apigw" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.api_lambda.function_name
  principal     = "apigateway.amazonaws.com"

  source_arn = "${aws_api_gateway_rest_api.api.execution_arn}/*/*"
}

output "api_url" {
  value = aws_api_gateway_deployment.api_deploy.invoke_url
}