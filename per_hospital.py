from selenium import webdriver
import time
from bs4 import BeautifulSoup
from datetime import datetime
import csv
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

url = 'https://www.health.ntpc.gov.tw/basic/?mode=detail&node=788'

class Hospital():
    def __init__(self, driver) -> None:
        self.driver = driver

    def get_web(self, url):
        self.driver.get(url)
        time.sleep(1)
        return self.driver
    
    def click(self, xpath):
        element = self.driver.find_element('xpath', xpath)
        element.click()
        time.sleep(2)

driver = webdriver.Chrome()   
hospital = Hospital(driver)
hospital.get_web(url)

hospital_name = []
waiting_docs = []
waiting_hospitalization = []
whether_reported_119 = []
waiting_ICU = []
update_time = []
waiting_bed = [] 

# 馬偕醫院 - 台北分院
try:
    # 台北分院
    hospital.click('//*[@id="is_content"]/p[5]/a')
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    hospital_table = soup.find('table', {'id': 'GridView2'}).find_all('tr')
    hospital_name.append('馬偕醫院 - 台北分院')
    update_time.append(hospital_table[1].find_all('td')[1].text)
    whether_reported_119.append(hospital_table[2].find_all('td')[1].text)
    waiting_docs.append(hospital_table[3].find_all('td')[1].text)
    waiting_bed.append(hospital_table[4].find_all('td')[1].text)
    waiting_hospitalization.append(hospital_table[5].find_all('td')[1].text)
    waiting_ICU.append(hospital_table[6].find_all('td')[1].text)
    
    # 淡水分院
    hospital.click('//*[@id="RadioButtonList1_1"]')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    dan_table = soup.find('table', {'id': 'GridView2'}).find_all('tr')
    hospital_name.append('馬偕醫院 - 淡水分院')
    update_time.append(dan_table[1].find_all('td')[1].text)
    whether_reported_119.append(dan_table[2].find_all('td')[1].text)
    waiting_docs.append(dan_table[3].find_all('td')[1].text)
    waiting_bed.append(dan_table[4].find_all('td')[1].text)
    waiting_hospitalization.append(dan_table[5].find_all('td')[1].text)
    waiting_ICU.append(dan_table[6].find_all('td')[1].text)
    print(hospital_name, waiting_docs, waiting_bed, waiting_hospitalization, waiting_ICU, whether_reported_119, update_time)
except:
    with open('failed_urls.txt', 'a', encoding='utf-8') as file:
        file.write(f"Time: {datetime.now().strftime('%Y/%m/%d %H:%M:%S')}\n")
        file.write(f"Failed to scrape data from: {'馬偕醫院'}\n")


csv_file_path = 'hospital_data_mackay.csv'
with open(csv_file_path, mode='a', newline='', encoding = 'utf-8-sig') as csv_file:
    print('成功開啟')
    csv_writer = csv.writer(csv_file)
    for name, docs, beds, hospitalization, ICU, reported_119, update in zip(hospital_name, waiting_docs, waiting_bed, waiting_hospitalization, waiting_ICU, whether_reported_119, update_time):
        print(name, docs, beds, hospitalization, ICU, reported_119, update)
        csv_writer.writerow([name, docs, beds, hospitalization, ICU, reported_119, update])