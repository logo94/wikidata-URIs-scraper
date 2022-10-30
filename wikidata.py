from operator import contains
from selenium.webdriver import Firefox
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from time import sleep
import openpyxl
import tkinter as tk
from tkinter import filedialog


url = "https://www.wikidata.org/wiki/Wikidata:Main_Page"

root = tk.Tk()
root.withdraw()
file = filedialog.askopenfilename()

fire_driver = GeckoDriverManager().install()
driver = Firefox(service=FirefoxService(fire_driver))
driver.maximize_window()
driver.get(url)

wb = openpyxl.load_workbook(file)
sh = wb.active
m_row = sh.max_row

def title(cell):
    string = sh.cell(row = i, column=2).value
    return string

def get_uri(i):
    driver.get(url)
    txt = title(i)
    driver.find_element(By.NAME, 'search').send_keys(
        txt)
    sleep(1)
    driver.find_element(By.ID, 'searchButton').click()
    sleep(1)

    if driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[4]/div[4]/div[2]/ul/li[1]/table/tbody/tr/td[2]/div[1]/a/span/span[1]'):
        driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[4]/div[4]/div[2]/ul/li[1]/table/tbody/tr/td[2]/div[1]/a/span/span[1]').click()
        sleep(1)
        abText = driver.current_url
        abCell = sh.cell(row = i, column=1)
        abCell.value = "<" + abText + ">"
        wb.save(file)
    else:
        pass

for i in range(1, m_row + 1):
    try:
        get_uri(i)
    except:
        pass
