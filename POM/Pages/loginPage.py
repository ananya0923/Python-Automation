from POM.Locators.locators import Locators
class LoginPage():
    def __init__(self,driver):
        self.driver=driver
        self.un_xpath=Locators.un_xpath
        self.pass_xpath="//input[@name='password']"
        self.loginbutton_xpath="//button[@type='submit']"
        self.invalid_un_xpath="//p[text()='Invalid credentials']"
    def enter_un(self,username):
        self.driver.find_element(Locators.un_xpath).clear()
        self.driver.find_element(Locators.un_xpath).send_keys(username)
    def enter_pass(self,password):
        self.driver.find_element(self.un_xpath).clear()
        self.driver.find_element(self.pass_xpath).send_keys(password)
    def loginbtn(self):
        self.driver.find_element(self.loginbutton_xpath).click()

    def check_invalidun_msg(self):
        msg = self.driver.find_element(self.invalid_un_xpath).text
        return msg

