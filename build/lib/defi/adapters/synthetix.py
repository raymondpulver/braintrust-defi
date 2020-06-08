from os.path import dirname, join
from ..lib.artifacts import read_artifacts

this_dir = dirname(str(__file__))

synthetix_artifacts = read_artifacts(join(this_dir, "..", "artifacts", "synthetix", "*.json"))


class SynthetixAdapter:
    def __init__(self, bt):
        self.bt = bt
    def __getattr__(self, name):
        document = synthetix_artifacts["SynthetixDeployments"]
        target = document["targets"][name]
        source = document["sources"][target["source"]]
        return self.bt.w3.eth.contract(address=target["address"], abi=source["abi"])
