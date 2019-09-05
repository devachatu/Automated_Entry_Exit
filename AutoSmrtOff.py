# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 21:15:55 2019

@author: devac
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 12:17:12 2019

@author: devac
"""
import time
import pywinauto
#import win32api
from pywinauto import application
import tkinter
import clipboard

def Xconv(x):
    x=int((x / 1366 * tkinter.Tk().winfo_screenwidth()))
    return(x)
def Yconv(y):
    y=int((y / 768 * tkinter.Tk().winfo_screenheight()))
    return(y)
    

app = application.Application()
app.start("c:\\Smart Office suite.exe")
time.sleep(5)
SMRTOFF = app.window(title='SmartOffice Login')
time.sleep(1)
SMRTOFF.Edit2.set_edit_text('smart')
SMRTOFF.Edit1.set_edit_text('smart')
SMRTOFF.Login.click()
SMRTOFF1=app.window(title='Smart Office Suite 9.5')
SMRTOFF1.wait('Ready')
SMRTOFF1.maximize()
time.sleep(2)
pywinauto.mouse.click(button='left', coords=(882,56))
time.sleep(2)
SMRTOFF2=app.window(title='Smart Office Suite 9.5 - [Device List]')
SMRTOFF2.Button.click_input()
SMRTOFF2.Button14.click_input()
time.sleep(2)
flag=1
for i in range(2):
    stime=time.time()
    #print(time.time()-stime)
    while (time.time() - stime)<=600:
        time.sleep(10)
        pywinauto.mouse.click(button='left', coords=(782,170+20*i))
        pywinauto.keyboard.send_keys('^c')
        text=clipboard.paste()
        print(text.find('Downloading Completed'))
        print("loop")
        if text.find('Downloading Completed')!=-1:
            flag=0
            print('Downloading Completed')
            break
        elif text.find('Unable To Connect')!=-1:
            print(flag)
            flag=1
            break

if flag==0:
    app.kill()
    app1 = application.Application()
    app1.start("E:\\ESSL\\WebRun.exe")
elif flag==1:
    print('Unable to connect') 

#print(win32api.GetCursorPos())


    
    
