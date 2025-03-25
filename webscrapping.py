import numpy as np
import pandas as pd

import requests
from bs4 import BeautifulSoup

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
from time import sleep

from links import superone


driver = webdriver.Chrome()  


driver.get(superone)  


time.sleep(3)

try:
 
    boton_aceptar = driver.find_element(By.CSS_SELECTOR, ".melindres-button.is-primary")
    boton_aceptar.click()  
    print(" Cookies aceptadas.")
except Exception as e:
    print(" No se encontró el botón de aceptar cookies.", e)

try:
 
    campo_postal = driver.find_element(By.XPATH, '//form[@id="form_postalcode"]/span[1]/span[1]/span[1]/span[1]')
    campo_postal.click()
    time.sleep(2)
    print("Elemento clicado con éxito")
except Exception as e:
    print("Error en el proceso.", e)

try:
  
    campo_postal = driver.find_element(By.XPATH, '//input[@class="select2-search__field"]')
    campo_postal.click()  
    campo_postal.send_keys("15220")  
    time.sleep(1) 



    opcion_postal = driver.find_element(By.XPATH, '//li[contains(@class,"select2-results__option") and text()="15220"]')
    opcion_postal.click()  
    time.sleep(1) 

    print(" Código postal seleccionado con éxito")


    boton_aceptar = driver.find_element(By.XPATH, '//button[@class="btn principal_btn btn_new_client ladda-button"]/span[1]')
    boton_aceptar.click()
    
    print("Botón de aceptar clickeado.")
except Exception as e:
    print(" Error en el proceso.", e)