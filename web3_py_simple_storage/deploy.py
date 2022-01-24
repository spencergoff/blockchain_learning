from solcx import compile_standard, install_solc
import json
import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()
install_solc('0.6.0')

with open('./SimpleStorage.sol', 'r') as f:
    simple_storage_file = f.read()

compiled_sol = compile_standard(
    {
        'language': 'Solidity',
        'sources': {'SimpleStorage.sol': {'content': simple_storage_file}},
        'settings': {
            'outputSelection': {
                '*': {
                    '*': ['abi', 'metadata', "evm.bytecode", 'evm.sourceMap']}
            }
        }
    },
    solc_version = '0.6.0',
)

with open('compiled_code.json', 'w') as file:
    json.dump(compiled_sol, file)

bytecode = compiled_sol['contracts']['SimpleStorage.sol']['SimpleStorage']['evm']['bytecode']['object']

abi = compiled_sol['contracts']['SimpleStorage.sol']['SimpleStorage']['abi']

# For connecting to Ganache
w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/41469ce51dbe472186d27f756e62ca6d'))
chain_id = 5 # the chain id of Goerli is 5
my_address = '0x00000000000000000000'
private_key = os.getenv('PRIVATE_KEY')

# Create the contract in Python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
nonce = w3.eth.getTransactionCount(my_address)

transaction = SimpleStorage.constructor().buildTransaction(
    {
        'chainId': chain_id,
        'gasPrice': w3.eth.gas_price,
        'from': my_address,
        'nonce': nonce
    }
)

signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# Interact with the deployed contract
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
initial_stored_value = simple_storage.functions.retrieve().call()
print(f'initial_stored_value: {initial_stored_value}')
store_txn = simple_storage.functions.store(7).buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce + 1
    }
)
signed_store_txn = w3.eth.account.sign_transaction(
    store_txn, private_key
)
send_store_txn = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(send_store_txn)
new_stored_value = simple_storage.functions.retrieve().call()
print(f'new_stored_value: {new_stored_value}')