import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

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

# ############################ ACCORDION #################
def test_accordion(driver):
    driver.get('https://demo.automationtesting.in/Accordion.html')
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="Functionality"]/div/div/div/div[1]/div[1]'))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="Functionality"]/div/div/div/div[2]/div[1]'))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="Functionality"]/div/div/div/div[3]/div[1]'))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="Functionality"]/div/div/div/div[4]/div[1]'))
    ).click()

# ######################## AUTOCOMPLETE ##################
def test_autocomplete(driver):
    driver.get('https://demo.automationtesting.in/AutoComplete.html')
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input.ui-autocomplete-input'))
    )
    input_field.send_keys('BRAZIL')
    brazil_option = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/section/div[1]/div[2]/div[2]/ul/li/a'))
    )
    brazil_option.click()

# #################### DATEPICKER HOJE ###################
def test_datepicker_today(driver):
    driver.get('https://demo.automationtesting.in/Datepicker.html')
    driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/form/div[2]/div[2]/img').click()
    driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[5]/a').click()

# ############ DATEPICKER NASCIMENTO #####################
def test_datepicker_birthdate(driver):
    driver.get('https://demo.automationtesting.in/Datepicker.html')
    birth_date_input = driver.find_element(By.XPATH, '//*[@id="datepicker2"]')
    birth_date_input.send_keys('10/12/1976')

# ########################### SLIDER #####################
def test_slider(driver):
    driver.get('https://demo.automationtesting.in/Slider.html')
    slider_handle = driver.find_element(By.CSS_SELECTOR, '#slider .ui-slider-handle')
    actions = ActionChains(driver)
    actions.click_and_hold(slider_handle).move_by_offset(50, 0).release().perform()
