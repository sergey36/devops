from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window();
driver.get("https://sandbox.grow.link/6f340bc4d18a0bcb559914d970ac2870-MTE4NjI")

message=driver.find_element(By.ID,"message").text
assert "עבר בהצלחה"


error_message=driver.find_element(By.ID,"error").text
assert "לא תקין"
