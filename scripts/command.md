# 打开
geth --datadir /Users/apple/github/go-ethereum/local --rpc --rpccorsdomain "*"  --rpcapi "admin,clique,debug,eth,miner,net,personal,rpc,txpool,web3" --rpcport 8545  --rpcaddr 0.0.0.0 --allow-insecure-unlock --unlock 0

# 解锁
personal.unlockAccount(eth.coinbase,"123456")

# 获取私钥
/Users/apple/github/ethereumTool/venv/bin/python /Users/apple/github/ethereumTool/key_utils/getPrivateKey.py /Users/apple/github/go-ethereum/local/keystore/UTC--2019-12-14T03-43-55.622721000Z--14873f0584b85760ffa094a8283864df4c38dfe7 123456

0x14873f0584b85760ffa094a8283864df4c38dfe7

0x615546b6406de7d6d5e7d30d69f9c68477bac2473496b356821ad3a07d5c33d4


# 挖坑
geth attach /Users/apple/github/go-ethereum/local/geth.ipc

# 反编译
- get set合约
python graduate_main/abi_utils.py 0x5961Ff52353e3e9147BBae2ff7E4A31d172AA497
- 代币合约
python graduate_main/abi_utils.py  0xf23B908a4DD82aBf482AF0d1a0F6D99d84b3ABA8
