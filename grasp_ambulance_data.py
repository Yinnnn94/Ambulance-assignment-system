from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

from datetime import datetime

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

    def select(self, xpath, text):
        filter = Select(self.driver.find_element('xpath', xpath))
        filter.select_by_visible_text(text)

    def get_table(self, table_class_name, hospital_name):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        hospital_table = soup.find('table', {'class': table_class_name})
        print(hospital_table)
        with open(hospital_log_path, 'a', encoding='utf-8') as f:
            now = datetime.today()
            f.write(hospital_name)
            f.write(now.strftime(" %Y-%m-%d %H:%M:%S"))
            f.write('\n')
            for row in hospital_table.find_all('tr'):
                for td in row.find_all('td'):
                    f.write(td.text)
                    f.write(' ')
                f.write('\n')

hospital_log_path = 'hospital_log.txt'
driver = webdriver.Chrome()    
hospital = Hospital(driver)
hospital.get_web(url)

# 衛生福利部雙和醫院
hospital.click('//*[@id="is_content"]/p[3]/a')
driver.close()
driver.switch_to.window(driver.window_handles[0])
soup = BeautifulSoup(driver.page_source, 'html.parser')
hospital_table = soup.find('table', {'class': 'page_table'}).find_all('tr')
with open(hospital_log_path, 'a', encoding='utf-8') as f:
    f.write('衛生福利部雙和醫院')
    f.write('\n')
    for row in hospital_table[1:]:
        for td in row.find_all('td'):
            f.write(td.text)
            f.write(' ')
        f.write('\n')
    f.write('-' * 50)
    f.write('\n')


# # 亞東紀念醫院
hospital.get_web(url)
hospital.click('//*[@id="is_content"]/p[4]/a')
driver.close()
driver.switch_to.window(driver.window_handles[0])
with open(hospital_log_path, 'a', encoding='utf-8') as f:
    f.write('亞東紀念醫院')
    f.write(driver.find_element('xpath', '//*[@id="page__main"]/div[2]/div[1]/div[1]').text)
    f.write('\n')
    for i in range(1, 5):
        element = driver.find_element('xpath', f'//*[@id="page__main"]/div[2]/div[1]/div[2]/div[{i}]')
        text = element.text.replace("\n", " ")
        text_split = text.split(' ')
        f.write(text_split[0] +  text_split[1])
        f.write(' ')
        f.write(text_split[2])
        f.write('\n')
    f.write('-' * 50)
    f.write('\n')



# 淡水馬偕醫院
hospital.get_web(url)
hospital.click('//*[@id="is_content"]/p[5]/a')
driver.close()
driver.switch_to.window(driver.window_handles[0])
soup = BeautifulSoup(driver.page_source, 'html.parser')
hospital_table = soup.find('table', {'id': 'GridView2'}).find_all('tr')
with open(hospital_log_path, 'a', encoding='utf-8') as f:
    f.write('淡水馬偕醫院')
    f.write('\n')
    for row in hospital_table[1:]:
        for td in row.find_all('td'):
            f.write(td.text)
            f.write(' ')
        f.write('\n')
    f.write('-' * 50)
    f.write('\n')

# 慈濟醫院 <- 沒有119通報的資料
hospital.get_web(url)
hospital.click('//*[@id="is_content"]/p[6]/a')
driver.close()
driver.switch_to.window(driver.window_handles[0])
soup = BeautifulSoup(driver.page_source, 'html.parser')
hospital_table = soup.find('table', {'id': 'gv'}).find_all('tr')
with open(hospital_log_path, 'a', encoding='utf-8') as f:
    f.write('慈濟醫院')
    f.write('\n')
    th_list = []
    td_list = []
    for row in hospital_table:
        for th in row.find_all('th'):
            th_list.append(th.text)
        for td in row.find_all('td'):
            td_list.append(td.text)
    for th, td in zip(th_list, td_list):
        f.write(th)
        f.write(' ')
        f.write(td)
        f.write('\n')
    f.write('-' * 50)
    f.write('\n')

# 耕莘醫院
hospital.get_web(url)
hospital.click('//*[@id="is_content"]/p[7]/a')
driver.close()
driver.switch_to.window(driver.window_handles[0])
soup = BeautifulSoup(driver.page_source, 'html.parser')
hospital_table = soup.find('div', {'id': 'layer1'}).find_all('p')
with open(hospital_log_path, 'a', encoding='utf-8') as f:
    f.write('耕莘醫院 - 新店分院')
    f.write('\n')
    for row in hospital_table:
        for b in row.find_all('b'):
            b = b.text.replace('\n', ' ')
            b = b.replace(' ', '')
            f.write(b)
            f.write('\n')
    f.write('-' * 50)
    f.write('\n')

hospital.click('//*[@id="layer2"]/a')
soup = BeautifulSoup(driver.page_source, 'html.parser')
hospital_table = soup.find('div', {'id': 'layer1'}).find_all('p')
with open(hospital_log_path, 'a', encoding='utf-8') as f:
    f.write('耕莘醫院 - 安康分院')
    f.write('\n')
    for row in hospital_table[:-1]:
        for b in row.find_all('b'):
            b = b.text.replace('\n', ' ')
            b = b.replace(' ', '')
            f.write(b)
        f.write('\n')
    f.write('-' * 50)
    f.write('\n')
        

