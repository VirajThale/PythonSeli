from selenium.webdriver.common.by import By


class Login:
    button_login_ClassName = 'login'
    textbox_email_name = 'user_login'
    textbox_password_xpath = "//input[@name='user_pwd']"
    button_login_xpath = "//input[@name='btn_login']"
    warning_text_xpath = "//*[@id='msg_box']"

    username = "asb@gamil.com"
    Password = "Asbc@123456"
    BaseURL = "https://www.simplilearn.com"

    def __init__(self, driver):
        self.driver = driver

    def UserName(self):
        self.driver.get(self.BaseURL)
        self.driver.find_element(By.CLASS_NAME, self.button_login_ClassName).click()
        self.driver.find_element(By.NAME, self.textbox_email_name).send_keys(self.username)

    def User_Password(self):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(self.Password)

    def LoginButton(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def AssertCheck(self):
        # print(self.driver.find_element(By.XPATH, self.warning_text_xpath).text)
        return self.driver.find_element(By.XPATH, self.warning_text_xpath).text
        # return msg
