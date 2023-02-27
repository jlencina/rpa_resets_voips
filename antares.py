import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def antares():
    driver = webdriver.Chrome()
    driver.get("http://10.1.42.15")
    time.sleep(1)

    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("Racional123")
    driver.find_element(By.CLASS_NAME, "login-btn").click()

    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='main']/div[2]/div/div[1]/div[2]/div[2]/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='maintainUpgrade']/div/div[2]/span[1]/button").click()
    time.sleep(2)
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "layui-layer4")))
    driver.find_element(By.XPATH, "//*[@id='layui-layer4']/div[3]/a[1]").click()
    time.sleep(3)

antares()
