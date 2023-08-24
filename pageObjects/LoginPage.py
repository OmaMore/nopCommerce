from selenium.webdriver.common.by import By


class LoginPage():
    textbox_username_id='Email'
    textbox_password_id="Password"
    login_button_xpath="//button[normalize-space()='Log in']"
    link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver=driver

    def setusername(self,username):
     self.driver.find_element('id', self.textbox_username_id).clear()
     self.driver.find_element('id', self.textbox_username_id).send_keys(username)
    def setpassword(self,password):
     self.driver.find_element('id', self.textbox_password_id).clear()
     self.driver.find_element('id', self.textbox_password_id).send_keys(password)
    def clicklogin(self):
     self.driver.find_element("xpath", self.login_button_xpath).click()
     # self.driver.find_element(By.XPATH(self.login_button_xpath)).click()
    def logout(self):
     self.driver.find_element('linktext', self.link_logout_linktext).click()












