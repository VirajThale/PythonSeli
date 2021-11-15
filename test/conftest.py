import pytest
import pdb
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver



def setup():

    driver_location = "C://Users//vthale//PycharmProjects//PythonSeli//chromedriver.exe"
    baseURL = "https://www.simplilearn.com"
    driver: WebDriver = webdriver.Chrome(executable_path=driver_location)
    driver.get(baseURL)
    driver.maximize_window()
    driver.implicitly_wait(10)
    print("Launching WebDriver for Chrome...")
    return driver
