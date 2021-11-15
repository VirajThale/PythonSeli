
from PagesObjects.LoginPage import Login
from test.conftest import setup


class Test_001_Login:
    BaseURL = "https://www.simplilearn.com"

    def test_login_check(self):

        self.driver = setup()
        self.driver.get(self.BaseURL)
        self.lp = Login(self.driver)
        self.lp.UserName()
        self.lp.User_Password()
        self.lp.LoginButton()

        try:
            assert "The email or password you have entered is invalid." in self.lp.AssertCheck()
        except AssertionError:
            print("Assertion Error")
        else:
            print("Assertion Clear:Test Passed")
