import json
import requests
import difflib
from logs_floor import logs_pro;
#通过导入的日志文件调用方法生成实例化的日志对象
log_info=logs_pro.get_log();

#参数：请求方式 接口路径 接口请求参数

def requests_strong(inter_method,inter_url,inter_parms):
    # 通过判断接口的请求方式调用requests对象的不同方法
        if inter_method == "get":
    # 将requests对象请求后的对象进行接受，返回的是一个响应体(响应的状态码，响应报文信息)
            result = requests.get(url=inter_url, params=json.loads(inter_parms))
        else:

            result = requests.post(url=inter_url, data=json.loads(inter_parms))

        return result;


def if_resp_success(result,预期结果):
    if result.status_code==200 and difflib.SequenceMatcher(None,预期结果,result.text).ratio()>0.8:
        log_info.info("测试通过")
        return"√"
    else:
        log_info.error('接口测试不通过')
        return"×"
