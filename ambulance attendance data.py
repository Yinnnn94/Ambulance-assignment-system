import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl as oxl
from datetime import date,datetime
import time
import random
location_name=[]
captians=[]
time_list=[]
type_list=[]

def ambulance():
    driver_path=r"C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe" #Selenium of Chrome path
    browser=webdriver.Chrome(driver_path)
    url='http://119.ylfire.gov.tw:8080/DTS/caselist/html' #website
    browser.get(url) 
    times=browser.find_elements("xpath",'//tbody/tr/td[2]')#grab the time
    types=browser.find_elements("xpath",'//tbody/tr/td[3]')# grab the type
    location=browser.find_elements("xpath",'//tbody/tr/td[4]') # grab the location
    captian=browser.find_elements("xpath",'//tbody/tr/td[5]') # grab the department
    for adrr,cap,t,typess in zip(location,captian,times,types): # append the data in list
        location_name.append(adrr.text)
        captians.append(cap.text)
        time_list.append(t.text)
        type_list.append(typess.text)
    browser
    return location_name,captians,time_list,type_list
    
lat=[]
log=[]
def locaiton():
    driver_path=r"C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe"
    browser=webdriver.Chrome(driver_path)
    delay_choices = [8, 5, 10, 6, 20, 11]  #delay of time
    delay = random.choice(delay_choices)  # random time to avoid the website think I'm a robot!
    
    for i in location_name:
        url='http://www.map.com.tw/'
        browser.get(url)
        # browser.find_elements('xpath','//*[@id="Menu"]/div[2]').clear() #clear the search input
        browser.find_element('xpath','//*[@id="searchWord"]').send_keys(Keys.CONTROL,"a")
        browser.find_elements('xpath','//*[@id="Menu"]/div[2]').clear()
        # search_word
        time.sleep(delay)  #delay
        browser.find_element('xpath','//*[@id="searchWord"]').send_keys(i) # input the location
        browser.find_element('xpath','//*[@id="Menu"]/div[2]/img[2]').click() 
        time.sleep(delay) 
        inframe=browser.find_element('xpath','//*[@id="customMarkinfowindow"]/div/iframe') # find the pop window
        browser.switch_to.frame(inframe) #switch to the pop window
        browser.find_element('xpath','//*[@id="defaultInfo"]/table/tbody/tr[3]/td/table/tbody/tr/td[2]').click() #click the lat and long
        a=browser.find_element('xpath','//*[@id="location"]/table/tbody/tr[2]/td') # grab them
        a = a.text.strip().split()
        latitude = a[-1].split("：")[-1] #split!
        longtitude = a[0].split("：")[-1]
        lat.append(latitude) 
        log.append(longtitude)
        # browser.quit()
        print(i,lat,log)
    return lat,log


def get_data(path,today):
    data=pd.DataFrame(list(zip(time_list,location_name,captians,type_list,lat,log))
                    ,columns=["事發時間",'事發地點','派遣分局','案件類型','事發緯度','事發經度'])
    with pd.ExcelWriter(path) as writer:  
        data.to_excel(writer,encoding="utf_8_sig",sheet_name=today,index=False)

def run():
    ambulance()
    locaiton()
    get_data(path,today)


today=str(date.today()) #today time
path=r"C:\Users\user\ambulance%s.xlsx"%(today)
run()

