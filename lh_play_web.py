from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import re
from lh_login import login_logout
from lh_play_class import web_play
from lh_xls_class import lh_xls
import configparser


def play_web():
    #xls = lh_xls()
    #link = xls.get_link()
    #username = xls.get_username()
    #password = xls.get_password()

    config = configparser.RawConfigParser()
    config.read('config.properties')

    print (config.get('CredentialSection', 'credential.username'))
    print (config.get('CredentialSection', 'credential.password'))
    username= config.get('CredentialSection', 'credential.username')
    password= config.get('CredentialSection', 'credential.password')

    setup = login_logout()
    #initial setup, open browser, close cookies etc.
    setup.setUp()
    driver = setup.driver
    #Find and press login button
    setup.login(username,password)
    #verify login
    setup.verify_login()




    #Perform the play
    play = web_play()

    #play lotto
    game_xpath = "//a[@href='/lh/lottery-game/lotto-6aus49']"
    play.play(driver,game_xpath)

    #play eurojackpot
    game_xpath = "//a[@href='/lh/lottery-game/eurojackpot']"
    play.play(driver,game_xpath)

    #play Toto
    game_xpath = "//a[@href='/lh/lottery-game/toto-6aus45']"
    play.play(driver,game_xpath)

    #play glucksspirale
    game_xpath = "//a[@href='/lh/lottery-game/glucksspirale']"
    play.play(driver,game_xpath)

    #play Keno
    game_xpath = "//a[@href='/lh/lottery-game/keno']"
    play.play(driver,game_xpath)

    #play Bingo
    game_xpath = "//a[@href='/lh/lottery-game/bingo']"
    play.play(driver,game_xpath)

#press logout
#setup.logout()
#verify if logout is successfull
#setup.verify_logout()

#close the browser
#driver.close()
    print("sample test case successfully completed")

#play_web()
