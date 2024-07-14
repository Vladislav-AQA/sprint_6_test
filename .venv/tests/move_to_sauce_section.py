from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver

driver = webdriver.Chrome()
driver.get('https://stellarburgers.nomoreparties.site/')

driver.find_element(By.TAG_NAME, ".//span[text()='Соусы']").click()
element = driver.find_element(By.XPATH, ".//div/h2[text()='Соусы']")
driver.execute_script("arguments[0].scrollIntoView();", element)
assert 'Соусы' in element.text

deriver.quit()