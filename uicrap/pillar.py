from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://developer.mozilla.org')


logo_locator = By.CSS_SELECTOR, 'a.logo'
logo = driver.find_element(*logo_locator)
#logo = driver.find_element_by_css_selector('header#main-header div.center a.logo')
#driver.find_element_by_class_name('logo')
header = driver.find_element_by_id('main-header')
search = driver.find_element_by_class_name('q')




print(logo)
print(logo.text)

#import ipdb; ipdb.set_trace()

#sss = driver.find_element_by_id('home-q')
# ss1 = By.ID, 'home-q'
# sss = driver.find_element(*ss1)
#
# sss.send_keys('test')
#
# sss.send_keys(Keys.ENTER)

driver.quit()
