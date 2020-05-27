
from root_setup import *
from graduate_main.error_exe_check import ErrorCheck
from graduate.contract import generate_calldata
from conf import contract_addr
if __name__ == "__main__":
    is_error_check=True
    raw=generate_calldata(contract_addr,is_error_check)
    transfer_func_name='a9059cbb'
    raw=raw.replace('095bcdb6',transfer_func_name)
    result=ErrorCheck.is_error_exe(contract_addr,raw)
    if result:
        print("此次调用是一次误调用")
    else:
        print("此次调用是正常调用")

        