from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver

driver = webdriver.Chrome()
driver.get('https://stellarburgers.nomoreparties.site/')

driver.find_element(By.TAG_NAME, ".//span[text()='Начинки']").click()
element = driver.find_element(By.XPATH, ".//div/h2[text()='Начинки']")
driver.execute_script("arguments[0].scrollIntoView();", element)
assert 'Начинки' in element.text

deriver.quit()