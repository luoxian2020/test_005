from Page.login_page import Login_Page
from Page.setting_page import Setting_Page

class Page:

    def __init__(self,driver):
        self.driver = driver

    def get_login_page(self):
        return Login_Page(self.driver)

    def setting_page(self):
        return Setting_Page(self.driver)

