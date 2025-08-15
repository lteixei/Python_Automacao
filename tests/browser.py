from selenium import webdriver

class Browser:
    def __init__(self):
        # Remover a opção headless para ver o navegador
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")  # Remova ou comente esta linha para ver o navegador
        self.driver = webdriver.Chrome(options=options)
        print("Navegador iniciado com sucesso!")

    def quit(self):
        if self.driver:
            self.driver.quit()
            print("Navegador fechado com sucesso!")
