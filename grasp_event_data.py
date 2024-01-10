from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime

location_name=[]
captians=[]
time_list=[]
type_list=[]

ambulance_url = 'https://e.tpf.gov.tw/'

log_path = 'ambulance_log.txt'

class Ambulance():
    def __init__(self, driver) -> None:
        self.driver = driver

    def get_web(self, url):
        self.driver.get(url)
        time.sleep(1)
        return self.driver
    
    def click(self, xpath):
        element = self.driver.find_element('xpath', xpath)
        element.click()
        time.sleep(1)

    def get_text(self, xpath):
        element = self.driver.find_element('xpath', xpath)
        return element.text
    

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options = options)    

# ambulance 
ambulance = Ambulance(driver)
ambulance.get_web(ambulance_url)
ambulance.click('//*[@id="vue-app"]/div[12]/div/div[2]/div/div[4]/div[2]/div[2]/div[2]/button[1]') # click the button to check the list form
ambulance.click('//*[@id="vue-app"]/div[12]/div/div[2]/div[1]/div[1]/div[3]/div[2]/button') # click the button for ambulance list

wait = WebDriverWait(driver, 3)
i = 1
with open(log_path, 'a', encoding='utf-8') as f:
    while True:
        xpath_expression = '//*[@id="vue-app"]/div[12]/div/div[2]/div[1]/div[3]/div/div[{}]/div/button[1]/div[3]'.format(i)
        try:
            element = wait.until(EC.presence_of_element_located(('xpath', xpath_expression)))
            now = datetime.today()
            f.write(now.strftime("%Y-%m-%d %H:%M:%S "))
            f.write(element.text)
            f.write('\n')
            i += 1
        except Exception as e:
            break




# fire

# fire = Ambulance(driver)
# fire.get_web(ambulance_url)
# fire.click('//*[@id="vue-app"]/div[12]/div/div[2]/div/div[4]/div[2]/div[2]/div[2]/button[1]') # click the button to check the list form

# fire data
# ambulance.click(f'//*[@id="vue-app"]/div[12]/div/div[2]/div[1]/div[3]/div/div[1]/div/button[2]')
# ambulance.get_web(driver.current_url)

# wait = WebDriverWait(driver, 3)

# i = 1
# with open(log_path, 'a', encoding='utf-8') as f:
#     while True:
#         xpath_expression = '//*[@id="panel_main_content"]/div[3]/div[2]/div[{}]/div/div[2]/div'.format(i)
#         try:
#             element = wait.until(EC.presence_of_element_located(('xpath', xpath_expression)))
#             f.write(element.text)
#             i += 1
#         except Exception as e:
#             break

# print(fire_data)


# def ambulance():
#     driver_path=r"C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe" #Selenium of Chrome path
#     browser=webdriver.Chrome(driver_path)
#     url='http://119.ylfire.gov.tw:8080/DTS/caselist/html' #website
#     browser.get(url) 
#     times=browser.find_elements("xpath",'//tbody/tr/td[2]')#grab the time
#     types=browser.find_elements("xpath",'//tbody/tr/td[3]')# grab the type
#     location=browser.find_elements("xpath",'//tbody/tr/td[4]') # grab the location
#     captian=browser.find_elements("xpath",'//tbody/tr/td[5]') # grab the department
#     for adrr,cap,t,typess in zip(location,captian,times,types): # append the data in list
#         location_name.append(adrr.text)
#         captians.append(cap.text)
#         time_list.append(t.text)
#         type_list.append(typess.text)
#     browser
#     return location_name,captians,time_list,type_list
    
# lat=[]
# log=[]
# def locaiton():
#     driver_path=r"C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe"
#     browser=webdriver.Chrome(driver_path)
#     delay_choices = [8, 5, 10, 6, 20, 11]  #delay of time
#     delay = random.choice(delay_choices)  # random time to avoid the website think I'm a robot!
    
#     for i in location_name:
#         url='http://www.map.com.tw/'
#         browser.get(url)
#         # browser.find_elements('xpath','//*[@id="Menu"]/div[2]').clear() #clear the search input
#         browser.find_element('xpath','//*[@id="searchWord"]').send_keys(Keys.CONTROL,"a")
#         browser.find_elements('xpath','//*[@id="Menu"]/div[2]').clear()
#         # search_word
#         time.sleep(delay)  #delay
#         browser.find_element('xpath','//*[@id="searchWord"]').send_keys(i) # input the location
#         browser.find_element('xpath','//*[@id="Menu"]/div[2]/img[2]').click() 
#         time.sleep(delay) 
#         inframe=browser.find_element('xpath','//*[@id="customMarkinfowindow"]/div/iframe') # find the pop window
#         browser.switch_to.frame(inframe) #switch to the pop window
#         browser.find_element('xpath','//*[@id="defaultInfo"]/table/tbody/tr[3]/td/table/tbody/tr/td[2]').click() #click the lat and long
#         a=browser.find_element('xpath','//*[@id="location"]/table/tbody/tr[2]/td') # grab them
#         a = a.text.strip().split()
#         latitude = a[-1].split("：")[-1] #split!
#         longtitude = a[0].split("：")[-1]
#         lat.append(latitude) 
#         log.append(longtitude)
#         # browser.quit()
#         print(i,lat,log)
#     return lat,log


# def get_data(path,today):
#     data=pd.DataFrame(list(zip(time_list,location_name,captians,type_list,lat,log))
#                     ,columns=["事發時間",'事發地點','派遣分局','案件類型','事發緯度','事發經度'])
#     with pd.ExcelWriter(path) as writer:  
#         data.to_excel(writer,encoding="utf_8_sig",sheet_name=today,index=False)

# def run():
#     ambulance()
#     locaiton()
#     get_data(path,today)


# today=str(date.today()) #today time
# path=r"C:\Users\user\ambulance%s.xlsx"%(today)
# run()

