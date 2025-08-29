import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # ativa modo headless
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    yield driver
    driver.quit()

def test_video_vimeo(driver):
    driver.get('https://demo.automationtesting.in/Vimeo.html')

    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe[src*="vimeo.com"]'))
    )

    driver.execute_script("""
        var script = document.createElement('script');
        script.src = 'https://player.vimeo.com/api/player.js';
        script.async = false;
        document.head.appendChild(script);
    """)

    WebDriverWait(driver, 10).until(
        lambda d: d.execute_script("return typeof Vimeo !== 'undefined' && typeof Vimeo.Player !== 'undefined';")
    )

    driver.execute_script("""
        var iframe = document.querySelector('iframe[src*="vimeo.com"]');
        var player = new Vimeo.Player(iframe);
        player.play();
    """)

    WebDriverWait(driver, 5).until(lambda d: True)
