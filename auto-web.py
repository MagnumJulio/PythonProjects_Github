from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib
import datetime
import time
from pyautogui import *
import sys
import webbrowser as wb
import pyperclip

#msg -> bomdia
def open_wpp(bomdia):
    press('winleft')
    time.sleep(5)    
    write('Chrome')
    time.sleep(5)
    press('enter')
    time.sleep(2)
    #entra na conta google
    moveTo(569, 531)
    click()
    time.sleep(1)
    #clica na barra de pesquisa
    moveTo(436, 60)
    click()
    time.sleep(1)
    #https://web.whatsapp.com/send?phone={5531982544980}&text={bomdia}
    write(f'web')
    time.sleep(0.5)    
    press('enter')
    time.sleep(10)    
    #click()
    #write(f'https://web.whatsapp.com/send?phone={5531982544980}')
    #time.sleep(0.5)    
    #press('enter')
    time.sleep(5)
    moveTo(317, 351)
    click()
    hotkey('ctrl', 'v') 
    #write(bomdia)
    time.sleep(20)
    press('enter')
    #time.sleep(0.5)    
    #press('enter')

#espera 6:40 para executar programa
'''
while datetime.datetime.now().minute != 40 or datetime.datetime.now().hour != 5:
    time.sleep(1)
'''

#login bom dia mercado
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#options.add_experimental_option("--headless")
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
bomdia = '*' + titulo.text + '*\n\n'
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


#bomdia = "Olá"
pyperclip.copy(bomdia)
print(bomdia)

driver.close()

#enviar msg pelo wpp já aberto com pyautogui
open_wpp(bomdia)
