from selenium import webdriver                             # A biblioteca Selenium é usada para automação de navegadores
from selenium.webdriver.chrome.service import Service      # A classe Service gerencia a execução do ChromeDriver
from selenium.webdriver.chrome.options import Options      # A classe Options permite configurar opções para o navegador
from webdriver_manager.chrome import ChromeDriverManager   # O WebDriver Manager gerencia a instalação automática do ChromeDriver


def get_selenium_driver():
    """Configura o WebDriver do Selenium para rodar em modo headless (sem interface gráfica)."""
    try:
        # Cria um objeto para configurar opções do Chrome
        options = Options()
        # Essa opção permite rodar o navegador sem interface gráfica
        options.add_argument("--headless")
        # Instala e gerencia automaticamente o ChromeDriver
        service = Service(ChromeDriverManager().install())
        # Inicializa e retorna uma instância do WebDriver
        return webdriver.Chrome(service=service, options=options)
    # Captura e trata qualquer erro na configuração do WebDriver
    except Exception as e:
        print(f"Erro ao configurar o WebDriver: {e}")
        return None
