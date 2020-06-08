from os.path import dirname, join
from eth_account import Account
from dydx.client import Client
from web3 import Web3
from ..lib.artifacts import read_artifacts
from ..lib.infura import get_infura_mainnet_url

this_dir = dirname(str(__file__))

dydx_artifacts = read_artifacts(join(this_dir, "..", "artifacts", "dydx", "*.json"))

class DydxPerpetualAdapter:
    def __init__(self, bt, rpc_endpoint):
        self.bt = bt
        self.client = Client(Web3.toHex(Account.create('').privateKey), 0, rpc_endpoint)
    def set_account(self, account):
        self.client = Client(account.privateKey, 0, get_infura_mainnet_url())
    def __getattr__(self, name):
        artifact = dydx_artifacts[name]
        address = artifact["networks"][self.bt.chain_id]["address"]
        return self.bt.w3.eth.contract(address=address, abi=artifact["abi"])
