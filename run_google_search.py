from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_google_search():
    # Definindo as opções do navegador
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=chrome-data")  # Caminho do seu perfil

    # Inicializando o WebDriver
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com")
    print("Acessando a página do Google...")

    # Esperando até o campo de pesquisa estar visível e preenchendo-o
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Python")

    # Esperando o botão de pesquisa estar clicável e clicando nele
    search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnK")))
    search_button.click()
    print("Botão de pesquisa clicado com sucesso!")

    # Esperando os resultados da pesquisa
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search")))
    print("Aguardando os resultados da pesquisa...")

    # Tentando localizar o título dos resultados
    try:
        title = driver.title
        print(f"Título da página: {title}")
    except Exception as e:
        print(f"Erro ao localizar o título do resultado: {e}")

    # Fechando o navegador
    driver.quit()
    print("Navegador fechado com sucesso!")
