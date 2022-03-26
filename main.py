import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('Users\Денис\PycharmProjects\PythonTutorial\chromedriver.exe')
driver.get('http://130.193.37.179/app/pets')
(driver.find_elements(By.XPATH,'//*[@id="image"]/img'))[0].click()
time.sleep(4)
driver.quit()