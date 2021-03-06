from root_setup import *
from pano.loader import Loader
from pano.vm import VM
import json
from panoramix import decompile
class ABIUtil():
    @staticmethod
    def get_abi(addr):
        abi,have_fallback=decompile(addr)
        print("反编译.............")
        print("abi是{}".format(abi))
        result={}
        has_fallback=False
        for k,v in abi.items():
            name=v.get('name')
            if not name:
                name=v.get('fname')
                if name=="_fallback()":
                    continue
                else:  #unknown
                    continue
            params=v['params']
            payable=v['payable']
            result[k]={'name':name,'params':params,'payable':payable}
        return result,have_fallback


if __name__ == "__main__":
    if len(sys.argv)<2:
        print("传合约地址进来兄弟")
        exit()
    addr=sys.argv[1]
    abi,have_fallback=ABIUtil.get_abi(addr)
    print(abi)
    print()
    print(have_fallback)
