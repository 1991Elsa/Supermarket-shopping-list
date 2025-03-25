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


# Iniciar el navegador (asegúrate de tener el WebDriver correspondiente)
driver = webdriver.Chrome()  # Cambia si usas otro navegador

# Abrir la página web
driver.get(superone)  # Cambia por la URL real

# Esperar a que aparezca el banner de cookies
time.sleep(3)

try:
    # Buscar el botón "ACEPTAR" usando CSS Selector
    boton_aceptar = driver.find_element(By.CSS_SELECTOR, ".melindres-button.is-primary")
    boton_aceptar.click()  # Hacer clic en el botón
    print("✅ Cookies aceptadas.")
except Exception as e:
    print("❌ No se encontró el botón de aceptar cookies.", e)

try:
    # 1️⃣ Hacer clic en el campo del código postal
    campo_postal = driver.find_element(By.XPATH, '//form[@id="form_postalcode"]/span[1]/span[1]/span[1]/span[1]')
    campo_postal.click()
    time.sleep(2)
    print("Elemento clicado con éxito")
except Exception as e:
    print("❌ Error en el proceso.", e)

try:
    # Encontrar el campo de búsqueda y escribir el código postal
    campo_postal = driver.find_element(By.XPATH, '//input[@class="select2-search__field"]')
    campo_postal.click()  # Hacer clic para enfocar el campo
    campo_postal.send_keys("15220")  # Escribir el código postal
    time.sleep(1)  # Esperar un poco para que las opciones se filtren

    # Ahora, después de escribir el código postal, seleccionamos la opción correcta
    # Si la lista es desplegada, las opciones generalmente se colocan en un contenedor como <ul> o <li>
    # Aquí estamos buscando el texto dentro de las opciones, pero también puedes buscar por atributo o índice

    opcion_postal = driver.find_element(By.XPATH, '//li[contains(@class,"select2-results__option") and text()="15220"]')
    opcion_postal.click()  # Seleccionar la opción
    time.sleep(1)  # Esperar para asegurarse de que la opción se seleccionó

    print("✅ Código postal seleccionado con éxito")

    # Hacer clic en el botón "Aceptar"
    boton_aceptar = driver.find_element(By.XPATH, '//button[@class="btn principal_btn btn_new_client ladda-button"]/span[1]')
    boton_aceptar.click()
    
    print("✅ Botón de aceptar clickeado.")
except Exception as e:
    print("❌ Error en el proceso.", e)