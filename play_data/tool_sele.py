"""
Selenium을 이용하여 웹 크롤링을 할 때 사용하는 도구들 총 정리
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as BS

# Create Chrome
def chrome_init(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver

# Click button on Chrome web page
def click(driver,selector):
    driver.find_element(By.CSS_SELECTOR, selector).click()
    return

# Get current page HTML
def get_html(driver):
    return(BS(driver.page_source))

