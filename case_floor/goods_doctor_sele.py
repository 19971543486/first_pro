from setting_floor import sele_setting
import time
from selenium.webdriver.common.by import By
import pytest
import random
import allure;
from logs_floor import logs_pro;
a=logs_pro.get_log()

from selenium.webdriver.support.select import Select

llq = sele_setting.get_browser("edge")

@allure.epic("医药管理系统接口测试报告")
@allure.feature("登录模块")
@pytest.mark.parametrize("uname,upwd,title,result",[("admn","admin23","登录医药管理系统","失败-用户名失败"),("admin","1234","登录医药管理系统","失败-密码错误"),
                                             ("adminss","admin123","登录医药管理系统","失败-组合错误"),("admin","admin123","管理系统","成功"),])
def test_01_login(uname,upwd,title,result):
    allure.dynamic.title(result)
    llq.get("http://127.0.0.1:8008")

    time.sleep(3)
    a.debug("清空用户名输入框")
    llq.find_element(by=By.NAME, value="username").clear()
    time.sleep(3)
    a.debug("输入用户名")
    llq.find_element(by=By.NAME, value="username").send_keys(uname)
    time.sleep(3)

    a.debug("清空密码")
    llq.find_element(by=By.NAME, value="password").clear()
    time.sleep(3)
    a.debug("输入密码")
    llq.find_element(by=By.NAME, value="password").send_keys(upwd)
    time.sleep(3)
    llq.find_element(by=By.ID, value="btnSubmit").click()
    time.sleep(3)


    if result == "成功":
        a.error(f"登录测试成功  用户名: {uname}, 密码: ****")
        assert title == llq.title


    elif "用户名错误" in result:
        # 用户名错误场景
        a.error(f"登录测试失败（用户名错误）- 输入用户名: {uname}")


    elif "密码错误" in result:
        # 密码错误场景
        a.error(f"登录测试失败（密码错误）- 输入密码: ****")


    else:
        # 组合错误场景
        a.error(f"登录测试失败（组合错误）- 输入: {uname}/{upwd}")

@allure.epic("医药管理系统接口测试报告")
@allure.feature("管理模块")
@allure.story('药品——添加')
@pytest.mark.parametrize(
    "case_name,product_Name,select,stock_Num,int_Price,outPrice",  # 与测试数据列数保持一致
    [
        ("药品名称非空验证","", "2", "100", "80", "100"),
        ("供应商非空验证","阿莫西林", "", "100", "30", "100"),
        ("全空验证","", "", "", "", ""),
        ("正确输入验证","阿莫西林", "2", "100", "80", "100"),
    ]
)
def test_medicine(case_name,product_Name, select, stock_Num, int_Price, outPrice):  # 移除未使用的参数
    # 登录系统
    allure.dynamic.title(case_name)
    login_llq = sele_setting.login(llq)
  # 这里的"llq"参数需根据实际情况调整


        # 导航到药品管理页面
    time.sleep(3)
    login_llq.find_element(by=By.LINK_TEXT, value="管理").click()

    time.sleep(3)
    login_llq.find_element(by=By.LINK_TEXT, value="药品").click()

    time.sleep(3)
    framel = login_llq.find_element(by=By.XPATH, value="html/body/div/div/div[3]/iframe[2]")
    login_llq.switch_to.frame(framel)

        # 获取当前总条数
    pagination_text = login_llq.find_element(
        by=By.XPATH,
        value="html/body/div/div/div[2]/div[1]/div[3]/div[1]/span"
    ).text
    before_num = pagination_text.split("共")[1][:-3].strip()

        # 点击添加按钮
    login_llq.find_element(by=By.LINK_TEXT, value="添加").click()

    time.sleep(3)
    login_llq.switch_to.default_content()

    time.sleep(3)
    add_frame = login_llq.find_element(by=By.XPATH, value="html/body/div[3]/div[2]/iframe")
    time.sleep(3)
    login_llq.switch_to.frame(add_frame)

        # 填写表单
    time.sleep(3)
    login_llq.find_element(by=By.NAME, value="productName").send_keys(product_Name)

    time.sleep(3)
    select_obj = login_llq.find_element(by=By.NAME, value="supplierId")
    if select:
        Select(select_obj).select_by_index(select)

    time.sleep(3)
    select_obj_unit = login_llq.find_element(by=By.NAME, value="unit")
    time.sleep(3)
    Select(select_obj_unit).select_by_index(2)  # 固定选择第三个单位

    time.sleep(3)
    login_llq.find_element(by=By.NAME, value="stockNum").send_keys(stock_Num)

    time.sleep(3)
    login_llq.find_element(by=By.NAME, value="intPrice").send_keys(int_Price)

    time.sleep(3)
    login_llq.find_element(by=By.NAME, value="outPrice").send_keys(outPrice)

    time.sleep(3)
    login_llq.switch_to.default_content()

        # 提交表单
    login_llq.find_element(by=By.LINK_TEXT, value="确定").click()
    time.sleep(3)

        # 重新获取总条数
    login_llq.switch_to.frame(framel)
    pagination_text = login_llq.find_element(by=By.XPATH,value="html/body/div/div/div[2]/div[1]/div[3]/div[1]/span").text
    after_num = pagination_text.split("共")[1][:-3].strip()
    if before_num<=after_num:
        a.info(case_name+'执行成功')
    else:
        a.error(case_name+'执行失败')


    #
    #     print(f"测试数据: {product_Name}, {stock_Num}, {int_Price}, {outPrice}")
    #     print(f"之前条数: {before_num}, 之后条数: {after_num}")
    #
    #     # 简单断言：假设所有测试用例都应该成功添加
    #     assert int(before_num) < int(after_num), "添加失败，记录数未增加"
    #
    # finally:
    #     # 关闭浏览器
    #     login_llq.quit()

    # login_llq.switch_to.default_content()
    #
    # login_llq.find_element(by=By.LINK_TEXT, value="注销").click()

    login_llq.quit()


