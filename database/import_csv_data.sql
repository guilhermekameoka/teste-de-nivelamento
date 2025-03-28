-- Importa os dados do 1º Trimestre de 2023
LOAD DATA INFILE '/Users/guilhermekameoka/Desktop/prova/database/financial_statements/2023/1T2023.csv'
INTO TABLE health_expenses
CHARACTER SET utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(@data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
   data = STR_TO_DATE(@data, '%Y-%m-%d'),
   reg_ans = TRIM(@reg_ans),
   cd_conta_contabil = TRIM(@cd_conta_contabil),
   descricao = TRIM(@descricao),
   vl_saldo_inicial = CAST(REPLACE(@vl_saldo_inicial, ',', '.') AS DECIMAL(15,2)),
   vl_saldo_final = CAST(REPLACE(@vl_saldo_final, ',', '.') AS DECIMAL(15,2));

-- Importa os dados do 2º Trimestre de 2023
LOAD DATA INFILE '/Users/guilhermekameoka/Desktop/prova/database/financial_statements/2023/2T2023.csv'
INTO TABLE health_expenses
CHARACTER SET utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(@data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
   data = STR_TO_DATE(@data, '%Y-%m-%d'),
   reg_ans = @reg_ans,
   cd_conta_contabil = @cd_conta_contabil,
   descricao = @descricao,
   vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
   vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');

-- Importa os dados do 3º Trimestre de 2023
LOAD DATA INFILE '/Users/guilhermekameoka/Desktop/prova/database/financial_statements/2023/3T2023.csv'
INTO TABLE health_expenses
CHARACTER SET utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(@data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
   data = STR_TO_DATE(@data, '%Y-%m-%d'),
   reg_ans = @reg_ans,
   cd_conta_contabil = @cd_conta_contabil,
   descricao = @descricao,
   vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
   vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');
   vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');

-- Importa os dados do 4º Trimestre de 2023
LOAD DATA INFILE '/Users/guilhermekameoka/Desktop/prova/database/financial_statements/2023/4T2023.csv'
INTO TABLE health_expenses
CHARACTER SET utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(@data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
   data = STR_TO_DATE(@data, '%d/%m/%Y'),
   reg_ans = @reg_ans,
   cd_conta_contabil = @cd_conta_contabil,
   descricao = @descricao,
   vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
   vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');

-- Importa os dados do 1º Trimestre de 2024
LOAD DATA INFILE '/Users/guilhermekameoka/Desktop/prova/database/financial_statements/2024/1T2024.csv'
INTO TABLE health_expenses
CHARACTER SET utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(@data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
   data = STR_TO_DATE(@data, '%Y-%m-%d'),
   reg_ans = @reg_ans,
   cd_conta_contabil = @cd_conta_contabil,
   descricao = @descricao,
   vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
   vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');

-- Importa os dados do 2º Trimestre de 2024
LOAD DATA INFILE '/Users/guilhermekameoka/Desktop/prova/database/financial_statements/2024/2T2024.csv'
INTO TABLE health_expenses
CHARACTER SET utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(@data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
   data = STR_TO_DATE(@data, '%Y-%m-%d'),
   reg_ans = @reg_ans,
   cd_conta_contabil = @cd_conta_contabil,
   descricao = @descricao,
   vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
   vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');

-- Importa os dados do 3º Trimestre de 2024
LOAD DATA INFILE '/Users/guilhermekameoka/Desktop/prova/database/financial_statements/2024/3T2024.csv'
INTO TABLE health_expenses
CHARACTER SET utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(@data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
   data = STR_TO_DATE(@data, '%Y-%m-%d'),
   reg_ans = @reg_ans,
   cd_conta_contabil = @cd_conta_contabil,
   descricao = @descricao,
   vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
   vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');

-- Importa os dados do 4º Trimestre de 2024
LOAD DATA INFILE '/Users/guilhermekameoka/Desktop/prova/database/financial_statements/2024/4T2024.csv'
INTO TABLE health_expenses
CHARACTER SET utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(@data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
   data = STR_TO_DATE(@data, '%Y-%m-%d'),
   reg_ans = @reg_ans,
   cd_conta_contabil = @cd_conta_contabil,
   descricao = @descricao,
   vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
   vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');