from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# iniciar a nova aba do Firefox
driver = webdriver.Firefox()

# navegar para  apagina de login do Instagram
driver = webdriver.Firefox(executable_path='/https://www.instagram.com/accounts/login/')

# espera para pagina carregar
time.sleep(2)

# enter usuario e a senha e faz o log in
username_field = driver.find_element_by_name("username")
username_field.send_keys("gringohti")
password_field = driver.find_element_by_name("password")
password_field.send_keys("D3vjean%123")
password_field.send_keys(Keys.RETURN)

# espera o processo de login completar
time.sleep(5)

# navegar para o seu perfil do  Instagram
driver.get("https://www.instagram.com/gringohti/")