#随机勾选
@allure.epic("医药管理系统接口测试报告")
@allure.feature("管理模块")
@allure.story('药品——删除')
def test_shanchu():
    """药品删除模块验证"""
    allure.dynamic.title("药品删除模块验证")

    login_llq = sele_setting.login(llq)

    time.sleep(3)
    login_llq.find_element(by=By.LINK_TEXT, value="管理").click()

    time.sleep(3)
    login_llq.find_element(by=By.LINK_TEXT, value="药品").click()
    time.sleep(3)

    # 进入到药品整体大框
    frame = login_llq.find_element(by=By.XPATH, value="html/body/div/div/div[3]/iframe[2]")
    login_llq.switch_to.frame(frame)

    # 删除前的总条数
    pagination_text = login_llq.find_element(
        by=By.XPATH,
        value="html/body/div/div/div[2]/div[1]/div[3]/div[1]/span"
    ).text
    before_num = pagination_text.split("共")[1][:-3].strip()

    # 随机勾选复选框
    count = login_llq.find_elements(by=By.NAME, value="btSelectItem")
    coun = len(count)
    if coun > 0:
        random_index = random.randint(0, coun - 1)
        random_checkbox = count[random_index]
        random_checkbox.click()

    # 点击删除按钮
    sa=login_llq.find_element(by=By.LINK_TEXT, value="删除").click()
    time.sleep(3)
    login_llq.switch_to.frame(sa)
    login_llq.find_element(by=By.LINK_TEXT, value="确认").click()
    login_llq.switch_to.default_content()
    time.sleep(3)
    framel = login_llq.find_element(by=By.XPATH, value="html/body/div/div/div[3]/iframe[2]")
    login_llq.switch_to.frame(framel)
    time.sleep(3) # 切回药品管理iframe

    # 获取执行删除后的总条数（修复元素定位问题）
    try:
        pagination_text = login_llq.find_element(
            by=By.XPATH,
            value="html/body/div/div/div[2]/div[1]/div[3]/div[1]/span"
        ).text
        after_num = pagination_text.split("共")[1][:-3].strip()

        if before_num > after_num:
            a.info("药品删除模块验证" + "删除成功")
        else:
            a.error("药品删除模块验证" + "删除失败")
    except Exception as e:
        a.error(f"获取删除后条数失败: {str(e)}")
        raise

    time.sleep(3)
    login_llq.quit()


