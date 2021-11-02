from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
print("sample test case started")
driver = webdriver.Chrome(r"C:\Users\maurogiannopoulos\PycharmProjects\pythonProjectTest\Browsers\chromedriver.exe")
#driver=webdriver.firefox()
#driver=webdriver.ie()
#maximize the window size
driver.maximize_window()
#navigate to the url
driver.get("https://www.google.gr/")
time.sleep(3)
#click on the Accept terms button
driver.find_element_by_id("L2AGLb").send_keys(Keys.ENTER)
time.sleep(3)
#identify the Google search text box and enter the value
driver.find_element_by_name("q").send_keys("javatpoint")
time.sleep(3)
#click on the Google search button
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(5)
#close the browser
driver.close()
print("sample test case successfully completed")