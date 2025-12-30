import os, sys
sys.path.append('C:\\Users\\neket\\OneDrive\\Документы\\tg_bomb')
sys.path.append('C:\\Users\\neket\\AppData\\Local\\Programs\\Python\\Python314\\python314.zip')
sys.path.append('C:\\Users\\neket\\AppData\\Local\\Programs\\Python\\Python314\\DLLs')
sys.path.append('C:\\Users\\neket\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\site-packages')
sys.path.append('C:\\Users\\neket\\AppData\\Local\\Programs\\Python\\Python314')
sys.path.append('C:\\Users\\neket\\AppData\\Local\\Programs\\Python\\Python314\\Lib')
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchFrameException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
import time

def open(net, interval = 0):
 time.sleep(60)
 options = webdriver.ChromeOptions()
 options.add_argument("--disable-blink-features=AutomationControlled")
 options.add_argument("--no-sandbox")
 options.add_argument("--disable-dev-shm-usage")
 options.add_argument("--disable-gpu")
 options.add_argument("--disable-extensions")
 options.add_argument("--disable-infobars")
 options.add_argument("--start-maximized")
 options.add_argument("--window-size=1920,1080")
 options.add_argument("--ignore-certificate-errors")
 options.add_argument("--allow-running-insecure-content")
 options.add_argument("--disable-web-security")
 options.add_argument("--disable-features=IsolateOrigins,site-per-process")
 user_agent = (
     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
     "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
 )
 options.add_argument(f"user-agent={user_agent}")
 options.add_experimental_option('useAutomationExtension', False)
 options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
 options.add_experimental_option('excludeSwitches', ['enable-logging'])
 
 while True:
  drivery = webdriver.Chrome(options=options)
  drivery.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
  url='https://bot-tgf.onrender.com/'
  drivery.get(url)
  time.sleep(30)
  drivery.quit()
  time.sleep(600)

open()
