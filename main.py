import time

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.actions.interaction import KEY
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('Users\Денис\PycharmProjects\PythonTutorial\chromedriver.exe')
driver.get('https://google.com/')
driver.find_element(By.XPATH,'//*[@title=\'Поиск\']').send_keys('ютубчик' + Keys.RETURN)

driver.save_screenshot('goog.png')

time.sleep(3)

driver.quit()