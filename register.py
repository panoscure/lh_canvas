from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import re



class register():

    def get_random_string(self):
        #random_source = string.ascii_letters + string.digits + string.punctuation
        random_source = string.ascii_letters + string.digits

        # select 1 lowercase
        password = random.choice(string.ascii_lowercase)
        # select 1 uppercase
        password += random.choice(string.ascii_uppercase)
        # select 1 digit
        password += random.choice(string.digits)
        # select 1 special symbol
        #password += random.choice(string.punctuation)

        # generate other characters
        for i in range(6):
            password += random.choice(random_source)

        password_list = list(password)
        # shuffle all characters
        random.SystemRandom().shuffle(password_list)
        password = ''.join(password_list)
        return password

    def get_random_numbers(self):
        #random_source = string.ascii_letters + string.digits + string.punctuation
        #random_source = string.ascii_letters + string.digits
        random_source = string.digits

        # select 1 digit
        password = random.choice(string.digits)
        # select 1 special symbol
        #password += random.choice(string.punctuation)

        # generate other characters
        for i in range(10):
            password += random.choice(random_source)

        password_list = list(password)
        # shuffle all characters
        random.SystemRandom().shuffle(password_list)
        password = ''.join(password_list)
        return password

    def setUp(self):
        print("Register test case started")
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
        #Find and press register button
        self.driver.find_element_by_xpath('//button[text()="Register"]').send_keys(Keys.ENTER)

    def bit8SetUp(self):
        print("Register test case started")
        self.driver = webdriver.Chrome(r"C:\Users\maurogiannopoulos\PycharmProjects\pythonProjectTest\Browsers\chromedriver.exe")
        # wait time before close
        self.driver.implicitly_wait(30)
        #Full window
        self.driver.maximize_window()
        # navigate to the url
        self.driver.get("http://10.85.42.10:1024/index.php/site/login#/../players/Index")
        time.sleep(1)
        #click on the Accept cookies button
        #self.driver.find_element_by_id("onetrust-accept-btn-handler").send_keys(Keys.ENTER)
        #time.sleep(3)
        #Find and press register button
        #self.driver.find_element_by_xpath('//button[text()="Register"]').send_keys(Keys.ENTER)

    def bit8_change_name(self):

        # Enter Username
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="login_username"]').send_keys("fatuser20180126")
        time.sleep(3)

        # Enter Password
        self.driver.find_element_by_xpath('//*[@id="login_password"]').send_keys("qoUjmWXtoab1vR86mm3g7")
        time.sleep(3)
        # Enter Password confirmation
        self.driver.find_element_by_xpath('//*[@id="submit_button"]').click()

        #find the player
        self.driver.find_element_by_id("ribbon-5").click()
        time.sleep(0.4)
        self.driver.find_element_by_xpath('//*[@id="ribbon-5-group"]/div[1]/ul/li[1]/a/div/img').click()
        time.sleep(7)
        # Enter Name to search
        self.driver.find_element_by_xpath('//*[@id="search_name_value"]').send_keys("rene")
        time.sleep(2.5)
        self.driver.find_element_by_xpath('//*[@id="search_surname_value"]').send_keys("Friedence")
        time.sleep(2.5)
        self.driver.find_element_by_id("search_button").send_keys(Keys.ENTER)
        time.sleep(5)
        self.driver.find_element_by_class_name("player_manage_btn").send_keys(Keys.ENTER)
        time.sleep(0.5)
        #click personal info
        self.driver.find_element_by_xpath('// *[ @ id = "player_personal_info_header"]').click()
        time.sleep(0.5)
        #click edit
        self.driver.find_element_by_id("btn_edit_personal_info").send_keys(Keys.ENTER)
        time.sleep(0.5)

        extra_string = self.get_random_string()

        #find name and replace it
        self.driver.find_element_by_id("name_field").send_keys(Keys.BACKSPACE)
        time.sleep(0.5)
        self.driver.find_element_by_id("name_field").send_keys(extra_string)
        time.sleep(3.5)
        #find surname and replace it
        self.driver.find_element_by_id("surname_field").send_keys(Keys.BACKSPACE)
        time.sleep(0.5)
        self.driver.find_element_by_id("surname_field").send_keys(extra_string)
        time.sleep(3.5)

        self.driver.find_element_by_xpath('//*[@id="personal_info_save_changes"]').send_keys(Keys.ENTER)
        time.sleep(0.5)
        #self.driver.find_element_by_link_text("Yes").send_keys(Keys.SPACE)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#page_players_player_info > div:nth-child(29) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(1)"))).click()

        time.sleep(2.5)

        #verify that username changed
        #Click on players is skipped as is already there
        #self.driver.find_element_by_id("ribbon-5").send_keys(Keys.ENTER)
        #time.sleep(0.4)

        self.driver.find_element_by_xpath('//*[@id="ribbon-5-group"]/div[1]/ul/li[1]/a/div/img').click()
        time.sleep(7)
        # Enter Name to search
        name = "ren"+extra_string
        surname = "friedenc"+extra_string
        self.driver.find_element_by_xpath('//*[@id="search_name_value"]').send_keys(name)
        time.sleep(2.5)
        self.driver.find_element_by_xpath('//*[@id="search_surname_value"]').send_keys(surname)
        time.sleep(0.5)
        self.driver.find_element_by_id("search_button").send_keys(Keys.ENTER)
        time.sleep(2.5)

        #check if player found
        try:
            player_found = self.driver.find_element_by_class_name("player_manage_btn")
        except NoSuchElementException:
            print("Could not find player with name: ",name)



    def register_process(self):

        # Enter Username
        extra_string = self.get_random_string()
        username = "renepanos"+extra_string
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@placeholder='username']").send_keys(username)
        time.sleep(3)

        # Enter Password
        self.driver.find_element_by_xpath("//input[@placeholder='password']").send_keys("123456q!")
        time.sleep(3)
        # Enter Password confirmation
        self.driver.find_element_by_xpath("//input[@placeholder='password confirmation']").send_keys("123456q!")
        time.sleep(2)
        # Enter e-mail address
        email = extra_string+"panoscure2@gmail.com"
        self.driver.find_element_by_xpath("//input[@placeholder='email address']").send_keys(email)
        time.sleep(4)
        # find and click Next button to go to step 2
        self.driver.find_element_by_xpath('//button[text()="Next"]').send_keys(Keys.ENTER)
        time.sleep(3)
        #########################################################Step 2#########################################
        #select male option
        select = Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "gender"))))
        select.select_by_visible_text("Male")
        time.sleep(2)
        # Enter First name
        self.driver.find_element_by_xpath("//input[@placeholder='first name']").send_keys("rene")
        time.sleep(2)
        # Enter surname
        self.driver.find_element_by_xpath("//input[@placeholder='surname']").send_keys("Friedence")
        time.sleep(2)
        # Enter street name
        self.driver.find_element_by_xpath("//input[@placeholder='street name']").send_keys("Veringstr.")
        time.sleep(2)
        # Enter street number
        self.driver.find_element_by_xpath("//input[@placeholder='street number']").send_keys("10")
        time.sleep(2)
        # Enter birthname
        self.driver.find_element_by_xpath("//input[@placeholder='Birth name']").send_keys("panos")
        time.sleep(1)
        # Enter postcode
        self.driver.find_element_by_xpath("//input[@placeholder='Postcode']").send_keys("21107")
        time.sleep(1)
        # Enter city
        self.driver.find_element_by_xpath("//input[@placeholder='City']").send_keys("hamburg")
        time.sleep(1)
        # Enter date of birth
        self.driver.find_element_by_xpath("//input[@placeholder='date of birth']").send_keys("22.05.1968")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@placeholder='date of birth']").send_keys(Keys.ENTER)
        time.sleep(1)
        # Enter place of birth
        self.driver.find_element_by_xpath("//input[@placeholder='Place Of Birth']").send_keys("Veringstr")
        time.sleep(1)
        # Enter Phone number
        phone = self.get_random_numbers()
        self.driver.find_element_by_xpath("//input[@placeholder='phone number']").send_keys(phone)
        time.sleep(1)
        # Select phone number prefix
        time.sleep(1)
        select = Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "countryPrefix"))))
        select.select_by_visible_text("+30")
        # Enter IBAN
        self.driver.find_element_by_xpath("//input[@placeholder='IBAN number']").send_keys("DE19511700240033177700")
        time.sleep(3)
        # find and click Next button to go to step 3
        self.driver.find_element_by_xpath('//button[text()="Next"]').send_keys(Keys.ENTER)
        time.sleep(7)
##########################################################step 3#####################################################
        #click all checkboxes
        self.driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(3)
        checkbox_element = self.driver.find_elements_by_class_name("label-after")
        #y = checkbox_element.location['y']
        #driver.execute_script('window.scrollTo(0, {0})'.format(y))


        print("checkbox element", checkbox_element)
        for checkbox in checkbox_element:
            print(checkbox)
            checkbox.click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//button[text()="Confirm"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//button[text()="Verify"]').click()
        time.sleep(5)

        #checkbox_element.click()

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
            l = self.driver.find_element_by_xpath("//img[@alt='skandalaki']")
            s = l.get_attribute("title")
            print("Title attribute value is :" + s)
            l.click()
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


setup = register()



#initial setup, open browser, close cookies etc.
setup.setUp()
driver = setup.driver
#Find and press login button
setup.register_process()
#close browser
#driver.close()

#bit8 Clear user just created
#bit8 login
setup.bit8SetUp()
#change the name for bit8
setup.bit8_change_name()




#close the browser
#driver.close()
print("sample test case successfully completed")

