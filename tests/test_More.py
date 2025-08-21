import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# ==========================================================
# FIXTURE WEBDRIVER
# ==========================================================
@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    yield driver
    driver.quit()

# ########################################################
# ################ FILE DOWNLOAD TXT #####################
# ########################################################
def test_file_download_txt(driver):
    driver.get("https://demo.automationtesting.in/FileDownload.html")

    txtbox = driver.find_element(By.XPATH, '//*[@id="textbox"]')
    txtbox.send_keys("BRAZIL")

    # Força evento input para habilitar botão
    driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }))", txtbox)

    btn_txt = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="createTxt"]'))
    )
    btn_txt.click()

    link_download = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="link-to-download"]'))
    )
    link_download.click()
    time.sleep(2)

# ########################################################
# ################ FILE DOWNLOAD PDF #####################
# ########################################################
def test_file_download_pdf(driver):
    driver.get("https://demo.automationtesting.in/FileDownload.html")

    pdfbox = driver.find_element(By.XPATH, '//*[@id="pdfbox"]')
    pdfbox.send_keys("BRAZIL")

    driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }))", pdfbox)

    btn_pdf = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="createPdf"]'))
    )
    btn_pdf.click()

    link_download_pdf = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="pdf-link-to-download"]'))
    )
    link_download_pdf.click()
    time.sleep(2)

# ########################################################
# ###################### FILE UPLOAD #####################
# ########################################################
def test_file_upload(driver):
    driver.get("https://demo.automationtesting.in/FileUpload.html")

    arquivo = os.path.abspath("C:/Users/Leonardo/OneDrive/Documents/info.pdf")
    input_file = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    input_file.send_keys(arquivo)
    time.sleep(2)

# ########################################################
# ######################## LOADER ########################
# ########################################################
def test_loader(driver):
    driver.get("https://demo.automationtesting.in/Loader.html")

    loader_btn = WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="loader"]'))
    )
    loader_btn.click()

    close_btn = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="myModal"]/div/div/div[3]/button[1]'))
    )
    close_btn.click()

# ########################################################
# ##################### PROGRESS BAR #####################
# ########################################################
def test_progress_bar(driver):
    driver.get("https://demo.automationtesting.in/ProgressBar.html")

    btn_start = WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="cricle-btn"]'))
    )
    btn_start.click()
