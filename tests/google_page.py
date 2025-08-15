from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys  # Para pressionar Enter

class GooglePageLocator(object):
    INPUT_PESQUISA = '[name="q"]'
    BUTTON_PESQUISAR = '.FPdoLc [name="btnK"]'  # Seletor para o botão de pesquisa
    TITLE_RESULTADO = '[data-attrid="title"]'
    POPUP_COOKIE = '#L2AGLb'

class GooglePage:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def acess_page(self, url):
        self.driver.get(url)

    def send_keys_input_pesquisa(self, texto):
        input_pesquisa = self.get_element(GooglePageLocator.INPUT_PESQUISA)
        input_pesquisa.clear()  # Limpa o campo antes de escrever
        input_pesquisa.send_keys(texto)
        input_pesquisa.send_keys(Keys.RETURN)  # Pressiona Enter após digitar

    def get_text_title_resultado(self):
        try:
            # Espera até que o título do resultado de pesquisa esteja visível
            WebDriverWait(self.driver, 30).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, GooglePageLocator.TITLE_RESULTADO))
            )
            element = self.driver.find_element(By.CSS_SELECTOR, GooglePageLocator.TITLE_RESULTADO)
            return element.text
        except Exception as e:
            print("Erro ao localizar o título do resultado:", e)
            return None

    def close_cookie_popup(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, GooglePageLocator.POPUP_COOKIE)))
            cookie_popup = self.get_element(GooglePageLocator.POPUP_COOKIE)
            cookie_popup.click()
            print("Pop-up de cookies fechado com sucesso.")
        except Exception as e:
            print("Popup de cookies não encontrado ou já fechado:", e)

    def click_search_button(self):
        """ Método para clicar no botão de pesquisa principal """
        try:
            # Espera até o botão de pesquisa ficar visível e clicável
            search_button = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, GooglePageLocator.BUTTON_PESQUISAR))
            )
            search_button.click()  # Clicando no botão de pesquisa
            print("Botão de pesquisa clicado com sucesso.")
        except Exception as e:
            print("Erro ao clicar no botão de pesquisa:", e)
