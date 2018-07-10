
import allure
class Test_Screen:

    def get_screen_01(self):

        with open('./screen/test.png','rb') as f:
            allure.attach('截图名字',f.read(),allure.attach_type.PNG)

    def test_01(self):
        allure.attach('描述','描述内容')
        assert 0, self.get_screen_01()
