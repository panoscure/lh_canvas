from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import re


print("sample test case started")
driver = webdriver.Chrome(r"C:\Users\maurogiannopoulos\PycharmProjects\pythonProjectTest\Browsers\chromedriver.exe")
#driver=webdriver.firefox()
#driver=webdriver.ie()
#maximize the window size
driver.maximize_window()
#navigate to the url
driver.get("http://lhmbqa.intralot.com/")
time.sleep(3)

#click on the Accept cookies button
driver.find_element_by_id("onetrust-accept-btn-handler").send_keys(Keys.ENTER)
time.sleep(1)
#click on the Accept terms button
# identify image
images = driver.find_elements_by_tag_name('img')
for image in images:
    print(image.get_attribute('src'))

driver.find_element_by_xpath("//a[@href='/lh/lottery-game/lotto-6aus49']").send_keys(Keys.ENTER)
time.sleep(10)



#identify the Google search text box and enter the value
driver.find_element_by_xpath('//*[@id="mainScroll"]/div/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/button[2]').send_keys(Keys.ENTER)
time.sleep(3)
#identify the Google search text box and enter the value
driver.find_element_by_xpath('//*[@id="mainScroll"]/div/div[2]/div/div/div[2]/div/div[5]/div[3]/div/div/div[4]/button').send_keys(Keys.ENTER)
time.sleep(3)
#close the browser
driver.close()
print("sample test case successfully completed")

