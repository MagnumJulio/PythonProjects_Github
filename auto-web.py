from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib
import datetime
import time

#espera 6:40 para executar programa

while datetime.datetime.now().minute != 40 or datetime.datetime.now().hour != 5:
    time.sleep(1)

#login bom dia mercado
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
#https://www.bomdiamercado.com.br/exclusivo-assinante
driver.get("https://www.bomdiamercado.com.br/exclusivo-assinante")
while len(driver.find_elements('xpath', '//*[@id="email"]')) < 1:
    time.sleep(2)

time.sleep(5)
driver.find_element('xpath', '//*[@id="email"]').send_keys('')
time.sleep(5)
driver.find_element('xpath', '//*[@id="password"]').send_keys('')
time.sleep(5)
driver.find_element('xpath', '//*[@id="next_button_default"]').click()
time.sleep(5)

#pega mensagem de bom dia
bomdia = ""
time.sleep(5)

elemento_texto = driver.find_element('xpath', '/html/body/section/div/div[3]')
#/html/body/section/div/div[3]

html_content = elemento_texto.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html5lib')
titulo = soup.find('h3')
cont = 0
bomdia = '*' + titulo.text.title() + '*\n\n'
lista_soup = soup.find_all('p')
for texto in lista_soup:
    cont += 1
    if cont == 3:
        bomdia += texto.text + '\n\n'
    elif cont == (len(lista_soup)-3):
        print(texto.text)
        break
    else:
        bomdia += texto.text + '\n'
#soup = BeautifulSoup(html_content, 'html5lib')

print(bomdia)


#login whatsapp
driver.get("https://web.whatsapp.com/")
while len(driver.find_elements('id', 'side')) < 1:
    time.sleep(1)

#manda mensagem para mim mesmo
bomdia = urllib.parse.quote(bomdia)
link = f"https://web.whatsapp.com/send?phone={5531982544980}&text={bomdia}"
driver.get(link)
while len(driver.find_elements('id', 'side')) < 1:
    time.sleep(1)

#envia a msg
while len(driver.find_elements('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span')) < 1:
    time.sleep(1)
driver.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span').send_keys(Keys.ENTER)

time.sleep(10)



