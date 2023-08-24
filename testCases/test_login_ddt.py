import time

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_login:
    baseurl=Readconfig.getApplictaionURL()
    path=".//TestData//test_data.xlsx"
    logger=LogGen.loggen()


    def test_login_ddt(self, setup_driver):
        self.logger.info('***** Test_002_DDT_login****')
        self.logger.info("***********verifying login test**************")
        self.driver = setup_driver
        self.driver.get(self.baseurl)
        # self.driver.maximize_window()
        self.login=LoginPage(self.driver)

        self.rows=XLUtils.getRowCount(self.path,"Sheet1") ### path of xl file and sheet name
        print("no of rows in exel:",self.rows)
        list_status = []

        for r in range(2,self.rows):
            self.user_name=XLUtils.readData(self.path,"Sheet1",r,1)
            self.pass_word = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp_result = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.driver.implicitly_wait(10)
            self.login.setusername(self.user_name)
            self.login.setpassword(self.pass_word)
            self.login.clicklogin()
            time.sleep(5)
            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
               if self.exp_result=='pass':
                  self.logger.info("*****Passed*****")
                  self.login.logout()
                  list_status.append('Passed')
               elif self.exp_result=='fail':
                    self.logger.info("****** failed****")
                    self.login.logout()
                    list_status.append('fail')

            elif act_title!=exp_title:
                 if self.exp_result=="pass":
                    self.logger.info('*** failed***')
                    list_status.append('fail')
                 elif self.exp_result=='fail':
                     self.logger.info("*** passed***")
                     list_status.append('pass')
            print(list_status)

        if 'fail' not in list_status:
            self.logger.info("**** login ddt test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.info("****** login ddt test failed ****")
            self.driver.close()
            assert False

        self.logger.info('**** end of login ddet test******')
        self.logger.info("****** completed login ddt test002****")