# 國泰綜合醫院 <- 沒有時間
hospital.get_web(url)
hospital.click('//*[@id="is_content"]/p[9]/a')
driver.close()
driver.switch_to.window(driver.window_handles[0])
soup = BeautifulSoup(driver.page_source, 'html.parser')
hospital_table = soup.find('table').find_all('tr')
with open(hospital_log_path, 'a', encoding='utf-8') as f:
    f.write('國泰綜合醫院')
    f.write('\n')
    for row in hospital_table:
        for b in row.find_all('td')[1:3]:
            f.write(b.text)
        f.write('\n')
    f.write('-' * 50)
    f.write('\n')


# 恩主公醫院 <- 沒有時間
hospital.get_web(url)
hospital.click('//*[@id="is_content"]/p[10]/a')
driver.close()
driver.switch_to.window(driver.window_handles[0])
with open(hospital_log_path, 'a', encoding='utf-8') as f:
    for i in range(2, 7):
        element = driver.find_element('xpath', f'//*[@id="main"]/div/div/main/div[2]/div/div[3]/div[{i}]')
        text = element.text.replace("\n", " ")
        f.write(text)
        f.write('\n')
    f.write('-' * 50)
    f.write('\n')


# 耕莘醫院 - 永和分院 <- 沒有時間
hospital.get_web(url)
hospital.click('//*[@id="is_content"]/p[11]/a')
driver.close()
driver.switch_to.window(driver.window_handles[0])
soup = BeautifulSoup(driver.page_source, 'html.parser')
hospital_table = soup.find('div', {'id': 'layer1'}).find_all('p')
with open(hospital_log_path, 'a', encoding='utf-8') as f:
    f.write('耕莘醫院 - 永和分院')
    f.write('\n')
    for row in hospital_table:
        for b in row.find_all('b'):
            f.write(b.text)
    f.write('-' * 50)
    f.write('\n')

# 衛生福利部台北醫院 <- 沒有時間
hospital.get_web(url)
hospital.click('//*[@id="is_content"]/p[12]/a')
driver.close()
driver.switch_to.window(driver.window_handles[0])
soup = BeautifulSoup(driver.page_source, 'html.parser')
hospital_table = soup.find('table').find_all('tr')
with open(hospital_log_path, 'a', encoding='utf-8') as f:
    f.write('衛生福利部台北醫院')
    f.write('\n')
    for row in hospital_table:
        for td in row.find_all('td'):
            td_ = td.text.replace(' ', '')
            td_ = td_.replace('\n', '')
            f.write(td_)
        f.write('\n')
    f.write('-' * 50)
    f.write('\n')

# 聯合醫院
hospital.get_web(url)
hospital.click('//*[@id="is_content"]/p[13]/a')
driver.close()
driver.switch_to.window(driver.window_handles[0])
link = driver.find_element('xpath', '//*[@id="content_text"]/table/tbody/tr[4]/td/a')
hospital.get_web(link.get_attribute('href'))
soup = BeautifulSoup(driver.page_source, 'html.parser')
hospital_table = soup.find('table', {'id': 'GridView1'}).find_all('tr')
th_list, td_list = [], []
with open(hospital_log_path, 'a', encoding='utf-8') as f:
    for row in hospital_table:
        for th in row.find_all('th'):
            th_list.append(th.text)
            # f.write(th.text)
        for td in row.find_all('td'):
            td_list.append(td.text)
    for th, three_data in zip(th_list, td_list[:7]):
        f.write(th)
        f.write(' ')
        f.write(three_data)
        f.write('\n')
    for th, ban in zip(th_list, td_list[7:]):
        f.write(th)
        f.write(' ')
        f.write(ban)
        f.write('\n')
    f.write('-' * 50)
    f.write('\n')

# 輔仁大學附設醫院
hospital.get_web(url)
hospital.click('//*[@id="is_content"]/p[14]/a')
driver.close()
driver.switch_to.window(driver.window_handles[0])
soup = BeautifulSoup(driver.page_source, 'html.parser')
hospital_table = soup.find('table').find_all('tr')
with open(hospital_log_path, 'a', encoding='utf-8') as f:
    f.write('輔仁大學附設醫院')
    f.write('\n')
    for row in hospital_table[1:]:
        for td in row.find_all('td'):
            td_ = td.text.replace('\n', '')
            td_ = td_.replace(' ', '')
            f.write(td_)
            f.write(' ')
        f.write('\n')
    f.write('-' * 50)
    f.write('\n')

# 土城醫院 <- 沒有時間
hospital.get_web(url)
hospital.click('//*[@id="is_content"]/p[15]/a')
driver.close()
driver.switch_to.window(driver.window_handles[0])
soup = BeautifulSoup(driver.page_source, 'html.parser')
hospital_table = soup.find('table', {'class' : 'font15-22'}).find_all('tr')
title = ['已向119通報滿床', '等待看診人數', '等待推床人數', '等待住院人數', '等待加護住院人數']
with open(hospital_log_path, 'a', encoding='utf-8') as f:
    f.write('土城醫院')
    f.write('\n')
    for row, t in zip(hospital_table, title):
        f.write(t)
        f.write(' ')
        for td in row.find_all('td'):
            td_ = td.text.replace('\n', '')
            td_ = td_.replace(' ', '')
            f.write(td_)
        f.write('\n')
    f.write('-' * 50)
    f.write('\n')

