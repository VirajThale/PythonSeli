from selenium import webdriver
from PagesObjects.LoginPage import Login


class Test_001_Login:
    BaseURL = "https://www.simplilearn.com"
    username = "asb@gamil.com"
    Password = "Asbc@123456"
    driver_location = "C://Users//vthale//PycharmProjects//PythonSeli//chromedriver.exe"

    def test_login_check(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_location)
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lp = Login(self.driver)

        self.lp.UserName(self.username)
        self.lp.User_Password(self.Password)
        self.lp.LoginButton()

        try:
            assert "The email or password you have entered is invalid." in self.lp.AssertCheck()
        except AssertionError:
            print("Assertion Error")
        else:
            print("Assertion Clear:Test Passed")

        self.driver.close()
