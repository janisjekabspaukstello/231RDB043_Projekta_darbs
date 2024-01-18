import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from openpyxl import Workbook, load_workbook 

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

dati=load_workbook('dati.xlsx')
speletaji=dati['Latvijas_Speletaji']
kanali=dati['YT_kanali']

lastRow = kanali.max_row
for rinda in range(2,lastRow+1):
    saite=(kanali['d' + str(rinda)].value)
    pedejais = (kanali['b' + str(rinda)].value)
    url = str(saite)
    driver.get(url)
    time.sleep(2)
    cookies_no = driver.find_element(By.CLASS_NAME,"VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc iMLaPd")
    cookies_no.click
    time.sleep(2)
    latest = driver.find_element(By.ID,"video-title-link")
    saite = latest.get_attribute("href")
    jaunais = saite
    if(pedejais == jaunais):
        kanali['c'+str(rinda)].value= "tas pats"
    else:
        kanali['c'+str(rinda)].value= "JAUNS"
        kanali['b'+str(rinda)].value= jaunais
