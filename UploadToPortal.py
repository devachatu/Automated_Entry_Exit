# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 12:17:12 2019

@author: devac
"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import date,timedelta

def datec():
    dt = date.today()
    if date.weekday(dt) == 0 :
       dt=date.today()-timedelta(days=3)
       dt=dt.strftime("%d %b %Y")
       #print(dt)
       return(dt)
    else:
       dt=date.today()-timedelta(days=1)
       dt=dt.strftime("%d %b %Y")
       #print(dt)
       return(dt)
print(datec())
def press(a):
    elem=browser.find_element_by_xpath(a)
    elem.get_attribute('href')
    elem.click()
    
  #UPLOAD
print("Make sure chrome webdriver is located in C:\\driver\\chromedriver.exe'")
browser=webdriver.Chrome('C:\\driver\\chromedriver.exe')
browser.get('http://10.46.10.114:9001/login')
browser.maximize_window()
time.sleep(10)
UName=browser.find_element_by_name('user')#inspect element
UName.send_keys(Keys.CONTROL,'a')
UName.send_keys('attAdmin')
PWord=browser.find_element_by_name('password') #inspect element
PWord.send_keys(Keys.CONTROL,'a')
PWord.send_keys("Attadmin@123")
PWord.send_keys(Keys.ENTER)
time.sleep(15)
browser.get('http://10.46.10.114:9001/home')
press('/html/body/div[1]/div/div/div/ul/li[1]/a')
time.sleep(5)
browser.get('http://10.46.10.114:9001/setting')
press('//*[@id="loader-setting"]/div/div[1]/ul/li[3]/a')#inspect element
time.sleep(1)
press('//*[@id="mainDiv"]/div[2]/div/table/tbody/tr[8]/td/span')
Edate=browser.find_element_by_name('date')
Edate.send_keys(datec())
Edate.send_keys(Keys.ENTER)
time.sleep(1)
Edate.send_keys(Keys.ENTER)
time.sleep(3)
browser.close() 
                          
 #LOAD
browser=webdriver.Chrome('E:\\chromedriver_win32\\chromedriver.exe')
browser.get('https://machint.greythr.com/')
browser.maximize_window()
time.sleep(20)
UName=browser.find_element_by_name('username')
UName.send_keys(Keys.CONTROL,'a')
UName.send_keys('Test')
PWord=browser.find_element_by_name('password') #inspect element
PWord.send_keys(Keys.CONTROL,'a')
PWord.send_keys("Test@12345")
PWord.send_keys(Keys.ENTER)
time.sleep(15)
browser.get('https://machint.greythr.com/home.do#/')
press('/html/body/div[5]/div[1]/div/div[1]/ul/li[2]/a')
press('/html/body/div[5]/div[1]/div/div[2]/ul/li[2]/ul/li[3]/a/span')
press('/html/body/div[5]/div[1]/div/div[2]/ul/li[2]/ul/li[3]/ul/li[1]/a')
time.sleep(5)
browser.get('https://machint.greythr.com/ngapp/leave/admin/attendanceprocessor')
press('//*[@id="app-container"]/div/div[2]/div/div[2]/span')
fdate=browser.find_element_by_name('fromDate')
fdate.send_keys(Keys.CONTROL,'a')
fdate.send_keys(datec())
tdate=browser.find_element_by_name('toDate')
tdate.send_keys(Keys.CONTROL,'a')
tdate.send_keys(datec())
time.sleep(1)
tdate.send_keys(Keys.TAB)
time.sleep(1)
button=browser.find_element_by_css_selector('body > div.modal.ng-scope > div.modal-footer > button.btn.btn-medium.btn-primary')
button.click()
time.sleep(300)
browser.close()

