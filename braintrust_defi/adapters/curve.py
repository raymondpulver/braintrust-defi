from os.path import dirname, join
from braintrust_defi.lib.artifacts import read_artifacts

this_dir = dirname(str(__file__))

curve_artifacts = read_artifacts(join(this_dir, "..", "artifacts", "curve", "*.json"))

class Curve:
    def __init__(self, bt, name):
        self.bt = bt
        self.token = bt.w3.eth.contract(address=curve_artifacts['curves'][name]['token'], abi=curve_artifacts['CurveToken']['abi'])
        self.swap = bt.w3.eth.contract(address=curve_artifacts['curves'][name]['swap'], abi=curve_artifacts['Curvefi']['abi'])

class CurveAdapter:
    def __init__(self, bt):
        self.bt = bt

    def __getattr__(self, name):
        return Curve(self.bt, name)
