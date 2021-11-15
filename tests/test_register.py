import configparser
from register import Register

def test_registration():
    config = configparser.RawConfigParser()
    config.read('..\config.properties')
    link = config.get('UrlSection', 'url.link')
    bit8_link = config.get('UrlSection', 'url.bit8_link')
    bit8_user = config.get('CredentialSection', 'credential.bit8_user')
    bit8_password = config.get('CredentialSection', 'credential.bit8_password')

    setup = Register()

    # initial setup, open browser, close cookies etc.
    setup.setUp(link)
    driver = setup.driver
    # Find and press login button
    setup.register_process()
    #assert True
    # screenshot
    # driver.save_screenshot("ss.png")
    # screenshot = Image.open("ss.png")
    # screenshot.show()


    # bit8 Clear user just created
    # bit8 login
    setup.bit8SetUp(bit8_link)
    # change the name for bit8
    setup.bit8_change_name(bit8_user, bit8_password)
    assert True
