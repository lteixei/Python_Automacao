import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

# Usa apenas uma vez para cachear
_driver_path = ChromeDriverManager().install()

# ==========================================================
# FIXTURE DO WEBDRIVER
# ==========================================================
@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # Modo mais rápido
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(service=Service(_driver_path), options=chrome_options)
    yield driver
    driver.quit()

# ==========================================================
# TESTE DRAG AND DROP - STATIC
# ==========================================================
def test_drag_and_drop_static(driver):
    driver.get('https://demo.automationtesting.in/Static.html')
    drop_area = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "droparea"))
    )

    for obj_id in ['angular', 'mongo', 'node']:
        obj = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, obj_id))
        )
        ActionChains(driver).drag_and_drop(obj, drop_area).perform()

# ==========================================================
# TESTE DRAG AND DROP - DYNAMIC
# ==========================================================
def test_drag_and_drop_dynamic(driver):
    driver.get('https://demo.automationtesting.in/Dynamic.html')
    drop_area = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "droparea"))
    )

    for obj_id in ['angular', 'mongo', 'node']:
        obj = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, obj_id))
        )
        ActionChains(driver).drag_and_drop(obj, drop_area).perform()

# ==========================================================
# TESTE SELECTABLE - DEFAULT
# ==========================================================
def test_selectable_default(driver):
    driver.get('https://demo.automationtesting.in/Selectable.html')
    for i in [1, 3, 5, 7]:
        item = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f'//*[@id="Default"]/ul/li[{i}]'))
        )
        item.click()

# ==========================================================
# TESTE SELECTABLE - SERIALIZE
# ==========================================================
def test_selectable_serialize(driver):
    driver.get('https://demo.automationtesting.in/Selectable.html')
    indices = [1, 3, 5, 7]
    for i in indices:
        item = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f'//*[@id="Default"]/ul/li[{i}]'))
        )
        item.click()

# ==========================================================
# TESTE RESIZABLE
# ==========================================================
def test_resizable(driver):
    driver.get('https://demo.automationtesting.in/Resizable.html')
    handle = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="resizable"]/div[3]'))
    )

    ActionChains(driver).move_to_element(handle).click_and_hold().move_by_offset(50, 0).release().perform()
