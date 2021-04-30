#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import getpass

#Enter Credentials
print("Enter your your email: ")
usrname = input()
print("Enter your your password: ")
passwrd = getpass.getpass()

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
 
#Login
driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1619651017&rver=6.7.6631. 0&wp=MBI_SSL&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttps%253a%252f%252f www.bing.com%252f%253fFORM%253dZ9FD1%2526wlsso%253d1%2526wlexpsignin%253d1%26sig%3d2F298F20C6EC631032609F07C7466265 &lc=1033&id=264960&CSRFToken=23650bdc-1204-4521-a01e-ceacf97214eb&aadredir=1")
email = driver.find_element_by_id("i0116")
email.send_keys(usrname)
email.send_keys(Keys.RETURN)

password = driver.find_element_by_id("i0118")
password.send_keys(passwrd)
password.send_keys(Keys.RETURN)

time.sleep(1)
   
submitButton = driver.find_element_by_id("idSIButton9")
submitButton.click()
          
#Searches
time.sleep(1)
for i in range(0, 50):
    driver.get("https://www.bing.com/")

    search = driver.find_element_by_name("q")
    search.send_keys(i)
    search.send_keys(Keys.RETURN)
    
driver.quit() 


# In[ ]:





# In[ ]:




