import binascii
import requests
from utils.hd_key import mnemonic_to_hd_node

SAFE_RELAY_SERVICE = "https://safe-relay.staging.gnosisdev.com/api/" #"https://safe-relay.gnosis.io/api/"
SAFE_INFO_ENDPOINT = "v1/safes/%s"
ETH_DERIVATION_PATH = "m/44'/60'/0'/0"
if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'r') as f:
        mnemonic = ' '.join(f.read().split())

    safe = sys.argv[2]
    index_range = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    safe_info = requests.get(SAFE_RELAY_SERVICE + SAFE_INFO_ENDPOINT % safe).json()
    print(f'safe: {safe}')
    print(f'owners: {safe_info["owners"]}')

    node = mnemonic_to_hd_node(mnemonic, str_derivation_path=ETH_DERIVATION_PATH)

    owner_indices = [] 
    for i in range(index_range):
        address = node.derive(i).public_key().address()
        if address in safe_info['owners']:
            owner_indices.append(i)

    print(f'owner indices: {owner_indices}')