import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Configuração do WebDriver com ChromeOptions em modo headless
@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ativa modo headless
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    yield driver
    driver.quit()

# ######################## SUMMERNOTE ############################
def test_summernote(driver):
    driver.get('https://demo.automationtesting.in/SummerNote.html')

    editor = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.note-editable'))
    )

    editor.click()
    editor.clear()
    editor.send_keys('LEONARDO')

    # Seleciona tudo e aplica negrito + sublinhado (Ctrl + A)
    ActionChains(driver).key_down('\ue009').send_keys('a').key_up('\ue009').perform()

    # Negrito
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.note-btn-bold'))
    ).click()

    # Sublinhado
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.note-btn-underline'))
    ).click()

