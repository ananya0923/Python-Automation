class HomePage():
    def __init__(self,driver):
        self.driver=driver
        self.logout_link="//button[@type='submit']"
    def click_logot(self):
        self.driver.find_element(self.logout_link).click()