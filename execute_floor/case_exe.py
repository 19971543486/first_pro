import pytest;
import os;

pytest.main(["../case_floor/aaaaa.py","-sv","--alluredir","../report_floor/data"])
os.system("allure generate ../report_floor/data -o ../report_floor/html --clean")
#medicine   shanchu     xiugai      chazhao     caigou

