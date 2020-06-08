from web3 import Web3, EthereumTesterProvider, HTTPProvider
from web3.middleware import construct_sign_and_send_raw_middleware
from .adapters.dydx import DydxPerpetualAdapter
from .adapters.curve import CurveAdapter
from .adapters.synthetix import SynthetixAdapter
from .lib.infura import get_infura, get_infura_mainnet_url


class BrainTrustEngine:
    def __init__(self, network):
        self.initialize_w3(network)
        self.chain_id = self.w3.net.version
        self.dydx = DydxPerpetualAdapter(self, get_infura_mainnet_url())
        self.curve = CurveAdapter(self)
        self.synthetix = SynthetixAdapter(self)

    def initialize_w3(self, network):
        self.w3 = (
            get_infura(network)
            if network == "mainnet" or network == "kovan" 
            else Web3(
                EthereumTesterProvider() if network == "test" else HTTPProvider(network)
            )
        )

    def set_signer(self, account):
        self.w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))
        self.w3.eth.defaultAccount = account.address
        self.dydx.set_account(account)

def get_engine(network='mainnet'):
    return BrainTrustEngine(network)
