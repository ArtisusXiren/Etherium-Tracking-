from web3 import Web3
def provider():
    w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.g.alchemy.com/v2/V2NWqHZFLlvDX10Vo1LrnX_kStsn-Yt-'))
    return w3
