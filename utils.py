from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from constants import PAUSE_DURATION_SECONDS_SELENIUM, URL


def get_copout():
    service = Service(executable_path=ChromeDriverManager().install())
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(URL)
    driver.maximize_window()
    sleep(PAUSE_DURATION_SECONDS_SELENIUM)

    press_button = driver.find_element(By.LINK_TEXT, 'Сгенерировать отмазку')

    press_button.click()

    sleep(PAUSE_DURATION_SECONDS_SELENIUM)

    copout_text = driver.find_element(By.CLASS_NAME, 'wrap-excuse__middle')

    return copout_text.text
