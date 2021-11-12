from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import re
import pandas as pd



class lh_xls():


    def setUp(self,link):
        print("Login-Logout test case started")
        self.driver = webdriver.Chrome(r"C:\Users\maurogiannopoulos\PycharmProjects\pythonProjectTest\Browsers\chromedriver.exe")
        # wait time before close
        self.driver.implicitly_wait(30)
        #Full window
        self.driver.maximize_window()
        # navigate to the url
        self.driver.get(link)
        time.sleep(1)
        #click on the Accept cookies button
        self.driver.find_element_by_id("onetrust-accept-btn-handler").send_keys(Keys.ENTER)
        time.sleep(2)
        #click on the Accept terms button
        self.driver.find_element_by_xpath('//*[@id="mainScroll"]/header/div[2]/div[3]/div[2]/div/div/div[2]/button[1]').send_keys(Keys.ENTER)

    def get_link(self):
        workbook = pd.read_excel('lh.xlsx')
        workbook.head()
        # Print the 1st value of the Product column
        link = workbook['link'].iloc[0]
        print("Link from XLS is: ",link)
        return link

    def get_bit8_link(self):
        workbook = pd.read_excel('lh.xlsx')
        workbook.head()
        # Print the 1st value of the Product column
        bit8_link = workbook['bit8_link'].iloc[0]
        print("bit8_link from XLS is: ",bit8_link)
        return bit8_link

    def get_bit8_user(self):
        workbook = pd.read_excel('lh.xlsx')
        workbook.head()
        # Print the 1st value of the Product column
        bit8_user = workbook['bit8_user'].iloc[0]
        print("bit8_user from XLS is: ",bit8_user)
        return bit8_user

    def get_bit8_password(self):
        workbook = pd.read_excel('lh.xlsx')
        workbook.head()
        # Print the 1st value of the Product column
        bit8_password = workbook['bit8_password'].iloc[0]
        print("bit8_password from XLS is: ",bit8_password)
        return bit8_password

    def get_username(self):
        workbook = pd.read_excel('lh.xlsx')
        workbook.head()
        # Print the 1st value of the Product column
        username = workbook['username'].iloc[0]
        print("username from XLS is: ",username)
        return username

    def get_password(self):
        workbook = pd.read_excel('lh.xlsx')
        workbook.head()
        # Print the 1st value of the Product column
        password = workbook['password'].iloc[0]
        print("password from XLS is: ",password)
        return password

'''
setup = login_logout()
#initial setup, open browser, close cookies etc.
setup.setUp()
driver = setup.driver
#Find and press login button
setup.login()
#verify login
setup.verify_login()
#press logout
setup.logout()
#verify if logout is successfull
setup.verify_logout()

#close the browser
driver.close()
print("sample test case successfully completed")
'''
