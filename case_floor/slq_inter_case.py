from setting_floor import excute_setting, requests_setting
import allure;
import pytest

shop_resp_text_list=[];
shop_result_list=[];
@allure.epic("shop项目接口测试报告")
@allure.feature("shop模块")
@pytest.mark.parametrize("inter_info",excute_setting.read_interface(r"C:\Users\nakex\Desktop\测试用例.xlsx","shop"))
def test_shop_on_inter(inter_info):
    allure.dynamic.title(inter_info.get("接口名称"))
    resp=requests_setting.requests_strong(inter_info.get("请求方式"),inter_info.get("接口路径"),inter_info.get("接口请求参数"))
    result_text=requests_setting.if_resp_success(resp,inter_info.get("预期结果"))

    shop_resp_text_list.append(resp.text)
    shop_result_list.append(result_text)

def test_write_shop():
    excute_setting.write_text_result(shop_resp_text_list,shop_result_list,r"C:\Users\nakex\Desktop\测试用例.xlsx","shop")


lol_resp_text_list=[];
lol_result_list=[];
@allure.epic("lol项目接口测试报告")
@allure.feature("lol模块")
@pytest.mark.parametrize("inter_info",excute_setting.read_interface(r"C:\Users\nakex\Desktop\测试用例.xlsx","lol"))
def test_lol_on_inter(inter_info):
    allure.dynamic.title(inter_info.get("接口名称"))
    resp=requests_setting.requests_strong(inter_info.get("请求方式"),inter_info.get("接口路径"),inter_info.get("接口请求参数"))
    result_text=requests_setting.if_resp_success(resp,inter_info.get("预期结果"),)

    lol_resp_text_list.append(resp.text)
    lol_result_list.append(result_text)

def test_write_lol():
    excute_setting.write_text_result(lol_resp_text_list,lol_result_list,r"C:\Users\nakex\Desktop\测试用例.xlsx","lol")




personnel_resp_text_list=[];
personnel_result_list=[];
@allure.epic("personnel项目接口测试报告")
@allure.feature("personnel模块")
@pytest.mark.parametrize("inter_info",excute_setting.read_interface(r"C:\Users\nakex\Desktop\测试用例.xlsx","personnel"))
def test_personnel_on_inter(inter_info):
    allure.dynamic.title(inter_info.get("接口名称"))
    resp=requests_setting.requests_strong(inter_info.get("请求方式"),inter_info.get("接口路径"),inter_info.get("接口请求参数"))
    result_text=requests_setting.if_resp_success(resp,inter_info.get("预期结果"))

    personnel_resp_text_list.append(resp.text)
    personnel_result_list.append(result_text)

def test_write_personnel():
    excute_setting.write_text_result(personnel_resp_text_list,personnel_result_list,r"C:\Users\nakex\Desktop\测试用例.xlsx","personnel")