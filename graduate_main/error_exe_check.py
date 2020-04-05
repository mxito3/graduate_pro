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
    raw="0xf8890f85012a05f200830222e094151a2a029b6149d4bed3d1    \
1f59abc562b22b664b80a460fe47b1000000000000000000000000000000000000000000000000000000000000\
04571ba002c5f724d43878e7b26f03d96e0beee8164175bc0a24a18fb6dddb103aa6244ba01a8ad8126ed78df1\
2c2d2014b8b536e4a3defed878adf2d2adf48b6974db9093"
    addr="0x455eb180ccA0da93967E713e0e0AdF08e727c353"
    print(ErrorCheck.is_error_exe(addr,raw))