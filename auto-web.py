import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from pyautogui import *
import pyperclip
import winsound


#define alarmsound
def alarm_sound():
    winsound.Beep(400, 200)
    winsound.Beep(400, 200)
    winsound.Beep(500, 250)



#msg -> web.whatsapp
def open_wpp():
    press('winleft')
    time.sleep(10)    
    write('Chrome')
    time.sleep(3)
    press('enter')
    time.sleep(3)
    #clica na barra de pesquisa
    moveTo(273, 65)
    click()
    time.sleep(1)
    #abre wpp
    write(f'web')
    time.sleep(0.5)    
    press('enter')
    time.sleep(25)
    #clica no meu proprio contato
    moveTo(147, 378)
    click()
    time.sleep(0.5)
    hotkey('ctrl', 'v')
    time.sleep(15)


#tempo aleatório
sleepy = random.randint(4, 9)

#login bom dia mercado
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.headless = True
driver = webdriver.Chrome(options=options)
#https://www.bomdiamercado.com.br/exclusivo-assinante

driver.get("https://www.bomdiamercado.com.br/exclusivo-assinante")
while len(driver.find_elements('xpath', '//*[@id="email"]')) < 1:
    time.sleep(2)

time.sleep(sleepy)
driver.find_element('xpath', '//*[@id="email"]').send_keys('fernandolodi@capribr.com')
time.sleep(sleepy)
driver.find_element('xpath', '//*[@id="password"]').send_keys('Caprifo@3220')
time.sleep(sleepy)
#driver.find_element('xpath', '//*[@id="next_button_default"]').click()
driver.find_element('xpath', '//*[@id="password"]').send_keys(Keys.ENTER)
time.sleep(sleepy)

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
#print(bomdia)

#copia texto bom dia
pyperclip.copy(bomdia)
print(bomdia)

driver.close()
time.sleep(2)

#usa pyautogui para mandar a msg pelo whatsapp para mim mesmo
open_wpp()

alarm_sound()
