
from root_setup import *
from graduate_main.error_exe_check import ErrorCheck
from graduate.contract import generate_calldata
from conf import contract_addr
if __name__ == "__main__":
    is_error_check=False
    raw='0xf8aa1785012a05f200830222e09415066dc26ab16a9309e9cdb8b940ed5eccbbaaf580b844a9059cbb000000000000000000000000e6103e918fc8554b92cbd8f7e1527a1a75ce425400000000000000000000000000000000000000000000000000000000000000641ca08e76ddac2de526dce99ee71ff6a325db2bfbbc1d3cea04b161b83661a8376acba015b00174bde8dc1a2c5a56c384e08c816028d344734e3fa82ed6b763d20f0185'
    func_name="a9059cbb"
    raw=raw.replace(func_name,"ffffffff")
    result=ErrorCheck.is_error_exe(contract_addr,raw)
    if result:
        print("此次调用是一次误调用")
    else:
        print("此次调用是正常调用")

        