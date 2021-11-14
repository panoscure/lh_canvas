from lh_login import login_logout
from lh_play_class import web_play
import configparser

def test_play_web():
    config = configparser.RawConfigParser()
    config.read('..\config.properties')
    username= config.get('CredentialSection', 'credential.username')
    password= config.get('CredentialSection', 'credential.password')
    print (config.get('CredentialSection', 'credential.username'))
    print (config.get('CredentialSection', 'credential.password'))

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
    play.play(driver, game_xpath)

    #play eurojackpot
    game_xpath = "//a[@href='/lh/lottery-game/eurojackpot']"
    play.play(driver, game_xpath)

    #play Toto
    game_xpath = "//a[@href='/lh/lottery-game/toto-6aus45']"
    play.play(driver, game_xpath)

    #play glucksspirale
    game_xpath = "//a[@href='/lh/lottery-game/glucksspirale']"
    play.play(driver,game_xpath)

    #play Keno
    game_xpath = "//a[@href='/lh/lottery-game/keno']"
    play.play(driver,game_xpath)

    #play Bingo
    game_xpath = "//a[@href='/lh/lottery-game/bingo']"
    play.play(driver,game_xpath)