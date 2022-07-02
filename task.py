from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
link ="https://demoqa.com/"
browser = webdriver.Chrome()
browser.get(link)
browser.execute_script ("window.scrollTo(0, 450)")
elementt = browser.find_element (By.CSS_SELECTOR, "#app > div > div > div.home-body > div > div:nth-child(1) > div > div.avatar.mx-auto.white > svg > path").click()
checkboxx = browser.find_element (By.CSS_SELECTOR, "#item-1 > span").click()
check = browser.find_element (By.CSS_SELECTOR, "#tree-node > ol > li > span > label > span.rct-checkbox > svg").click()
radiobuttonn = browser.find_element (By.CSS_SELECTOR, "#item-2 > span").click()
impressive = browser.find_element (By.CSS_SELECTOR, "#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(2) > div:nth-child(3) > label").click()
yesradio = browser.find_element (By.CSS_SELECTOR, "#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(2) > div:nth-child(2) > label").click()