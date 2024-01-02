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
# hospital.click('//*[@id="is_content"]/p[3]/a')
# driver.close()
# driver.switch_to.window(driver.window_handles[0])
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# hospital_table = soup.find('table', {'class': 'page_table'}).find_all('tr')
# with open(hospital_log_path, 'a', encoding='utf-8') as f:
#     f.write('衛生福利部雙和醫院')
#     f.write('\n')
#     for row in hospital_table[1:]:
#         for td in row.find_all('td'):
#             f.write(td.text)
#             f.write(' ')
#         f.write('\n')


# # 亞東紀念醫院
# hospital.get_web(url)
# hospital.click('//*[@id="is_content"]/p[4]/a')
# driver.close()
# driver.switch_to.window(driver.window_handles[0])
# hospital.get_table('row circle-list circle-color', '衛生福利部雙和醫院', 'div')

# 淡水馬偕醫院
# hospital.get_web(url)
# hospital.click('//*[@id="is_content"]/p[5]/a')
# driver.close()
# driver.switch_to.window(driver.window_handles[0])
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# hospital_table = soup.find('table', {'id': 'GridView2'}).find_all('tr')
# with open(hospital_log_path, 'a', encoding='utf-8') as f:
#     f.write('淡水馬偕醫院')
#     f.write('\n')
#     for row in hospital_table[1:]:
#         for td in row.find_all('td'):
#             f.write(td.text)
#             f.write(' ')
#         f.write('\n')

# 慈濟醫院
# hospital.get_web(url)
# hospital.click('//*[@id="is_content"]/p[6]/a')
# driver.close()
# driver.switch_to.window(driver.window_handles[0])
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# hospital_table = soup.find('table', {'id': 'gv'}).find_all('tr')
# with open(hospital_log_path, 'a', encoding='utf-8') as f:
#     f.write('淡水馬偕醫院')
#     f.write('\n')
#     th_list = []
#     td_list = []
#     for row in hospital_table:
#         for th in row.find_all('th'):
#             th_list.append(th.text)
#         for td in row.find_all('td'):
#             td_list.append(td.text)
#     for th, td in zip(th_list, td_list):
#         f.write(th)
#         f.write(' ')
#         f.write(td)
#         f.write('\n')

# 耕莘醫院
# hospital.get_web(url)
# hospital.click('//*[@id="is_content"]/p[7]/a')
# driver.close()
# driver.switch_to.window(driver.window_handles[0])
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# hospital_table = soup.find('div', {'id': 'layer1'}).find_all('p')
# with open(hospital_log_path, 'a', encoding='utf-8') as f:
#     f.write('耕莘醫院 - 新店分院')
#     f.write('\n')
#     for row in hospital_table:
#         for b in row.find_all('b'):
#             f.write(b.text)

# hospital.click('//*[@id="layer2"]/a')
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# hospital_table = soup.find('div', {'id': 'layer1'}).find_all('p')
# with open(hospital_log_path, 'a', encoding='utf-8') as f:
#     f.write('耕莘醫院 - 安康分院')
#     f.write('\n')
#     for row in hospital_table[:-1]:
#         for b in row.find_all('b'):
#             f.write(b.text)

# 國泰綜合醫院
# hospital.get_web(url)
# hospital.click('//*[@id="is_content"]/p[9]/a')
# driver.close()
# driver.switch_to.window(driver.window_handles[0])
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# hospital_table = soup.find('table').find_all('tr')
# with open(hospital_log_path, 'a', encoding='utf-8') as f:
#     f.write('國泰綜合醫院')
#     f.write('\n')
#     for row in hospital_table:
#         for b in row.find_all('td')[1:3]:
#             f.write(b.text)
#         f.write('\n')


# 恩主公醫院
hospital.get_web(url)
hospital.click('//*[@id="is_content"]/p[10]/a')
driver.close()
driver.switch_to.window(driver.window_handles[0])

with open(hospital_log_path, 'a', encoding='utf-8') as f:
    for i in range(2, 6):
        print(i)
        element = driver.find_element('xpath', f'//*[@id="main"]/div/div/main/div[2]/div/div[3]/div[{i}]')
        # f.write(element.text[0], element.text[1])
        # f.write(' ')
        print(element.text)
