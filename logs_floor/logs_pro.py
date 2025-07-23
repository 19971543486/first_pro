import logging
from datetime import datetime

def get_log():
    #获取日志对象 logging，get
    logs_info=logging.getLogger("移动端自动化测试框架日志对象")
    #设置日志处理级别
    #logging.basicConfig(level=logging.DEBUG)
    logs_info.setLevel(logging.DEBUG)

    s_handler = logging.StreamHandler()
    log_file_name=str(datetime.today()).split(" ")[0]

    f_handler = logging.FileHandler("../logs_floor/"+log_file_name+".log",encoding="utf-8");
    formatter = logging.Formatter("----%(asctime)s---%(name)s---%(levelname)s---%(filename)s:[%(lineno)d]---%(message)s");


    s_handler.setFormatter(formatter)
    f_handler.setFormatter(formatter)


    #将处理日志添加至对象中
    logs_info.addHandler(s_handler)
    logs_info.addHandler(f_handler)

    return logs_info;