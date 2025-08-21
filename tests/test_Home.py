import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuração do WebDriver com ChromeOptions
@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    # chrome_options.add_argument("--headless")  # Rodar em modo headless, se necessário

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    yield driver
    driver.quit()

# ########################## HOME PAGE ##############################
def test_home(driver):
    # Acessando o site
    driver.get('https://demo.automationtesting.in/Index.html')

    # Verificando o título da página
    titulo = driver.title
    assert titulo == 'Index', f'Erro: Título esperado "Index", mas foi "{titulo}"'
