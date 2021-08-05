# $$$$$$$$$$$$$$$$$$$$$$$$

from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
from random import seed
from random import random
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains

'''
from selenium.webdriver.chrome.service import Service
service = Service('C:/Users/Seb/PycharmProjects/pythonProjectTinBo/chromedriver_win32 (1)/chromedriver.exe')
service.start()
'''


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument('headless')
chrome_options.add_argument('--hide-scrollbars')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('???')
chrome_options.add_argument('--no-proxy-server')



driver = webdriver.Chrome('/home/odg/shubham/scraping/chromedriver',chrome_options=chrome_options)

#list all industry
industry_list=["Computer Software", "Information technology","Internet"]



driver.get('https://www.linkedin.com/uas/login?session_redirect=%2Fsales&_f=navigator&fromSignIn=true&trk=sales-home-page_nav-header-signin&src=direct%2Fnone&veh=direct%2Fnone')
driver.maximize_window()
driver.delete_all_cookies()  

##########
soup_list=[]
sop1=[]
sop2=[]
sop3=[]
def crawler(soup):
    div_soup=soup.find('ol',{'class':'search-results__result-list'})
    (soup_list.append(div_soup))
    links=soup_list[0].find_all('a',{'data-anonymize':'company-name'})
    list=[]
    for link in links:
        (list.append("https://www.linkedin.com/"+link.get('href')))
  
    for i in list:
        driver.get(i)
        time.sleep(10)
        res = driver.page_source
        soups= BeautifulSoup(res, 'html.parser')
        sop1.append(soups)
        WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/section/section[1]/div[2]/section[1]/div[1]/p/div/button'))).click()
#         time.sleep(10)
        res = driver.page_source
        soups= BeautifulSoup(res, 'html.parser')
        sop2.append(soups)
        time.sleep(5)
        WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[11]/div/div/button'))).click()
        
        
        WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/section/div[1]/section/div/div[1]/div/div[1]/button[4]'))).click()
        time.sleep(5)
        res = driver.page_source
        soups= BeautifulSoup(res, 'html.parser')
        sop3.append(soups)
#         print(so3)11
        
        name=sop2[0].find('div',{'class','artdeco-entity-lockup__title ember-view'})
       
        print(name.text.replace('\n',' ').strip())
        overview=sop2[0].find('p',{'class','company-details-panel-description flex white-space-pre-wrap t-14'})
        overview.text.replace('\n',' ').strip()
        website_link=sop2[0].find('a',{'class','ember-view company-details-panel-website t-14'})
        print(website_link.text.replace('\n',' ').strip())
        total_emp_count=sop2[0].find('div',{'class','employee-count'}).find('dt',{'class','t-14 t-bold'})
        total_emp_count.text
        founded=sop2[0].find('dd',{'class','company-details-panel__content company-details-panel-founded t-black--light'})
        print(founded.text)
        growth_rate=sop2[0].find('div',{'class','insights__summary ph5 pv4'}).find_all('dt',{'class','t-14 t-bold'})
        six_month=growth_rate[1].text.replace('\n',' ').strip()
        print(six_month)
        one_year=growth_rate[2].text.replace('\n',' ').strip()
        print(one_year)
        two_year=growth_rate[3].text.replace('\n',' ').strip()
        sop1.clear()
        sop2.clear()
        sop3.clear()



#loging
def Login():


    WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/main/div[2]/form/div[1]/input'))).send_keys('sanjeevdirwal30@gmail.com')
    WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/main/div[2]/form/div[2]/input'))).send_keys('pranay@123')
    driver.find_element_by_xpath('/html/body/div/main/div[2]/form/div[2]/input').send_keys(Keys.ENTER)
    driver.back()
    WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/main/div[2]/form/div[2]/input'))).send_keys('pranay@123')
    driver.find_element_by_xpath('/html/body/div/main/div[2]/form/div[2]/input').send_keys(Keys.ENTER)

Login()



def Filter():
    
    time.sleep(25)
    WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/header/div/div[2]/section/div/div[1]/div/div/div[2]/a'))).click()
    # time.sleep(2)
    # nexts = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(), 'High')]")))

    # elements = driver.find_elements_by_class_name("advanced-search-filter__label  t-14 t-black t-bold cursor-inherit m0 search-filter__textLabel")
    # elements.click
    WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[10]/div/div/div[2]/div/div[2]/div/section[1]/ul/li[4]/div/div/div[2]/span'))).click()
    
    
    # time.sleep(5)

    WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[10]/div/div/div[2]/div/div[2]/div/section[1]/ul/li[4]/div/div/div[3]/input'))).send_keys('Israel')
        

    WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[10]/div/div/div[2]/div/div[2]/div/section[1]/ul/li[4]/div/div/div[3]/ol/li[1]/button/strong'))).click()
    
    
    # time.sleep(5)
    WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[10]/div/div/div[2]/div/div[2]/div/section[1]/ul/li[6]/div/div/div[1]/div/div/label'))).click()

    for indus in industry_list:
        WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[10]/div/div/div[2]/div/div[2]/div/section[1]/ul/li[6]/div/div/div[3]/input'))).send_keys(indus)
        time.sleep(1)
        WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[10]/div/div/div[2]/div/div[2]/div/section[1]/ul/li[6]/div/div/div[3]/ol/li[1]/button'))).click()

    #slecting companyheadcount
    
    
    WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[10]/div/div/div[2]/div/div[2]/div/section[3]/ul/li[2]/div/div/div/div/div/label'))).click()
    
    
    time.sleep(3)
    for i in range(0,5):
        WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[10]/div/div/div[2]/div/div[2]/div/section[3]/ul/li[2]/div/div/div[3]/ol/li[2]/button'))).click()

    WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[10]/div/div/div[1]/div[2]/button/span'))).click()  
       
    WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/header/div/div[3]/div/a[2]'))).click() 
    actions = ActionChains(driver)
    for _ in range(8):
        actions.send_keys(Keys.SPACE).perform()
        time.sleep(1)
        
    time.sleep(2)
    res = driver.page_source
    soup = BeautifulSoup(res, 'html.parser')  
    crawler(soup)

Filter()    








#######crawler###########333



    