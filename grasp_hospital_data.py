from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
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


hospital_log_path = 'hospital_log.txt'
driver = webdriver.Chrome()    
hospital = Hospital(driver)
hospital.get_web(url)


hospital_name = []
waiting_docs = []
waiting_hospitalization = []
whether_reported_119 = []
update_time = []
waiting_bed = []

# 衛生福利部雙和醫院
hospital.click('//*[@id="is_content"]/p[3]/a')
driver.close()
driver.switch_to.window(driver.window_handles[0])
soup = BeautifulSoup(driver.page_source, 'html.parser')
hospital_table = soup.find('table', {'class': 'page_table'}).find_all('tr')
hospital_name.append('衛生福利部雙和醫院')
if '未' in hospital_table[0].find_all('td')[1].text:
    whether_reported_119.append('否')
else:
    whether_reported_119.append('是')
waiting_docs.append(hospital_table[1].find_all('td')[1].text)
waiting_bed.append(hospital_table[2].find_all('td')[1].text)
waiting_hospitalization.append(hospital_table[3].find_all('td')[1].text)
update_time.append(hospital_table[-1].find_all('td')[0].text)

# 亞東紀念醫院
hospital.get_web(url)
hospital.click('//*[@id="is_content"]/p[4]/a')
driver.close()
driver.switch_to.window(driver.window_handles[0])
soup = BeautifulSoup(driver.page_source, 'html.parser')
hospital_name.append('亞東紀念醫院')
need_data = []
for i in range(1, 6):
    element = driver.find_element('xpath', f'//*[@id="page__main"]/div[2]/div[1]/div[2]/div[{i}]')
    text = element.text.replace("\n", " ")
    text_split = text.split(' ')
    need_data.append(text_split[2])
whether_reported_119.append(need_data[0])
waiting_docs.append(need_data[1])
waiting_bed.append(need_data[2])
waiting_hospitalization.append(need_data[3])
update_time.append(driver.find_element('xpath', '//*[@id="page__main"]/div[2]/div[1]/div[1]').text.split()[1])



# 淡水馬偕醫院
hospital.get_web(url)
hospital.click('//*[@id="is_content"]/p[5]/a')
driver.close()
driver.switch_to.window(driver.window_handles[0])
soup = BeautifulSoup(driver.page_source, 'html.parser')
hospital_table = soup.find('table', {'id': 'GridView2'}).find_all('tr')
hospital_name.append('淡水馬偕醫院')
update_time.append(hospital_table[1].find_all('td')[1].text.split()[2])
whether_reported_119.append(hospital_table[2].find_all('td')[1].text)
waiting_docs.append(hospital_table[3].find_all('td')[1].text)
waiting_bed.append(hospital_table[4].find_all('td')[1].text)
waiting_hospitalization.append(hospital_table[5].find_all('td')[1].text)




# 慈濟醫院 
hospital.get_web(url)
hospital.click('//*[@id="is_content"]/p[6]/a')
driver.close()
driver.switch_to.window(driver.window_handles[0])
soup = BeautifulSoup(driver.page_source, 'html.parser')
hospital_table = soup.find('table', {'id': 'gv'}).find_all('tr')
hospital_name.append('慈濟醫院')
if '未' in driver.find_element('xpath', '//*[@id="lblFull"]').text:
    whether_reported_119.append('否')
else:
    whether_reported_119.append('是')
waiting_docs.append(hospital_table[1].find_all('td')[0].text)
waiting_bed.append(hospital_table[1].find_all('td')[1].text)
waiting_hospitalization.append(hospital_table[1].find_all('td')[2].text)
update_time.append(hospital_table[1].find_all('td')[4].text.split()[-1])


