from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
from bs4 import BeautifulSoup
import time
from lxml import html
import string
from googletrans import Translator


driver = webdriver.Chrome()
driver.get("https://m.facebook.com/login/") #  https://m.facebook.com/login/
email = "" #логин для входа
password = "" #пароль для входа

email_xpath = '//*[@id="m_login_email"]'
pass_xpath = '//*[@id="m_login_password"]'
but_xpath = '//*[@id="login_password_step_element"]/button'

email_element = driver.find_element_by_xpath(email_xpath)
pass_element = driver.find_element_by_xpath(pass_xpath)
but_element = driver.find_element_by_xpath(but_xpath)

email_element.send_keys(email)
pass_element.send_keys(password)
but_element.click()

time.sleep(4)

try: 
  but_element_next = driver.find_element_by_xpath('//*[@id="root"]/table/tbody/tr/td/div/form/div/input') 
  but_element_next.click()     

  time.sleep(4)
  search_element = driver.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[2]/input')
  search_element.send_keys("Elena")
  time.sleep(2)
  pyautogui.press ('enter')
  time.sleep(6)
  main_page = driver.page_source
  soup = BeautifulSoup(main_page)
  for a in soup.find_all('a', href=True):
      if a['href'] != "#" and a['href'].find("search") == -1 and a['href'].find("refid=8") == -1 and a['href'].find("add_friend") == -1 :#a['href'].find("/search/people/?") != -1
          driver.get("https://m.facebook.com/" + a['href'])
except:
    but_element_next = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div[3]/div[2]/form/div/button') 
    but_element_next.click()   
    time.sleep(4)
    search_element = driver.find_element_by_xpath('//*[@id="search_jewel"]/a')
    search_element.click()
    time.sleep(2)
    input_element = driver.find_element_by_xpath('//*[@id="main-search-input"]')
    input_element.send_keys("Polina")
    time.sleep(2)
    pyautogui.press ('enter')
    
    time.sleep(6)

    words = {}

    main_page = driver.page_source
    soup = BeautifulSoup(main_page)
    for a in soup.find_all('a', href=True):
        if a['href'] != "#" and a['href'].find("search") == -1 and a['href'].find("refid=8") == -1 and a['href'].find("add_friend") == -1:
            driver.get("https://m.facebook.com/" + a['href']) 
            time.sleep(7)
            story_page = driver.page_source
            soup1 = BeautifulSoup(story_page)
            tags = soup1.find_all(['h2', 'p'])
            for tag in tags:
                text = tag.text.lower()
                sent = [w.strip(string.punctuation) for w in text.split()] #" ".join()
                for word in sent:
                    words[word] = sent.count(word)
    
    print(words)
    words = sorted(words.items(), key=lambda x: x[1], reverse=True)  
    print(words) 
    sorted_dict = {k: v for k, v in words}
    print(sorted_dict)
    keys = list(sorted_dict.keys())
    for k in keys:
        if len(k) > 2:
            word = k
            break
    print(word)
    #translator = Translator()
    #result = translator.translate(keys[0], dest='zh-tw')
    #print(f"original word: {keys[0]}, chinese: {result}")
