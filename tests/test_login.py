import pytest
import allure

@allure.feature("Funcionalidade de Login")
@allure.story("Falha no login com senha incorreta")
@allure.severity(allure.severity_level.NORMAL)
def test_login_falhou():
    usuario = "admin"
    senha = "errado"

    with allure.step("Abrir a tela de login"):
        print("Tela de login aberta")

    with allure.step("Preencher usuário e senha incorretos"):
        print(f"Usuário: {usuario}, Senha: {senha}")

    with allure.step("Clicar no botão de login"):
        print("Clique no botão de login")

    with allure.step("Validar mensagem de erro"):
        # Aqui, em vez de comparar diretamente com a senha, você pode validar a mensagem de erro.
        # Simulando que, se a senha for incorreta, deve retornar "Senha incorreta"
        assert senha != "1234", "Senha incorreta"  # Simula que a senha não é a correta
        allure.attach(body="Mensagem de erro exibida", name="Erro", attachment_type=allure.attachment_type.TEXT)
