import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Fixture para inicializar o WebDriver
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

# ########################################################
# ############################ ALERT #####################
# ########################################################
def test_alert_default(driver):
    driver.get('https://demo.automationtesting.in/')
    driver.find_element(By.XPATH, '//*[@id="btn2"]').click()
    driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[4]/a').click()
    driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[4]/ul/li[1]/a').click()
    driver.find_element(By.XPATH, "//a[@href='#OKTab']").click()
    driver.find_element(By.XPATH, '//*[@id="OKTab"]/button').click()

    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    assert 'I am an alert box!' in alert.text
    alert.accept()

def test_alert_with_ok_cancel(driver):
    driver.get('https://demo.automationtesting.in/Alerts.html')
    driver.find_element(By.XPATH, "//ul/li[2]/a[text()='Alert with OK & Cancel ']").click()
    driver.find_element(By.XPATH, '//*[@id="CancelTab"]/button').click()

    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    assert 'Press a Button !' in alert.text
    alert.accept()  # ou alert.dismiss() para testar o botão "Cancel"

def test_alert_with_textbox(driver):
    driver.get('https://demo.automationtesting.in/Alerts.html')
    driver.find_element(By.XPATH, "//ul/li[3]/a[text()='Alert with Textbox ']").click()
    driver.find_element(By.XPATH, '//*[@id="Textbox"]/button').click()

    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    assert 'Please enter your name' in alert.text
    alert.send_keys('Leonardo da Motta Teixeira')
    alert.accept()

# ########################################################
# ############################ WINDOWS ###################
# ########################################################
def test_windows(driver):
    driver.get('https://demo.automationtesting.in/Windows.html')
    tabbed_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="Tabbed"]/a/button'))
    )
    tabbed_link.click()

    # Espera uma nova janela abrir
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

    print('Nova janela foi aberta. URL: ' + driver.current_url)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

def test_separate_window(driver):
    driver.get('https://demo.automationtesting.in/Windows.html')
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a').click()

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="Seperate"]/button'))
    )
    button.click()

    # Espera a nova janela abrir - fora
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))  # Espera até que uma nova janela tenha sido aberta
    new_window = driver.window_handles[1]  # Acessa a nova janela
    driver.switch_to.window(new_window)
    driver.close()  # Fecha a nova janela
    driver.switch_to.window(driver.window_handles[0])  # Retorna à janela original

def test_multiple_windows(driver):
    driver.get('https://demo.automationtesting.in/Windows.html')
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a').click()

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="Multiple"]/button'))
    )
    button.click()

    # Espera até que duas novas janelas sejam abertas
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(3))
    windows = driver.window_handles
    driver.switch_to.window(windows[1])  # Muda para a primeira nova janela
    driver.close()
    driver.switch_to.window(windows[2])  # Muda para a segunda nova janela
    driver.close()
    driver.switch_to.window(windows[0])  # Retorna à janela original
