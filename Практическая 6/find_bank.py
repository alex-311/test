from    selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
s=Service('C:/Users/User/Downloads/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")
driver.set_window_size(1366, 768)
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.ID, "login-otp-button").click()
driver.find_element(By.ID, "payments-form").click()
driver.find_element(By.CSS_SELECTOR, "#dashboard-favorites > ul > li:nth-child(1) > div.favorite.vendor > a").click()
time.sleep(3)
driver.find_element(By.NAME, "payment.amount").send_keys("5")
driver.find_element(By.ID, "forward").click()
time.sleep(5)