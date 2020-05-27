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
        print()
        print("误调用检测中..........")
        if not method_id in all_support_funcs:
            print("合约不支持函数{}".format(method_id))
            return True
        #函数参数个数是否一致
        if len(params)!=len(abi[method_id]['params']):
            print("调用参数个数是 {},合约的此函数的函数参数个数是{}".format(len(params),len(abi[method_id]['params'])))
            print("函数参数个数不一致")
            return True
        # #函数是payable的，但是value是0
        # if abi[method_id]['payable'] and value==0:
        #     print("函数是payable的，但是value是0")
        #     return True
        return False

if __name__ == "__main__":
    raw="0xf8911285012a05f200830222e0945961ff52353e3e9147bbae2ff7e4a31d172aa497880de0b6b3a7640000a412514bba00000000000000000000000000000000000000000000000000000000000000011ba057edf3d576c33efdaf020eda42cd7a822b725475a18da9aacec6b22db2093305a06c123173172b4dda62f0e075460bbd74f8306730999ebe4a63951dc75c803f2b"
    addr="0xf23B908a4DD82aBf482AF0d1a0F6D99d84b3ABA8"
    result=ErrorCheck.is_error_exe(addr,raw)
    
    if result:
        print("此次调用是一次误调用")
    else:
        print("此次调用是正常调用")