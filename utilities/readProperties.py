import configparser

class ReadConfig:
    def __init__(self):
        self.config=configparser.RawConfigParser()
        self.config.read("C:\\Users\\amuly\\PycharmProjects1\\SeleniumPythonFramework\\Configurations\\config.ini")

    def getApplicationURL(self):
        ui_url=self.config.get('common info', 'baseURL')
        return ui_url

    def getAPIURL(self):
        api_url=self.config.get('common info', 'apiURL')
        return api_url

    def getinputPath(self):
        input_path=self.config.get('common info', 'path')
        return input_path

    def getoutputPath(self):
        outputpath = self.config.get('common info', 'output_path')
        return outputpath

    def getregister_firstname(self):
        reg_firstname=self.config.get('common info', 'register_firstname')
        return reg_firstname

    def getregister_lastname(self):
        reg_lastname=self.config.get('common info', 'register_lastname')
        return reg_lastname

    def getregister_email(self):
        reg_email=self.config.get('common info', 'register_email')
        return reg_email

    def getregister_phone(self):
        reg_phone=self.config.get('common info', 'register_phone')
        return reg_phone

    def getregister_password(self):
        reg_password=self.config.get('common info', 'register_password')
        return reg_password

    def getregister_confirm_password(self):
        reg_confirm_password=self.config.get('common info', 'register_confirm_password')
        return reg_confirm_password

    def getUserID(self):
        get_user_id=self.config.get('common info', 'user_id')
        return get_user_id



