from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import re



class login_logout():

    def setUp(self):
        print("Login-Logout test case started")
        self.driver = webdriver.Chrome(r"C:\Users\maurogiannopoulos\PycharmProjects\pythonProjectTest\Browsers\chromedriver.exe")
        # wait time before close
        self.driver.implicitly_wait(30)
        #Full window
        self.driver.maximize_window()
        # navigate to the url
        self.driver.get("http://lhmbqa.intralot.com/")
        time.sleep(1)
        #click on the Accept cookies button
        self.driver.find_element_by_id("onetrust-accept-btn-handler").send_keys(Keys.ENTER)
        time.sleep(3)
        #click on the Accept terms button
        self.driver.find_element_by_xpath('//*[@id="mainScroll"]/header/div[2]/div[3]/div[2]/div/div/div[2]/button[1]').send_keys(Keys.ENTER)

    def login(self):
        # Enter Username
        self.driver.find_element_by_xpath("//input[@placeholder='Please enter username or email']").send_keys("skandalaki")
        # time.sleep(1)

        # Enter Password
        self.driver.find_element_by_xpath("//input[@placeholder='Please enter password']").send_keys("123456q!")
        # time.sleep(3)

        # find and click submit button to login
        self.driver.find_element_by_class_name("btn-primary").send_keys(Keys.ENTER)
        time.sleep(20)

    # verify if text exists to verify login
    def verify_login(self):
        login_verify = self.driver.find_element_by_class_name("modal-title").text
        if login_verify == "Player Information":
            print("Log in is successfull:", login_verify)
            #now logout
            #dismiss the window
            self.driver.find_element_by_class_name("btn-primary").send_keys(Keys.ENTER)
            #Close the window
            self.driver.find_element_by_class_name("close").send_keys(Keys.ENTER)

            # identify image
            l = driver.find_element_by_xpath("//img[@alt='skandalaki']")
            s = l.get_attribute("title");
            print("Title attribute value is :" + s);
            l.click();
        else:
            print("something went wrong with the login")

    def logout(self):
        logout = self.driver.find_element_by_xpath("//div[@class='link' and text()='Logout']")
        logout.click()
        time.sleep(3)


    def verify_logout(self):
        # identify image
        images = self.driver.find_elements_by_tag_name('img')
        login_exist = "0"
        for image in images:
            # print(image.get_attribute('src'))
            if image.get_attribute('src') == "/static/ui/common/login.svg":
                login_exist = "1"

        if login_exist == "1":
            print("log out was successfull")
        else:
            print("something went wrong with the logout")


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

