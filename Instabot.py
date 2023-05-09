from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

try:
    # navegar para a página de login do Instagram
    driver = webdriver.Firefox(executable_path='C:/Users/Jean/Área de Trabalho/geckodriver/geckodriver.exe')
    driver.get('https://www.instagram.com/accounts/login/')

    # espera para página carregar
    time.sleep(2)

    # insere o nome de usuário
    username_field = driver.find_element_by_name("username")
    username_field.send_keys("seu_usuario")

    # insere a senha
    password_field = driver.find_element_by_name("password")
    password_field.send_keys("sua senha")

    # envia o formulário
    password_field.send_keys(Keys.RETURN)

    # espera o processo de login completar
    time.sleep(5)

    # navegar para o seu perfil do Instagram
    driver.get("https://www.instagram.com/seuusuario/")

except Exception as e:
    print(e)
