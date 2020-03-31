import sys
import os.path
root_directory=os.path.abspath(os.path.join(os.path.abspath(__file__),"../../"))
sys.path.append(root_directory)
from pano.loader import Loader
from pano.vm import VM
import json
from panoramix import decompile
class ABIUtil():
    @staticmethod
    def get_abi(addr):
        abi,have_fallback=decompile(addr)
        result=[]
        has_fallback=False
        print(abi)
        for k,v in abi.items():
            name=v.get('name')
            # print(v)
            if not name:
                name=v.get('fname')
                if name=="_fallback()":
                    continue
                else:  #unknown
                    continue
            params=v['params']
            result.append({'name':name,'params':params})
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
