from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_selenium_driver():
    """Configura o WebDriver do Selenium para rodar em modo headless (sem interface gráfica)."""
    try:
        options = Options()
        options.add_argument("--headless")
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)
    except Exception as e:
        print(f"Erro ao configurar o WebDriver: {e}")
        return None
