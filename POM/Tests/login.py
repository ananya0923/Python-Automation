import time
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import title_is
# from selenium.webdriver.support.select
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import HtmlTestRunner
from POM.Pages.loginPage import LoginPage
from POM.Pages.homePage import HomePage
class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver= webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    def test_01_login_valid(self):
        driver=self.driver
        driver.get(r"https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(2)
        # login = LoginPage(driver)
        # login.enter_un("Admin")
        # login.enter_pass("admin123")
        # login.loginbtn()
    def test_02_login_invalid(self):
        driver = self.driver
        driver.get(r"https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(2)
        msg = driver.find_element('xpath',"").text
        self.assertEquals(msg,"Invalid credentials")
        # home= HomePage(driver)
        # home.click_logot()
        # self.driver.find_element('xpath',"//input[@name='username']").send_keys('Admin')
        # self.driver.find_element('xpath',"//input[@name='password']").send_keys('admin123')
        # self.driver.find_element('xpath',"//button[@type='submit']").click()
        time.sleep(2)
        # self.driver.find_element('xpath',"//ul[@class='oxd-dropdown-menu']/li[4]/a").click()
    @classmethod
    def tearDownClass(cls):
        # cls.driver.find_element('xpath',"//p[text()='Fake Admin']").click()
        # cls.driver.find_element('xpath',"//a[text()='Logout']").click()
        cls.driver.close()
        cls.driver.quit()
        print('Test completed')
if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/USER/PycharmProjects/SeleniumPythonProject/reports'))
