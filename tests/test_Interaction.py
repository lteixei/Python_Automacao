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

# Configuração do WebDriver com ChromeOptions
@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    # Remover o modo headless para visualizar o navegador
    # chrome_options.add_argument("--headless")  # Comentado ou removido para rodar com navegador visível
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    yield driver
    driver.quit()  # Fechar o navegador após cada teste

# ######################## DRAG AND DROP - STATIC #####################
def test_drag_and_drop_static(driver):
    driver.get('https://demo.automationtesting.in/Static.html')
    drop_area = driver.find_element(By.XPATH, '//*[@id="droparea"]')
    
    objs = ['angular', 'mongo', 'node']
    for obj_id in objs:
        obj = driver.find_element(By.XPATH, f'//*[@id="{obj_id}"]')
        actions = ActionChains(driver)
        actions.drag_and_drop(obj, drop_area).perform()
        time.sleep(0.5)  # Aguarda meio segundo após cada ação

# ######################## DRAG AND DROP - DYNAMIC ####################
def test_drag_and_drop_dynamic(driver):
    driver.get('https://demo.automationtesting.in/Dynamic.html')
    drop_area = driver.find_element(By.XPATH, '//*[@id="droparea"]')

    objs = ['angular', 'mongo', 'node']
    for obj_id in objs:
        obj = driver.find_element(By.XPATH, f'//*[@id="{obj_id}"]')
        actions = ActionChains(driver)
        actions.drag_and_drop(obj, drop_area).perform()
        time.sleep(0.5)  # Aguarda meio segundo após cada ação

# ###################### SELECTABLE - DEFAULT ##########################
def test_selectable_default(driver):
    driver.get('https://demo.automationtesting.in/Selectable.html')
    items = [1, 3, 5, 7]
    for index in items:
        item = driver.find_element(By.XPATH, f'//*[@id="Default"]/ul/li[{index}]')
        item.click()
        time.sleep(0.5)  # Aguarda meio segundo após cada clique

# ###################### SELECTABLE - SERIALIZE ########################
def test_selectable_serialize(driver):
    driver.get('https://demo.automationtesting.in/Selectable.html')

    driver.find_element(By.XPATH, '//*[@id="Default"]/ul/li[1]').click()  # Clica na primeira opção
    driver.find_element(By.XPATH, '//*[@id="Default"]/ul/li[3]').click()  # Clica na terceira opção
    driver.find_element(By.XPATH, '//*[@id="Default"]/ul/li[5]').click()  # Clica na quinta opção
    driver.find_element(By.XPATH, '//*[@id="Default"]/ul/li[7]').click()  # Clica na sétima opção

# ######################## RESIZABLE ##################################
def test_resizable(driver):
    driver.get('https://demo.automationtesting.in/Resizable.html')
    handle = driver.find_element(By.XPATH, '//*[@id="resizable"]/div[3]')
    box = handle.rect

    if not box:
        raise Exception('Não foi possível localizar o handle de resize')

    actions = ActionChains(driver)
    actions.move_to_element(handle).click_and_hold().move_by_offset(50, 0).release().perform()  # Ajusta o tamanho horizontal

    time.sleep(1)  # Aguarda 1 segundo para visualizar a ação

