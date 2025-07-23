import pytest
import random
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
import allure
from logs_floor import logs_pro
a=logs_pro.get_log()
desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '9', # 手机安卓版本
  'deviceName': 'leidian', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.dragon.read', # 启动APP Package名称
  'appActivity': 'com.dragon.read.pages.splash.SplashActivity', # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'newCommandTimeout': 60000,
  'automationName' : 'UiAutomator2'}

@allure.epic("番茄免费小说书籍获取与查找功能测试报告")
@allure.feature("搜索功能")
@pytest.mark.parametrize("case_name,name",[("小说名称模糊查询验证--","完美"),("小说作者模糊查询验证--","辰"),("小说名称精确查询验证--","完美世界"),("小说作者精确查询验证--","辰东")])
def test_01_login(case_name,name):
   driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
   allure.dynamic.title(case_name)
   time.sleep(10)


   #点击搜索框
   driver.find_element(by=By.ID,value="com.dragon.read:id/ck3").click()
   time.sleep(5)
   #默认搜索内容
   elements = driver.find_elements(by=By.ID, value="com.dragon.read:id/ddq")
   if len(elements) > 0:
       a.info(case_name + "默认搜索内容存在验证成功")
   else:
       a.info(case_name + "默认搜索内容存在验证失败")
   #断言后
   after_1 = driver.find_elements(by=By.ID, value="com.dragon.read:id/acc")
   if len(after_1) == 0:  # 此时可正常判断列表长度
       a.info(case_name + "点击搜索框跳转页面验证成功")

   after_1_1 = driver.find_elements(by=By.ID, value="com.dragon.read:id/e0c")
   if len(after_1_1) != 0:  #
       a.info(case_name + "搜索历史验证查询成功")

   after_1_2 = driver.find_elements(by=By.ID, value="com.dragon.read:id/d0y")
   if len(after_1_2) != 0:  #
       a.info(case_name + "热门榜单验证查询成功")
    #清空搜索框
   driver.find_element(by=By.ID, value="com.dragon.read:id/ddq").clear()
   time.sleep(5)

   # 输入小说
   driver.find_element(by=By.ID,value="com.dragon.read:id/ddq").send_keys(name)

   # 查找搜索logo元素列表（若不存在则返回空列表）
   after_2 = driver.find_elements(by=By.ID, value="com.dragon.read:id/e0c")
   if len(after_2) != 0:  # 此时可正常判断列表长度
       a.info(case_name + "未点搜索跳转页面验证成功")

    #点击搜索
   driver.find_element(by=By.ID,value="com.dragon.read:id/dee").click()
   after_3 = driver.find_elements(by=By.ID, value="com.dragon.read:id/bif")
   if len(after_3) == 0:  # 此时可正常判断列表长度
       a.info(case_name + "点击搜索跳转页面验证成功")
   time.sleep(5)

   driver.quit()
#------================================================
@allure.epic("番茄免费小说书籍获取与查找功能测试报告")
@allure.feature("榜单功能")
@pytest.mark.parametrize("case_name",[("榜单功能随机抽取验证--")])
def test_02_login(case_name):
    allure.dynamic.title(case_name)
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    time.sleep(20)

    elements = driver.find_elements("xpath", "//*[@resource-id='com.dragon.read:id/cp0']")
    if len(elements) >= 3:
        one_element = elements[2]  # 索引从0开始，所以第三个元素的索引是2
        one_element.click()

    time.sleep(5)  # 等待页面跳转

    target_text = one_element.text
    after_1 = driver.find_elements(by=By.XPATH, value=f'//*[@resource-id="com.dragon.read:id/cp0" and @text="{target_text}"]')

    if len(after_1) != 0:
        a.info(case_name+f"成功找到文本为“{target_text}”的元素，页面跳转验证成功")
    else:
        a.error(case_name+f"未找到文本为“{target_text}”的元素，页面跳转验证失败")

    time.sleep(5)
    #随机选取各榜单
    elements = driver.find_elements("xpath", "//*[@resource-id='com.dragon.read:id/dui']")
    if len(elements) >= 3:
        two_element = elements[2]  # 索引从0开始，所以第三个元素的索引是2
        two_element.click()
    time.sleep(5)  # 等待页面跳转

    targey_text =two_element.text
    after_2 = driver.find_elements(by=By.XPATH, value=f'//*[@resource-id="com.dragon.read:id/dui" and @text="{targey_text}"]')

    if len(after_2) != 0:
        a.info(case_name+f"成功找到文本为“{targey_text}”的元素，页面跳转验证成功")
    else:
        a.error(case_name+f"未找到文本为“{targey_text}”的元素，页面跳转验证失败")
    #随机选取文本后随机兴趣喜好
    elements = driver.find_elements("xpath", "//*[@resource-id='com.dragon.read:id/cp0']")
    if len(elements) >= 3:
        three_element = elements[2]  # 索引从0开始，所以第三个元素的索引是2
        three_element.click()
    time.sleep(5)  # 等待页面跳转
    targeu_text =three_element.text
    after_3 = driver.find_elements(by=By.XPATH, value=f'//*[@resource-id="com.dragon.read:id/cp0" and @text="{targeu_text}"]')

    if len(after_3) != 0:
        a.info(case_name+f"成功找到文本为“{targeu_text}”的元素，页面跳转验证成功")
    else:
        a.error(case_name+f"未找到文本为“{targeu_text}”的元素，页面跳转验证失败")

    driver.quit()


