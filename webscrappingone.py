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


excluir_categorias = [
    "Azúcar / edulcorantes", "Caramelos / chicles",
    "Precocinados", "Conservas cárnicas", "Conservas marisco",
    "Vinos de mes", "vinos gallegos", "vinos resto españa", "vinos importación", "bebidas espumosas", "aperitivos", "licores",
    "Harinas/papillas", "Leche polvo iniciación", "potitos/pures",
    "Pescadería", "Carnicería",
    "Morcillas/compangos", "Botillo/butelo/androlla",
    "Bazar", "Mascotas"
]


time.sleep(3)  
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

subcategoria_urls = []

categorias = soup.find_all("div", class_="label-row")

for categoria in categorias:
    categoria_nombre = categoria.find("a", class_="link_container").text.strip()
    
    if categoria_nombre in excluir_categorias:
        continue
    
    subcategorias = categoria.find_all("a", class_="plus-a")
    for subcategoria in subcategorias:
        subcategoria_nombre = subcategoria.text.strip()
        
        if subcategoria_nombre in excluir_categorias:
            continue
        
        productos = subcategoria.find_next_sibling("ul").find_all("a", class_="category_menu_link")
        for producto in productos:
            producto_nombre = producto.find("span", class_="category_menu_name").text.strip()
            producto_url = producto["href"]
            
            if producto_nombre not in excluir_categorias:
                subcategoria_urls.append((categoria_nombre, subcategoria_nombre, producto_nombre, producto_url))

for cat, subcat, prod, url in subcategoria_urls:
    print(f"Categoría: {cat} -> Subcategoría: {subcat} -> Producto: {prod} -> URL: {url}")

driver.quit()