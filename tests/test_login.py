import pytest
import allure

@allure.feature("Funcionalidade de Login")
@allure.story("Login bem-sucedido com credenciais válidas")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_sucesso():
    usuario = "admin"
    senha = "1234"
    
    with allure.step("Abrir a tela de login"):
        print("Tela de login aberta")
    
    with allure.step("Preencher usuário e senha"):
        print(f"Usuário: {usuario}, Senha: {senha}")
    
    with allure.step("Clicar no botão de login"):
        print("Clique no botão de login")
    
    with allure.step("Validar login"):
        assert usuario == "admin"
        assert senha == "1234"
        allure.attach(body="Usuário logado com sucesso", name="Resultado", attachment_type=allure.attachment_type.TEXT)


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
        assert senha == "1234", "Senha incorreta"
        allure.attach(body="Mensagem de erro exibida", name="Erro", attachment_type=allure.attachment_type.TEXT)
