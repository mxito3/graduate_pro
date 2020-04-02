from root_setup import *
import rlp
from hexbytes import (
    HexBytes,
)
from eth_account.account import Transaction
import json
from utils.json_encode import JsonEncoder
from web3 import Web3
from web3.contract import Contract
from eth_utils.crypto import keccak
class RLPUtil():
    @staticmethod 
    def decode(raw):
        raw_decoded=rlp.decode(raw)
        tx_deserialized = Transaction.deserialize(raw_decoded).as_dict()
        # tx_dict=json.loads(tx_deserialized,cls=JsonEncoder)
        for k,v in tx_deserialized.items():
            if isinstance(v,bytes):
                tx_deserialized[k]=HexBytes(v).hex()
        return tx_deserialized
    @staticmethod
    def get_data_from_raw(raw):
        tx_deserialized=RLPUtil.decode(raw)
        data=tx_deserialized['data']
        contract_addr=Web3.toChecksumAddress(tx_deserialized['to'])
        return data,contract_addr
    @staticmethod
    def get_params(raw):
        data,contract_addr=RLPUtil.get_data_from_raw(raw)
        method_id=data[0:10]
        params=[]
        index_start=10
        for index in range(int(len(data[10:])/64)):
            # print(index)
            end=index_start+64*(index+1)
            param=data[index_start:end]
            params.append(param)
            index_start+=end
        return method_id,params


if __name__ == "__main__":
    raw=HexBytes("0xf8890f85012a05f200830222e094151a2a029b6149d4bed3d1\
1f59abc562b22b664b80a460fe47b1000000000000000000000000000000000000000000000000000000000000\
04571ba002c5f724d43878e7b26f03d96e0beee8164175bc0a24a18fb6dddb103aa6244ba01a8ad8126ed78df1\
2c2d2014b8b536e4a3defed878adf2d2adf48b6974db9093")
    # print(RLPUtil.decode(raw))
    # print(RLPUtil.get_data_from_raw(raw))
    print(RLPUtil.get_params(raw))