from os import environ
from py_rpautom.desktop_utils import simular_digitacao
from py_rpautom.python_utils import abrir_arquivo_texto, cls
from py_rpautom.web_utils import (
    aguardar_elemento,
    iniciar_navegador,
    clicar_elemento,
    escrever_em_elemento,
)
from time import sleep


XPATH = 'xpath'
user_github = environ.get('user_github')
password_github = environ.get('password_github')
url_project_github = environ.get('url_project_github')
caminho_dados = r'C:\dev\projects\input_task_kanban_github\data\function_list_pyrpautom.csv'

conteudo_dados = abrir_arquivo_texto(
    caminho=caminho_dados,
    encoding='utf8',
).splitlines()

caminho_executavel = (
    r'C:\Users\arumeidaaran\webdrivers\edgedriver\130.0.2849.68\msedgedriver.exe'
)

iniciar_navegador(
    url=url_project_github,
    nome_navegador='edge',
    options=(('--start-maximized',)),
    baixar_webdriver_previamente=False,
    executavel=caminho_executavel,
)

input_username = '//input[@name="login"]'
aguardar_elemento(
    identificador=input_username,
    tipo_elemento=XPATH
)
escrever_em_elemento(
    seletor=input_username,
    texto=user_github,
    tipo_elemento=XPATH
)

input_password = '//input[@name="password"]'
aguardar_elemento(
    identificador=input_password,
    tipo_elemento=XPATH
)
escrever_em_elemento(
    seletor=input_password,
    texto=password_github,
    tipo_elemento=XPATH
)

button_signin = '//input[@value="Sign in"]'
clicar_elemento(
    seletor=button_signin,
    tipo_elemento=XPATH
)

button_add_item = '(//span[text()="Add item"])[2]/parent::*/parent::*'
aguardar_elemento(
    identificador=button_add_item,
    tipo_elemento=XPATH
)
clicar_elemento(
    seletor=button_add_item,
    tipo_elemento=XPATH
)

input_name_new_item = '//input[@id="combobox-input-1"]'
aguardar_elemento(
    identificador=input_name_new_item,
    tipo_elemento=XPATH
)

cls()

for new_card in conteudo_dados[1::]:
    new_card = new_card.split(';')

    modulo_name = new_card[0]
    funcao_name = new_card[1]

    new_card_title = '_'.join(
        (
            modulo_name,
            funcao_name,
        )
    )

    print('\n', new_card_title, '\n')

    escrever_em_elemento(
        seletor=input_name_new_item,
        texto=new_card_title,
        tipo_elemento=XPATH
    )

    simular_digitacao(texto='{ENTER}')

    sleep(1)
