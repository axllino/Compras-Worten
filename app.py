from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support.select import Select
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as condicao_esperada


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1200,700', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)
    chrome_options.add_experimental_option('prefs', {
        # Auterar o local padrão do download de arquivos
        'download.default_directory': 'C:\\Users\\lino\\Desktop\\Compras Worten\\Compras-Worten\\download',
        # Notificar o google chrome sobre essa auteração
        'download.directory_upgrade': True,
        # Desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos download
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
    # Inicializando o webdriver
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchCookieException,
            ElementNotVisibleException,
            ElementNotSelectableException
        ]
    )

    return driver, wait


driver, wait = iniciar_driver()


def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1, 5)/30)


# navegar até o site
driver.get('https://www.worten.pt')
sleep(2)

# botao_windows = driver.find_element(By.ID, 'WindowsRadioButton')

permitir_cookies = driver.find_element(
    By.XPATH, '//button[@class="button--primary button--md button--black button"]')
sleep(3)
permitir_cookies.click()
sleep(2)


botao_fazer_login = wait.until(condicao_esperada.visibility_of_element_located(
    (By.XPATH, '//button[@aria-label="Iniciar Sessão"]')))
sleep(2)
botao_fazer_login.click()

botao_iniciar_sessao = wait.until(condicao_esperada.visibility_of_element_located(
    (By.XPATH, '//a[@href="/cliente/conta#/myLogin"]')))
sleep(3)
botao_iniciar_sessao.click()
sleep(5)
# botao_windows = driver.find_element(By.ID, 'WindowsRadioButton')
campo_username = driver.find_element(By.XPATH, '//input[@id="username"]')
sleep(2)
texto01 = 'axlmotivacao@gmail.com'
digitar_naturalmente(texto01, campo_username)
sleep(3)

campo_senha_usuario = driver.find_element(
    By.XPATH, '//input[@type="password"]')
texto02 = 'EZ3nURgEC5'
digitar_naturalmente(texto02, campo_senha_usuario)


botao_entrar = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH, '//button[@type="submit"]')))
sleep(2)
botao_entrar.click()
sleep(10)

driver.execute_script("window.scrollTo(0, 800);")

# botao_worten = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//div[@class="main-nav__left-container"]')))
# sleep(2)
# botao_worten.click()
# sleep(10)


botao_adicionar_carrinho = wait.until(condicao_esperada.visibility_of_any_elements_located(
    (By.XPATH, '//button[@class="product-card__add-to-cart button--primary button--sm button--red button product-card__add-to-cart"]')))
sleep(2)
botao_adicionar_carrinho[0].click()
sleep(10)

botao_carrinho = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH, '//a[@aria-label="Carrinho"]')))
sleep(2)
botao_carrinho.click()
sleep(10)


# driver.execute_script('arguments[0].click()', botao_radio)
# botao_radio.send_keys(Keys.DOWN)

input('Aperte uma tecla para fechar')
