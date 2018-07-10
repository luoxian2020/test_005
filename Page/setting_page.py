from Base.Base import Base1
import Page,allure

class Setting_Page(Base1):

    def __int__(self,driver):
        Base1.__init__(self,driver)


    @allure.step(title='点击安全退出')
    def safe_logout(self):
        # 点击 安全退出
        self.click_ele(Page.logout_btn_id)