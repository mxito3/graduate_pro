from root_setup import *
from graduate_main.abi_utils import ABIUtil
from graduate_main.rlp_utils import RLPUtil
from hexbytes import HexBytes
#误调用检测
class ErrorCheck():
    #是否是误调用
    def is_error_exe(contract_addr,calldata):
        
        if isinstance(calldata,str):
            calldata=HexBytes(calldata.replace(" ",''))
        abi,have_fallback=ABIUtil.get_abi(contract_addr)
        
        all_support_funcs=[k for k in abi.keys()]
        print()
        print("所有支持的函数是{}".format(all_support_funcs))
        method_id,params,value=RLPUtil.get_params(calldata)
        #函数id是否存在
        if not method_id in all_support_funcs:
            return True
        #函数参数个数是否一致
        if len(params)!=len(abi[method_id]['params']):
            return True
        #函数是payable的，但是value是0
        if abi[method_id]['payable'] and value==0:
            return True

        return False

if __name__ == "__main__":
    raw="0xf8891185012a05f200830222e0945961ff52353e3e9147bbae2ff7e4a31d172aa49780a460fe47b100000000000000000000000000000000000000000000000000000000000004571ba071974ae3365e1dae3e945bb58caf4433179a316f32f387f955ed6849e0441066a05ad6d5940758e9afe1b74c7ff36c5146a89d00ecb83201340d68595632cea7a1"
    addr="0xf23B908a4DD82aBf482AF0d1a0F6D99d84b3ABA8"
    result=ErrorCheck.is_error_exe(addr,raw)
    print()
    print("误调用检测中..........")
    if result:
        print("此次调用是一次误调用")
    else:
        print("此次调用是正常调用")