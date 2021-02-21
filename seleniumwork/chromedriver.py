from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import re



baseUrl = 'https://moodle.iitd.ac.in/login/index.php'
locationChromeDriver ='../drivers/chromedriver'

entryno = input("enter your entry number: ")


drive = webdriver.Chrome(executable_path=locationChromeDriver)
drive.get(baseUrl)

search = drive.find_element_by_name('username')
search.send_keys(entryno)


text = drive.find_element_by_id('login').text
temp = re.findall(r'\d+', text)
res= list(map(int, temp))
if 'first' in text:
    ans = res[0]

if 'second' in text:
    ans = res[1]

if 'add' in text:
    ans = res[0] + res[1]

if 'subtract' in text:
    ans = res[0] - res[1]

cap = drive.find_element_by_name('valuepkg3')
cap.send_keys(ans)
















