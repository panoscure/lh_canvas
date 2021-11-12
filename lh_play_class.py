from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver.common.action_chains import ActionChains




class web_play:

    def play(self, driver,game_xpath):
        print("Game: ",game_xpath)

        time.sleep(1)
        #click on the game lotto 6aus49
        driver.find_element_by_xpath(game_xpath).send_keys(Keys.ENTER)
        time.sleep(20)
        try:
            #Select System
            #driver.find_element_by_link_text("System").send_keys(Keys.ENTER)
            #time.sleep(3)
            system = WebDriverWait(driver, 8).until(
                EC.element_to_be_clickable((By.LINK_TEXT, 'System')))
            system.send_keys(Keys.ENTER)
        except:
            print("no system option exists")

        try:
            #quick pick
            #driver.find_element_by_xpath('//*[@id="mainScroll"]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/i').click()
            time.sleep(3)
            qp = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="mainScroll"]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/i')))
            qp.click()
        except:
            print("no quick pick option exist")

        #play button
        #play_button = WebDriverWait(driver, 10).until(
        #    EC.element_to_be_clickable((By.XPATH, '//*[@id="mainScroll"]/div/div[2]/div/div/div[2]/div/div[5]/div[3]/div/div/div[4]/button')))
        try:
            play_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Play Now"]')))
        except:
            play_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Play Bingo"]')))

        time.sleep(3)
        play_button.send_keys(Keys.ENTER)
        #Select sepa Consent
        try:
            sepa_consent = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#confirmDialog > div > div.modal-body > div > div > div.confirm-result-footer > div > div > label")))
            sepa_consent.click()
        except:
            print("sepa consent is already checked")

        #select play selections
        time.sleep(3)
        play_selections = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#confirmDialog > div > div.modal-footer > button.btn.btn-success"))
        )
        play_selections.send_keys(Keys.ENTER)

        #sms verification verify
        time.sleep(3)
        verify_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#extraPinDialog > div > div > div.modal-content-body > div > div > div > div > div:nth-child(3) > div.button-container > div:nth-child(2) > button"))
        )
        verify_button.send_keys(Keys.ENTER)

        #find "your predictions have been placed" to verify play
        time.sleep(3)

        try:
            verify_play = WebDriverWait(driver, 8).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#playResult > div > div.modal-body > div.modal-content-body > div > div.play-result > div.message.font-large")))
            print("play was successfull")

        except:
            print("play is not successfull")

        ok_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="playResult"]/div/div[2]/button')))
        time.sleep(4)
        ok_button.send_keys(Keys.ENTER)






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
