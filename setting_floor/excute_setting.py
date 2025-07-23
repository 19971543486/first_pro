import xlrd;
from xlutils.copy import copy;
#接收 Excel 文件路径和工作表名称作为参数，返回一个包含所有接口信息的列表
def read_interface(case_file_url,case_sheet):
    # 通过调用xlrd对象的open_workbook()方法读取指定的excel文件
    file_excel = xlrd.open_workbook(case_file_url);
    # 通过读取到的文件指定要操作的sheet，通过调用excel文件对象的sheet_by_name操作指定的sheeet表
    shop_sheet = file_excel.sheet_by_name(case_sheet);
    # 通过sheet对象的nrows属性获取sheet表中的信息条数
    print(shop_sheet.nrows);
    shop_num = shop_sheet.nrows;
    # 创建一个空列表，用于存储从Excel中读取的数据
    inter_list = [];
    # 通过for循环获取每一行信息
    for i in range(1, shop_num):
        shop_info = {};
        shop_info["接口名称"] = shop_sheet.row(i)[1].value;
        shop_info["接口路径"] = shop_sheet.row(i)[3].value;
        shop_info["请求方式"] = shop_sheet.row(i)[4].value;
        shop_info["接口请求参数"] = shop_sheet.row(i)[5].value;
        shop_info["预期结果"] = shop_sheet.row(i)[6].value;

        inter_list.append(shop_info)
    return inter_list
'''
参数 响应信息列表   参数结果列表  用例文件的路径  sheet表名称  

'''
def write_text_result(resp_text_list,result_list,case_file_url,case_sheet):
    #打开excel文件
    case_file = xlrd.open_workbook(case_file_url);
    # 创建可写副本
    new_case_file = copy(case_file);
    # 获取工作表
    new_sheet = new_case_file.get_sheet(case_sheet);
    #按照行列写入信息
    for i in range(len(result_list)):
        new_sheet.write(i + 1, 7, resp_text_list[i])
        new_sheet.write(i + 1, 8, result_list[i])
#通过调用缓存文件的save方法将修改信息写入实际文件中
    new_case_file.save(case_file_url);

#通过 xlrd 库读取指定 Excel 文件，并返回其包含的所有工作表名称列表
def get_sheet_list(excue_file_url):
    case_file=xlrd.open_workbook(excue_file_url);
    return case_file.sheet_names();

get_sheet_list(r"C:\Users\nakex\Desktop\测试用例.xlsx")