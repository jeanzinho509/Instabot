# Instabot
Ele abre seu navegador de Firefox e Efetua o login na sua conta do Instagram

#  processo geral de uso

1- Primeiro, você precisa instalar o Selenium e o webdriver do Firefox. Você pode instalar o Selenium usando o seguinte comando no terminal:

pip install selenium

2- Em seguida, você precisa baixar o webdriver do Firefox a partir do seguinte link: https://github.com/mozilla/geckodriver/releases

3- Depois de baixar o webdriver, descompacte o arquivo e salve o caminho completo para o arquivo geckodriver.exe em uma variável.

driver_path = 'C:/geckodriver.exe' # exemplo

4- Agora, você precisa localizar os elementos de entrada de usuário e senha no formulário de login do Instagram usando o método find_element_by_name() e enviar suas respectivas informações.

Obs: Além disso, é importante verificar se o caminho especificado para o arquivo geckodriver.exe está correto. Certifique-se de que o caminho esteja correto, incluindo a unidade (no caso de sistemas Windows) e a extensão do arquivo (.exe).
