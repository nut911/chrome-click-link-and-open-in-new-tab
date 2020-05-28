from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# open browser to url
browser = webdriver.Chrome()
browser.get('http://ipv4.download.thinkbroadband.com')

elem = browser.find_element_by_xpath("//span[@class='title' and text()='Broadband Speed Test']")
webdriver.ActionChains(browser).key_down(Keys.CONTROL).click(elem).key_up(Keys.CONTROL).perform()

time.sleep(10)

# close selenium session
browser.close()
