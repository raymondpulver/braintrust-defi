from os.path import dirname, join
from json import loads
import os
from braintrust_defi.lib.artifacts import read_entire_file

this_dir = dirname(str(__file__))

def load_project_id():
  copy = dict(os.environ.copy())
  project_id = loads(read_entire_file(join(this_dir, 'infura.json')))['PROJECT_ID']
  copy['WEB3_INFURA_PROJECT_ID'] = project_id
  os.environ.clear()
  os.environ.update(copy)

def get_infura(network):
  load_project_id();
  if network == 'mainnet':
    from web3.auto.infura.mainnet import w3
    return w3
  elif network == 'kovan':
    from web3.auto.infura.kovan import w3
    return w3

def insert_scheme(scheme):
  copy = dict(os.environ.copy())
  copy['WEB3_INFURA_SCHEME'] = scheme
  os.environ.clear()
  os.environ.update(copy)


def get_infura_mainnet_url():
    load_project_id()
    from web3.auto.infura.endpoints import build_infura_url, INFURA_MAINNET_DOMAIN, HTTP_SCHEME
    insert_scheme(HTTP_SCHEME)
    return build_infura_url(INFURA_MAINNET_DOMAIN)
