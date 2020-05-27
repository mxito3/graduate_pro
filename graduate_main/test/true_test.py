
from root_setup import *
from graduate_main.error_exe_check import ErrorCheck
from graduate.contract import generate_calldata
from conf import contract_addr
if __name__ == "__main__":
    is_error_check=False
    raw=generate_calldata(contract_addr,is_error_check)
    result=ErrorCheck.is_error_exe(contract_addr,raw)
    if result:
        print("此次调用是一次误调用")
    else:
        print("此次调用是正常调用")

        