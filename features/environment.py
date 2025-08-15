from tests.browser import Browser

def before_all(context):
    print("Iniciando o navegador...")
    context.browser = Browser()
    print("Navegador iniciado!")

def after_all(context):
    if hasattr(context, 'browser'):
        print("Fechando o navegador...")
        context.browser.quit()
