import requests
from selenium import webdriver
import chromedriver_py
import time

url='https://www.linkedin.com/in/arslan-arshad-ai-engineer/'

driver=webdriver.Chrome()
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.get(url=url)
time.sleep(10)

cookies_dict = {}
for cookie in driver.get_cookies():
    cookies_dict[cookie['name']] = cookie['value']

driver.close()
print(cookie)

headers={'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
          'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'accept-encoding':'gzip, deflate, br, zstd',
          'accept-language':'en-US,en;q=0.9',
          'upgrade-insecure-requests':'1',
          'scheme': 'https',
 }

response=requests.get(url,cookies=cookies_dict,headers=headers)
html=response.text
print(html)
html_path='D:/PROGRAMING/Programing/1.4_Python_Scraping/linkedin_scraping/1.html'
page_fun=open(html_path,'w',encoding='utf-8')
page_fun.write(html)
page_fun.close() 