#修改项目
@allure.epic("医药管理系统接口测试报告")
@allure.feature("管理模块")
@allure.story('药品——修改')
@pytest.mark.parametrize("mc,gys,dw",[("阿莫西林","2","3")])
def test_xiugai(mc,gys,dw):
    allure.dynamic.title("药品修改模块验证")

    login_llq = sele_setting.login(llq)

    time.sleep(3)

    login_llq.find_element(by=By.LINK_TEXT, value="管理").click()

    time.sleep(3)

    login_llq.find_element(by=By.LINK_TEXT, value="药品").click()

    time.sleep(3)

    framel = login_llq.find_element(by=By.XPATH, value="html/body/div/div/div[3]/iframe[2]")

    login_llq.switch_to.frame(framel)
    #-----------------------修改内容-----------------------------------------------------------
    count = login_llq.find_elements(by=By.NAME, value="btSelectItem")
    coun = len(count)
    if coun > 0:
        random_index = random.randint(0, coun - 1)
        random_checkbox = count[random_index]
        random_checkbox.click()

    time.sleep(3)

    login_llq.find_element(by=By.LINK_TEXT, value="修改").click()

    time.sleep(3)

    login_llq.switch_to.default_content()

    time.sleep(3)

    select_frame=login_llq.find_element(by=By.XPATH,value="html/body/div[3]/div[2]/iframe")

    login_llq.switch_to.frame(select_frame)

    time.sleep(3)


    #断言修改前
    old_value= login_llq.find_element(by=By.NAME, value="productName").get_attribute("value")

    # 修改：统一使用login_llq实例
    login_llq.find_element(by=By.NAME, value="productName").clear()
    time.sleep(5)

    # 修改：统一使用login_llq实例
    login_llq.find_element(by=By.NAME, value="productName").send_keys(mc)
    #修改后
    new_value= login_llq.find_element(by=By.NAME, value="productName").get_attribute("value")

    if old_value!=new_value:
        a.info("药品修改模块"+'名称修改成功')
    else:
        a.error("药品修改模块"+'名称修改失败')


    select_obj =login_llq.find_element(by=By.NAME, value="supplierId")

    old_supplier = Select(select_obj).first_selected_option.get_attribute("value")

    Select(select_obj).select_by_index(gys)
    time.sleep(3)

    new_supplier = Select(select_obj).first_selected_option.get_attribute("value")


    if old_supplier!=new_supplier:
        a.info("药品修改模块"+'供应商修改成功')
    else:
        a.error("药品修改模块"+'供应商修改失败')

    select_obj_unit = login_llq.find_element(by=By.NAME, value="unit")
    old_unit = Select(select_obj_unit).first_selected_option.get_attribute("value")

    Select(select_obj_unit).select_by_index(dw)
    time.sleep(3)

    new_unit = Select(select_obj_unit).first_selected_option.get_attribute("value")

    if old_unit!=new_unit:
        a.info("药品修改模块"+"单位修改成功")
    else:
        a.info("药品修改模块"+"单位修改失败")

    login_llq.switch_to.default_content()
    login_llq.find_element(by=By.LINK_TEXT,value="确定").click()

    login_llq.switch_to.frame(framel)

    time.sleep(3)


#查找
@allure.epic("医药管理系统接口测试报告")
@allure.feature("管理模块")
@allure.story('药品——查找')
def test_chazhao():
    allure.dynamic.title("药品查找模块验证")

    login_llq = sele_setting.login(llq)

    time.sleep(3)

    login_llq.find_element(by=By.LINK_TEXT, value="管理").click()

    time.sleep(3)

    login_llq.find_element(by=By.LINK_TEXT, value="药品").click()

    time.sleep(3)

    framel = login_llq.find_element(by=By.XPATH, value="html/body/div/div/div[3]/iframe[2]")

    login_llq.switch_to.frame(framel)
    # 获取当前总条数
    pagination_text = login_llq.find_element(
        by=By.XPATH,
        value="html/body/div/div/div[2]/div[1]/div[3]/div[1]/span").text

    befor_num = pagination_text.split("共")[1][:-3]

    #清空搜索框
    login_llq.find_element(by=By.NAME,value="productName").clear()
    #正确输入查找内容
    login_llq.find_element(by=By.NAME,value="productName").send_keys("阿莫西林")
    time.sleep(3)
    #点击搜索
    login_llq.find_element(by=By.LINK_TEXT,value="搜索").click()
    time.sleep(3)

    pagination_text = login_llq.find_element(
        by=By.XPATH,
        value="html/body/div/div/div[2]/div[1]/div[3]/div[1]/span").text
    after_num = pagination_text.split("共")[1][:-3]
    print(befor_num, "=-------------=", after_num)

    if befor_num>=after_num:
        a.info("药品查找模块验证"+'搜索成功')
    else:
        a.error("药品查找模块验证"+'搜索n失败')

    login_llq.find_element(by=By.NAME,value="supplierId").send_keys("1")
    time.sleep(3)
    # 点击搜索
    login_llq.find_element(by=By.LINK_TEXT, value="搜索").click()
    time.sleep(3)

    pagination_text = login_llq.find_element(
        by=By.XPATH,
        value="html/body/div/div/div[2]/div[1]/div[3]/div[1]/span").text
    after2_num = pagination_text.split("共")[1][:-3]
    print(after_num, "=-------------=", after2_num)
    if befor_num>=after_num:
        a.info("药品查找模块验证"+'执行成功')
    else:
        a.error("药品查找模块验证"+'执行失败')


    # #重置返回检测错误搜索
    # login_llq.find_element(by=By.LINK_TEXT,value="重置").click()
    # time.sleep(3)
    #
    # login_llq.find_element(by=By.NAME, value="productName").send_keys("啊啊啊")
    # time.sleep(3)
    # # 点击搜索
    # login_llq.find_element(by=By.LINK_TEXT, value="搜索").click()
    # time.sleep(3)






