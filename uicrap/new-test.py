from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get('https://developer.mozilla.org')


ss1 = By.ID, 'home-q'
sss = driver.find_element(*ss1)

sss.send_keys('test')

sss.send_keys(Keys.ENTER)
