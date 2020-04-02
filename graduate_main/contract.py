from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
import time

#配置
abi = '[{"constant":false,"inputs":[{"name":"b","type":"uint256"}],"name":"set","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"constant":true,"inputs":[],"name":"a","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]'
contract_address = '0x151a2a029B6149D4bed3d11F59AbC562B22B664B'
rpc_path = "http://localhost:8545"


# w3=Web3(Web3.IPCProvider("~/.ethereum/geth.ipc"))
w3 = Web3(Web3.HTTPProvider(rpc_path))
w3.middleware_stack.inject(geth_poa_middleware, layer=0)  #use ipc
w3.isConnected(),'connect fail 请打开geth'

#eth_rinekby
key = '0x615546b6406de7d6d5e7d30d69f9c68477bac2473496b356821ad3a07d5c33d4'

from_address =w3.toChecksumAddress("0x14873f0584b85760ffa094a8283864df4c38dfe7")


nonce = w3.eth.getTransactionCount(from_address) 
contract = w3.eth.contract(address=contract_address, abi=abi)
transaction =  contract.functions.set(1111).buildTransaction({
                'nonce': nonce,
                'from':from_address,
                'gas':140000,#火币使用的，56000一般就够了
                'gasPrice':5000000000,
        })

print(transaction)
signed = w3.eth.account.signTransaction(transaction,key)

print(signed)

# #When you run sendRawTransaction, you get back the hash of the transaction:
# transactionHash=w3.eth.sendRawTransaction(signed.rawTransaction)  
# print(transactionHash.hex())
# print("waiting for mined")
# transaction=w3.eth.waitForTransactionReceipt(transactionHash, timeout=120)
# print("打包成功")
# print(transaction)