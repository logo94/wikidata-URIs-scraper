from selenium.webdriver import Firefox
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from time import sleep
import openpyxl
import tkinter as tk
from tkinter import filedialog


url = "https://it.wikipedia.org/wiki/Pagina_principale"

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
    string = sh.cell(row = i, column=3).value
    return string

def get_uri(i):
    driver.get(url)
    txt = title(i)
    driver.find_element(By.NAME, 'search').send_keys(
        txt)
    sleep(1)
    driver.find_element(By.ID, 'searchButton').click()
    sleep(3)
    
    driver.find_element(By.XPATH,
    '/html/body/div[4]/div[2]/nav[3]/div/ul/li[8]/a/span').click()
        
    abText = driver.current_url
    abCell = sh.cell(row = i, column=1)
    abCell.value = "<" + abText + ">"
    wb.save(file)

for i in range(1, m_row + 1):
    try:
        get_uri(i)
    except:
        pass