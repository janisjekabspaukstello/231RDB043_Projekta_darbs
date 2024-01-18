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
speles=dati['Nesenas_Speles']
kanali=dati['YT_kanali']

lastRow = speletaji.max_row
for rinda in range(2,lastRow+1):
    vards=(speletaji['a' + str(rinda)].value) + " " + (speletaji['b' + str(rinda)].value)
    liga=(speletaji['c' + str(rinda)].value)
    komanda=(speletaji['d' + str(rinda)].value)
    if(liga == "NBA"):
        url = "https://www.nba.com/games"
        driver.get(url)
        time.sleep(2)
        # nba get
        # decline coocies
    if(liga == "EuroCup"):
        url = "https://www.euroleaguebasketball.net/eurocup/game-center/"
        driver.get(url)
        time.sleep(2)
        # eurocup get
        # accept coocies
    if(liga == "EuroLeague"):
        url = "https://www.euroleaguebasketball.net/euroleague/game-center/"
        driver.get(url)
        time.sleep(2)
        # euroleague get
        # accept coocies
lastRow = kanali.max_row
for rinda in range(2,lastRow+1):
    saite=(kanali['d' + str(rinda)].value)
    pedejais = (kanali['b' + str(rinda)].value)
    url = str(saite)
    driver.get(url)
    time.sleep(2)
    #pedejais video
    jaunais = 0
    #
    if(pedejais == jaunais):
        kanali['c'+str(rinda)].value= "tas pats"
    else:
        kanali['c'+str(rinda)].value= "JAUNS"
