from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

navegador = webdriver.Firefox()
navegador.get('https://web.whatsapp.com/')

time.sleep(15)
busca = navegador.find_element_by_xpath('XPATH WAY HERE')

busca.click()
time.sleep(2)
busca.send_keys('CONTACT HERE')
time.sleep(2)

contato = navegador.find_element_by_xpath('XPATH WAY HERE')
contato.click()

xd = navegador.find_element_by_xpath('XPATH WAY HERE')
time.sleep(2)
xd.send_keys('MESSAGE HERE' + Keys.ENTER)
time.sleep(2)

navegador.quit()