# 耕莘醫院
hospital.get_web(url)
hospital.click('//*[@id="is_content"]/p[7]/a')
driver.close()
driver.switch_to.window(driver.window_handles[0])
soup = BeautifulSoup(driver.page_source, 'html.parser')
hospital_table = soup.find('div', {'id': 'layer1'}).find_all('p')
hospital_name.append('耕莘醫院 - 新店分院')
hospital_name.append('耕莘醫院 - 安康分院')
whether_reported_119.append(hospital_table[0].find_all('b')[0].text.split(' ')[0][-2])
waiting_docs.append(hospital_table[0].find_all('b')[1].text.split(' ')[0][-2])
waiting_bed.append(hospital_table[0].find_all('b')[2].text.split(' ')[0][-2])
waiting_hospitalization.append(hospital_table[0].find_all('b')[3].text.split('：')[1].split()[0])
update_time.append(driver.find_element('xpath', '//*[@id="layer3"]').text.split()[-1])

hospital.click('//*[@id="layer2"]/a')
soup = BeautifulSoup(driver.page_source, 'html.parser')
hospital_table = soup.find('div', {'id': 'layer1'}).find_all('p')
whether_reported_119.append(hospital_table[0].find_all('b')[0].text.split('：')[1].split()[0])
waiting_docs.append(hospital_table[1].find_all('b')[0].text.split('：')[1].split()[0])
waiting_bed.append(hospital_table[2].find_all('b')[0].text.split('：')[1].split()[0])
waiting_hospitalization.append(hospital_table[3].find_all('b')[0].text.split('：')[1].split()[0])
update_time.append(driver.find_element('xpath', '//*[@id="layer3"]').text.split()[-1])
        

# 國泰綜合醫院
hospital.get_web(url)
hospital.click('//*[@id="is_content"]/p[9]/a')
driver.close()
driver.switch_to.window(driver.window_handles[0])
soup = BeautifulSoup(driver.page_source, 'html.parser')
hospital_table = soup.find('table').find_all('tr')
hospital_name.append('國泰綜合醫院')
whether_reported_119.append(hospital_table[0].find_all('td')[2].text)
waiting_docs.append(hospital_table[1].find_all('td')[2].text)
waiting_bed.append(hospital_table[2].find_all('td')[2].text)
waiting_hospitalization.append(hospital_table[3].find_all('td')[2].text)
update_time.append(driver.find_element('xpath', '/html/body/p[2]').text.split()[1])



# 恩主公醫院 
hospital.get_web(url)
hospital.click('//*[@id="is_content"]/p[10]/a')
driver.close()
driver.switch_to.window(driver.window_handles[0])
need_data = []
for i in range(2, 7):
    element = driver.find_element('xpath', f'//*[@id="main"]/div/div/main/div[2]/div/div[3]/div[{i}]').text
    text_split = element.split()
    need_data.append(text_split[1])

hospital_name.append('恩主公醫院')
whether_reported_119.append(need_data[0])
waiting_docs.append(need_data[1])
waiting_bed.append(need_data[2])
waiting_hospitalization.append(need_data[3])
update_time.append(driver.find_element('xpath', '//*[@id="main"]/div/div/main/div[2]/div/div[1]').text.split()[-1])



# 耕莘醫院 - 永和分院
hospital.get_web(url)
hospital.click('//*[@id="is_content"]/p[11]/a')
driver.close()
driver.switch_to.window(driver.window_handles[0])
soup = BeautifulSoup(driver.page_source, 'html.parser')
hospital_table = soup.find('div', {'id': 'layer1'}).find_all('p')
hospital_name.append('耕莘醫院 - 永和分院')
whether_reported_119.append(hospital_table[0].find_all('b')[0].text.split(' ')[0][-2])
waiting_docs.append(hospital_table[1].find_all('b')[0].text.split('：')[1].split()[0])
waiting_bed.append(hospital_table[2].find_all('b')[0].text.split('：')[1].split()[0])
waiting_hospitalization.append(driver.find_elements('xpath', '//*[@id="Labelwaitipd"]')[0].text)
update_time.append(driver.find_element('xpath', '//*[@id="layer3"]').text)

