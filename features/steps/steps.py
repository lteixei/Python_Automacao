from behave import given, when, then
from tests.browser import Browser
from tests.google_page import GooglePage

@given('que acesso a página do Google')
def step_impl(context):
    print("Acessando a página do Google...")
    context.browser = Browser()
    context.page = GooglePage(context.browser.driver)
    context.page.acess_page('https://www.google.com')  # Acesse o Google explicitamente
    print("Página do Google acessada com sucesso!")

@when('preencho o campo de pesquisa com "{texto}"')
def step_impl(context, texto):
    print(f"Preenchendo o campo de pesquisa com o texto: {texto}")
    context.page.send_keys_input_pesquisa(texto)
    context.page.click_svg_button()
    print(f"Texto '{texto}' enviado com sucesso!")

@then('devo visualizar os resultados')
def step_impl(context):
    print("Verificando se os resultados estão visíveis...")
    result = context.page.get_text_title_resultado()
    assert result is not None, "Título do resultado não encontrado!"
    print("Resultados encontrados com sucesso!")
