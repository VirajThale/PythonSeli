from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.simplilearn.com/')  # get link fo driver
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.CLASS_NAME, 'login').click()
driver.find_element(By.NAME, 'user_login').send_keys("vthale@gmail.com")
password = driver.find_element(By.XPATH, "//input[@name='user_pwd']")
password.send_keys("1234567890@Real")
bttn_login = driver.find_element(By.XPATH, "//input[@name='btn_login']")
bttn_login.click()

try:
    msg = driver.find_element(By.XPATH, "//*[@id='msg_box']").text
    assert "The email or password you have entered is invalid." in msg
except AssertionError:
    print("Assertion Error")
else:
    print("Assertion Clear:Test Passed")

# print(driver.find_element(By.XPATH, "//*[@id='msg_box']").text)

# msg = driver.find_element(By.XPATH, "//*[@id='msg_box']").text  # XPATH
# print(msg)
# print(driver.find_element(By.CSS_SELECTOR, "div#msg_box").get_attribute("innerHTML"))  # CSS SELECTOR
# l = driver.find_element(By.CSS_SELECTOR, "div#msg_box").get_attribute("innerHTML")
# print(l)

driver.close()