#
# #----------------------------------采购订单 --------------------------------------
# def test_caigou():
#     login_llq = sele_setting.login(llq)
#
#     time.sleep(3)
#
#     login_llq.find_element(by=By.LINK_TEXT, value="管理").click()
#
#     time.sleep(3)
#
#     login_llq.find_element(by=By.LINK_TEXT, value="采购订单(记录)").click()
#
#     time.sleep(3)
#
#     framel1 = login_llq.find_element(by=By.XPATH, value="html/body/div/div/div[3]/iframe[2]")
#
#     login_llq.switch_to.frame(framel1)
# #----------------------添加--------------------------------------------------
#     pagination_text = login_llq.find_element(
#         by=By.XPATH,
#         value="html/body/div/div/div[2]/div[1]/div[3]/div[1]/span").text
#
#     befor_num=pagination_text.split("共")[1][:-3]
#
#     login_llq.find_element(by=By.LINK_TEXT,value="添加").click()
#
#     time.sleep(3)
#
#     login_llq.switch_to.default_content()
#
#     time.sleep(3)
#
#     add_frame=login_llq.find_element(by=By.XPATH,value="html/body/div[3]/div[2]/iframe")
#
#     time.sleep(3)
#
#     login_llq.switch_to.frame(add_frame)
#
#     time.sleep(3)
#
#     select_obj = login_llq.find_element(by=By.NAME, value="supplierId")
#
#     time.sleep(3)
#
#     Select(select_obj).select_by_index(1)
#
#     time.sleep(3)
#
#     select_obj_unit = login_llq.find_element(by=By.NAME, value="productId")
#
#     time.sleep(3)
#
#     Select(select_obj_unit).select_by_index(1)
#
#     time.sleep(3)
#
#     login_llq.find_element(by=By.NAME,value="purchNum").send_keys(200)
#
#     time.sleep(3)
#
#     login_llq.switch_to.default_content()
#
#     login_llq.find_element(by=By.LINK_TEXT, value="确定").click()
#
#     time.sleep(3)
#
#     login_llq.switch_to.frame(framel1)
#
#     pagination_text = login_llq.find_element(
#         by=By.XPATH,
#         value="html/body/div/div/div[2]/div[1]/div[3]/div[1]/span").text
#     after_num = pagination_text.split("共")[1][:-3]
#     print(befor_num, "=-------------=", after_num)
#     assert int(befor_num.strip()) < int(after_num.strip())
#
#     login_llq.find_element(by=By.LINK_TEXT, value="4").click()
#
#     time.sleep(3)
#
#     qrrk=login_llq.find_element(by=By.LINK_TEXT, value="确认入库").click()
#
#     time.sleep(3)
#
#     login_llq.switch_to.frame(qrrk)
#
#     login_llq.find_element(by=By.LINK_TEXT, value="确认").click()
#     time.sleep(3)
#     login_llq.switch_to.default_content()
#
#     #搜索测试-----------------------------------
#     login_llq.switch_to.frame(framel1)
#     pagination_text = login_llq.find_element(
#         by=By.XPATH,
#         value="html/body/div/div/div[2]/div[1]/div[3]/div[1]/span").text
#     before_num1 = pagination_text.split("共")[1][:-3]
#
#     sell = login_llq.find_element(by=By.NAME, value="supplierId")
#     time.sleep(3)
#
#     count = login_llq.find_elements(by=By.NAME, value="supplierName")
#
#     time.sleep(3)
#
#     coun = len(count)
#     if coun > 0:
#         n = random.randint(0, coun - 1)
#         Select(sell).select_by_index(n + 1)
#     time.sleep(3)
#
#     sell1 = login_llq.find_element(by=By.NAME, value="productId")
#
#     time.sleep(3)
#
#     count = login_llq.find_elements(by=By.NAME, value="productName")
#     coun = len(count)
#     if coun > 0:
#         n = random.randint(0, coun - 1)
#         Select(sell1).select_by_index(n + 1)
#     time.sleep(3)
#
#
#     login_llq.find_element(by=By.LINK_TEXT,value="搜索").click()
#
#     time.sleep(3)
#     pagination_text = login_llq.find_element(
#         by=By.XPATH,
#         value="html/body/div/div/div[2]/div[1]/div[3]/div[1]/span").text
#     after_num1 = pagination_text.split("共")[1][:-3]
#     print(before_num1, "=-------------=", after_num1)
#     assert int(before_num1.strip()) >= int(after_num1.strip())
#
#     login_llq.find_element(by=By.LINK_TEXT,value="重置").click()
#
#     time.sleep(200)

























