import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Driver cacheado para não instalar toda vez
_driver_path = ChromeDriverManager().install()

# ==========================================================
# FIXTURE DO WEBDRIVER
# ==========================================================
@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # Mais rápido sem interface
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(service=Service(_driver_path), options=chrome_options)
    yield driver
    driver.quit()

# ==========================================================
# TESTES DE ALERTAS
# ==========================================================
def test_alert_with_ok_cancel(driver):
    driver.get('https://demo.automationtesting.in/Alerts.html')

    # Espera até o link estar clicável e clica
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Alert with OK & Cancel')]"))
    ).click()

def test_alert_with_textbox(driver):
    driver.get('https://demo.automationtesting.in/Alerts.html')

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Alert with Textbox')]"))
    ).click()

# ==========================================================
# TESTES DE MULTI-JANELAS
# ==========================================================
def test_windows(driver):
    driver.get('https://demo.automationtesting.in/Windows.html')
    tab_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="Tabbed"]/a/button'))
    )
    tab_btn.click()

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])
    assert "Selenium" in driver.title or "selenium" in driver.current_url.lower()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

def test_separate_window(driver):
    driver.get('https://demo.automationtesting.in/Windows.html')
    driver.find_element(By.LINK_TEXT, "Open New Seperate Windows").click()

    btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="Seperate"]/button'))
    )
    btn.click()

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

def test_multiple_windows(driver):
    driver.get('https://demo.automationtesting.in/Windows.html')
    driver.find_element(By.LINK_TEXT, "Open Seperate Multiple Windows").click()

    btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="Multiple"]/button'))
    )
    btn.click()

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(3))
    handles = driver.window_handles
    for i in range(1, 3):
        driver.switch_to.window(handles[i])
        driver.close()
    driver.switch_to.window(handles[0])
