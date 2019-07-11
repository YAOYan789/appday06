import allure
import pytest


class Test01():
    @allure.step(title="测试登录操作")
    def test001(self):
        print("test001被执行")

    @allure.step(title="测试退出")
    def test002(self):
        print("test002被执行")

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test003(self):
        allure.attach("描述：", "test003正在被打印")
        print("test003正在被执行")

    def test004(self):
        with open("./image/fail.png", "rb")as f:
            # 参数：（描述：文件流，图片类型）
            allure.attach("失败原因：", f.read(), allure.attach_type.png)
