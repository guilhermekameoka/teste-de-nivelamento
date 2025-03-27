# Teste de Nivelamento Intuitive Care

Este repositório contém um teste de nivelamento que envolve Web Scraping e Transformação de Dados.

## 📝 Índice

- [1. Teste de Web Scraping](#1-teste-de-web-scraping)
- [2. Teste de Transformação de Dados](#2-teste-de-transformação-de-dados)

## 1. Teste de Web Scraping

O objetivo deste teste é realizar a extração de documentos a partir de uma página do governo e compactá-los.
 
### 📋 Pré-requisitos
 
Antes de começar, certifique-se de ter os seguintes requisitos instalados:
 
- Python 3.x
- Pip
- Google Chrome
- ChromeDriver

### 📦 Instalação
 
1. Clone este repositório:
 
   ```sh
   git clone https://github.com/guilhermekameoka/teste-de-nivelamento.git
   cd teste-de-nivelamento
   ```
 
2. Instale as dependências:
 
   ```sh
   pip install -r requirements.txt
   ```

### 🔧 Configuração

Antes de executar o projeto, é necessário configurar o diretório de download e a URL da página a ser extraída. Edite o arquivo `.env` e ajuste os seguintes parâmetros conforme o uso pretendido

### 🚀 Como executar

Para iniciar o processo de scraping e download:

```sh
# Para Windows
python3 webscrap/webscrapper.py
````

```sh
# Para Mac/Linux
python webscrap/webscrapper.py
```

Após a execução, os arquivos baixados serão compactados no arquivo `anexos.zip`.

### 🛠 Tecnologias utilizadas
 
- Python
- Selenium
- BeautifulSoup
- Requests
- WebDriver Manager

## 2. Teste de Transformação de Dados

O objetivo deste teste é realizar a extração de dados de uma tabela presente em um arquivo PDF e salvar esses dados em um arquivo CSV compactado em ZIP.

### 🔧 Configuração

Antes de executar o script, é necessário configurar as variáveis de ambiente. Edite o arquivo `.env` na pasta raiz do projeto e adicione o caminho para o arquivo PDF a ser processado. As variáveis de ambiente necessárias são:

- **PDF_PATH**: Caminho do arquivo PDF de entrada.

### 🚀 Como executar

Para iniciar o processo de transformação de dados:

```sh
# Para Windows
python3 data_extraction/transformData.py
```

```sh
# Para Mac/Linux
python -m data_extraction.transformData

```

Após a execução, o arquivo CSV será compactado em um arquivo ZIP com o nome `Teste_Guilherme_Kameoka.zip`.

### 🛠 Tecnologias utilizadas

- Python
- pdfplumber
- pandas
- zipfile
- dotenv

### 📄 Licença

Este projeto é apenas para fins de avaliação e não possui licença oficial.
