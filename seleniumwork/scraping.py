from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium.webdriver import ChromeOptions

import time
import re

import main
t= 1
for b in range(int(t)):


    cnumber  = input("enter your contest number")

    baseUrl = 'https://codeforces.com/contest/' + str(cnumber)
    locationChromeDriver = '../drivers/chromedriver'


    drive = webdriver.Chrome(executable_path=locationChromeDriver)
    drive.get(baseUrl)
    rows = drive.find_elements_by_xpath("//table/tbody/tr")
    num = len(rows)
    for i in range(num):

        drive.find_element_by_xpath(
            '//*[@id="pageContent"]/div[2]/div[6]/table/tbody/tr[' + str(i + 2) + ' ]/td[2]/div/div[1]/a').click()
        drive.save_screenshot("screenshot/"+str(cnumber)+str(i+1)+".png")
        dpoints = drive.find_elements_by_tag_name("pre")
        loops = len(dpoints)
        for j in range (loops):
            intext = drive.find_elements_by_tag_name("pre")[j].text
            #print(intext)
            file = open("testcase/"+ str(cnumber)+str(i+1)+ str(j) +".txt","w")
            file.write(intext)

        drive.back()













time.sleep(10)