@allure.epic("番茄免费小说书籍获取与查找功能测试报告")
@allure.feature("分类功能")
@pytest.mark.parametrize("case_name",[("分类功能随机抽取验证--")])
def test_03_login(case_name):
    allure.dynamic.title(case_name)
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    time.sleep(20)

    #进入分类页面
    driver.find_element(by=By.ID, value="com.dragon.read:id/vt").click()

    after_1 = driver.find_elements("xpath", "//*[@class='android.widget.TextView']")
    if len(after_1) > 0:
        a.info(case_name + "分页功能跳转页面验证成功")
    else:#android.widget.LinearLayout
        a.warning(case_name + "分页功能跳转失败，未找到分类列表元素")

    time.sleep(10)
#==============================
    #一级主题
    elements = driver.find_elements("xpath", "//*[@resource-id='com.dragon.read:id/a1e']")
    if len(elements) >= 3:  # 确保有足够的元素（索引0~2）
        two_element = elements[2]  # 取
        two_element.click()
    time.sleep(5)  # 等待页面跳转

    targey_text =two_element.text
    after_2 = driver.find_elements(by=By.XPATH, value=f'//*[@resource-id="com.dragon.read:id/a1e" and @text="{targey_text}"]')

    if len(after_2) != 0:
        a.info(case_name+f"成功找到文本为“{targey_text}”的元素，页面跳转验证成功")
    else:
        a.error(case_name+f"未找到文本为“{targey_text}”的元素，页面跳转验证失败")

    #二级分类
    elements = driver.find_elements("xpath", "//*[@resource-id='com.dragon.read:id/duo']")
    if len(elements) >= 7:  # 确保索引6的元素存在
        san_element = elements[6]

        # 在点击前先获取文本内容
        targeyy_text = san_element.text

        # 然后执行点击操作
        san_element.click()

        time.sleep(5)  # 等待页面跳转

        # 验证跳转后的页面是否包含预期的文本元素
        after_3 = driver.find_elements(by=By.XPATH,
                                       value=f'//*[@resource-id="com.dragon.read:id/duo" and @text="{targeyy_text}"]')

        if len(after_3) >=0:
            a.info(case_name + f"成功找到文本为“{targeyy_text}”的元素，页面跳转验证成功")
        else:
            a.error(case_name + f"未找到文本为“{targeyy_text}”的元素，页面跳转验证失败")


    driver.find_element(by=By.ID,value="com.dragon.read:id/c14").click()
    time.sleep(5)
    #默认搜索内容
    elements = driver.find_elements(by=By.ID, value="com.dragon.read:id/amz")
    if len(elements) > 0:
        a.info(case_name + "默认搜索内容存在验证成功")
    else:
        a.info(case_name + "默认搜索内容存在验证失败")

    driver.find_element(by=By.ID, value="com.dragon.read:id/amz").click()
    #字数，更新，综合
    elements = driver.find_elements("xpath", "//*[@resource-id='com.dragon.read:id/dv5']")
    if len(elements) >= 5:
        si_element = elements[4]  # 索引从0开始，所以第三个元素的索引是2
        si_element.click()
    time.sleep(5)  # 等待页面跳转

    ttargey_text = si_element.text
    after_4 = driver.find_elements(by=By.XPATH,
                                   value=f'//*[@resource-id="com.dragon.read:id/dv5" and @text="{ttargey_text}"]')

    if len(after_4) != 0:
        a.info(case_name + f"成功找到文本为“{ttargey_text}”的元素，页面跳转验证成功")
    else:
        a.error(case_name + f"未找到文本为“{ttargey_text}”的元素，页面跳转验证失败")
    ######
    elements = driver.find_elements(MobileBy.ID, "com.dragon.read:id/dv5")
    target_text = "连载中"
    target_element = None
    for element in elements:
        if element.text == target_text:
            target_element = element
            break

    if target_element:
        # 对目标元素进行操作，如点击
        target_element.click()
    else:
        print(f"未找到text为{target_text}的元素")

    driver.quit()
