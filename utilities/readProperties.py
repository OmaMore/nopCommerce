import configparser

config=configparser.RawConfigParser()
config.read(".\\Confugurations\\config.ini")

class Readconfig:
    @staticmethod
    def getApplictaionURL():
        url=config.get('common info','baseurl')
        return url

    @staticmethod
    def getUseremail():
        useremail=config.get('common info','username')
        return useremail

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password