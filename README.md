# Teste de Nivelamento Intuitive Care
 
Este repositório contém um teste de nivelamento que envolve Web Scraping.
 
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
   git clone https://github.com/seu-usuario/teste-de-nivelamento.git
   cd teste-de-nivelamento
   ```
 
2. Instale as dependências:
 
   ```sh
   pip install -r webscrap/requirements.txt
   ```
 
3. Configure as variáveis de ambiente no arquivo `webscrap/config.env`.
 
### 🚀 Como executar
 
Para iniciar o processo de scraping e download:
 
```sh
# Para Windows
cd webscrap
python webscrapper.py
````

```sh
# Para Mac/Linux
cd webscrap
python3 webscrapper.py
```
 
Após a execução, os arquivos baixados serão compactados no arquivo `anexos.zip`.
 
### 🛠 Tecnologias utilizadas
 
- Python
- Selenium
- BeautifulSoup
- Requests
- WebDriver Manager
 
### 📄 Licença
 
Este projeto é apenas para fins de avaliação e não possui licença oficial.
 
---
