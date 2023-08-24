from selenium import webdriver
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen


class Test_001_login:
    baseurl=Readconfig.getApplictaionURL()
    username=Readconfig.getUseremail()
    password=Readconfig.getPassword()
    logger=LogGen.loggen()


    def test_homepageTitle(self, setup_driver):
        self.logger.info('***** test_homePgae****')
        self.driver=setup_driver
        self.driver.get(self.baseurl)
        act_title=self.driver.title
        # self.driver.close() ## invalid session id
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************* homepge title test is passed***********")
        else:
            self.driver.save_screenshot(".//Screenshots"+"test_homepageTitle.png")
            assert False
            self.driver.close()
            self.logger.error("************ home page title is failed**********")


    def test_login(self, setup_driver):
        self.logger.info('***** test_login****')
        self.driver = setup_driver
        self.driver.get(self.baseurl)
        self.login=LoginPage(self.driver)
        self.login.setusername(self.username)
        self.login.setpassword(self.password)
        self.login.clicklogin()
        act_title=self.driver.title
        # self.driver.close()

        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("************* homepge title test is passed***********")
        else:
            self.driver.save_screenshot(".//Screenshots"+"test_login.png")
            assert False
            self.driver.close()
            self.logger.error("************ home page title is failed**********")