# 衛生福利部台北醫院
hospital.get_web(url)
hospital.click('//*[@id="is_content"]/p[12]/a')
driver.close()
driver.switch_to.window(driver.window_handles[0])
soup = BeautifulSoup(driver.page_source, 'html.parser')
hospital_table = soup.find('table').find_all('tr')
hospital_name.append('衛生福利部台北醫院')
whether_reported_119.append(hospital_table[0].find_all('td')[1].text.split()[0])
waiting_docs.append(hospital_table[1].find_all('td')[1].text.split()[0])
waiting_bed.append(hospital_table[2].find_all('td')[1].text.split()[0])
waiting_hospitalization.append(hospital_table[3].find_all('td')[1].text.split()[0])
update_time.append(datetime.now().strftime("%H:%M:%S"))

# 聯合醫院
hospital.get_web(url)
hospital.click('//*[@id="is_content"]/p[13]/a')
driver.close()
driver.switch_to.window(driver.window_handles[0])
link = driver.find_element('xpath', '//*[@id="content_text"]/table/tbody/tr[4]/td/a')
hospital.get_web(link.get_attribute('href'))
soup = BeautifulSoup(driver.page_source, 'html.parser')
hospital_table = soup.find('table', {'id': 'GridView1'}).find_all('tr')
hospital_name.append('聯合醫院 - 三重分院')
whether_reported_119.append(hospital_table[1].find_all('td')[1].text)
waiting_docs.append(hospital_table[1].find_all('td')[2].text)
waiting_bed.append(hospital_table[1].find_all('td')[3].text)
waiting_hospitalization.append(hospital_table[1].find_all('td')[4].text)
update_time.append(hospital_table[1].find_all('td')[6].text.split()[1])

hospital_name.append('聯合醫院 - 板橋分院')
whether_reported_119.append(hospital_table[2].find_all('td')[1].text)
waiting_docs.append(hospital_table[2].find_all('td')[2].text)
waiting_bed.append(hospital_table[2].find_all('td')[3].text)
waiting_hospitalization.append(hospital_table[2].find_all('td')[4].text)
update_time.append(hospital_table[2].find_all('td')[6].text.split()[1])


# 輔仁大學附設醫院
hospital.get_web(url)
hospital.click('//*[@id="is_content"]/p[14]/a')
driver.close()
driver.switch_to.window(driver.window_handles[0])
soup = BeautifulSoup(driver.page_source, 'html.parser')
hospital_table = soup.find('table').find_all('tr')
hospital_name.append('輔仁大學附設醫院')
whether_reported_119.append(hospital_table[1].find_all('td')[1].text)
waiting_docs.append(hospital_table[2].find_all('td')[1].text.split()[0])
waiting_bed.append(hospital_table[3].find_all('td')[1].text.split()[0])
waiting_hospitalization.append(hospital_table[4].find_all('td')[1].text.split()[0])
update_time.append(hospital_table[-1].find_all('td')[0].text.split()[1])


# 土城醫院
hospital.get_web(url)
hospital.click('//*[@id="is_content"]/p[15]/a')
driver.close()
driver.switch_to.window(driver.window_handles[0])
soup = BeautifulSoup(driver.page_source, 'html.parser')
hospital_table = soup.find('table', {'class' : 'font15-22'}).find_all('tr')
hospital_name.append('土城醫院')
whether_reported_119.append(hospital_table[2].find_all('td')[1].text)
waiting_docs.append(hospital_table[3].find_all('td')[1].text)
waiting_bed.append(hospital_table[4].find_all('td')[1].text)
waiting_hospitalization.append(hospital_table[5].find_all('td')[1].text)
update_time.append(hospital_table[0].find_all('td')[0].text.split()[-1])

hospital_dict = {'hospital_name': hospital_name, 'waiting_docs': waiting_docs, 'waiting_bed' : waiting_bed , 'waiting_hospitalization' : waiting_hospitalization ,'whether_reported_119': whether_reported_119, 'update_time': update_time}

hospital_data_pd = pd.DataFrame(hospital_dict)
print(hospital_data_pd)
hospital_data_pd.to_csv('hospital_data.csv', index = False, encoding = 'utf-8-sig')