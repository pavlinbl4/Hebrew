# pip install webdriver-manager
from datetime import datetime
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import FirefoxOptions

from selenium.webdriver.common.by import By

# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time




# def setting_chrome_options():
#     chrome_options = Options()
#     # chrome_options.add_argument("--headless")  # фоновый режим
#     chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # невидимость автоматизации
#     chrome_options.add_argument(
#         "user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
#     chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
#     chrome_options.add_experimental_option("detach", True)
#     return chrome_options





def open_page(page_link):
    # service = Service(ChromeDriverManager().install())
    service = Service(GeckoDriverManager().install())
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(service=service, options=options)
    # driver = webdriver.Chrome(service=service, options=setting_chrome_options())
    driver.get(page_link)
    # browser.get_screenshot_as_png('png_test')
    driver.save_screenshot(f'screen_short_{datetime.today()}.png')


# def sens_word_to_translate(word_to_translate):
#     browser.find_element(By.CSS_SELECTOR, '#word').send_keys(word_to_translate)
#     browser.find_element(By.CSS_SELECTOR, '#word').send_keys(Keys.ENTER)
#     time.sleep(3)
#     # translation = browser.find_element(By.CLASS_NAME,"cycle1").screenshot('test2.png')
#     translation = browser.find_element(By.CLASS_NAME, "cycle1").text
#
#     print(translation.split('\n'))
#     print(translation.split('\n')[2])
#     return translation.split('\n')


# browser = webdriver.Chrome(options=setting_chrome_options())

if __name__ == '__main__':
    # page_link = 'https://www.slovar.co.il/'
    page_link = 'https://korni.co.il/slovar_ivrit_russkii/'
    open_page(page_link)
    # sens_word_to_translate('relay')
    # end_selenium()
