import pytest
import allure
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver(request):
    """
    Fixture do Selenium WebDriver.
    Inicia o Chrome antes de cada teste e fecha no final.
    """
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # remove logs extras
    # chrome_options.add_argument("--headless")  # descomente se quiser rodar sem abrir o navegador

    # Redireciona logs do ChromeDriver para null (Windows/Linux)
    null_log = "NUL" if os.name == "nt" else "/dev/null"
    service = Service(ChromeDriverManager().install(), log_path=null_log)

    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Anexa o driver ao request para teardown
    request.node.driver = driver

    yield driver

    # Screenshot automático no Allure se o teste falhar
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG
        )

    driver.quit()


# ==========================================================
# HOOK: captura o status do teste (pass/fail) para usar no fixture
# ==========================================================
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    Hook do pytest para armazenar o resultado do teste
    (passou/falhou) dentro do objeto `item`.
    Assim podemos usar no fixture driver para tirar screenshot só em falha.
    """
    outcome = yield
    rep = outcome.get_result()

    # adiciona o resultado como atributo no item
    setattr(item, "rep_" + rep.when, rep)
    return rep
