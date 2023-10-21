from web3 import Web3
from solcx import compile_source

# Connect to an Ethereum node (e.g., Infura)
w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/30f6fddb41584e529e54e553bcff1f5f'))

# Your Ethereum account address
your_ethereum_address = '0x35D3310A613F2D753AC7dE94586b9d7601B6B390'

# Solidity source code
contract_source_code = """
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.6.0 <0.9.0;

contract footage {
    uint canAddFootage;
    
    struct Footage {
        string Date;
        string Time;
        string Location;
        string Camera_id;
    }
    
    mapping(uint => Footage) public data_stored;

    constructor() public {
        canAddFootage = 1;
    }

    function addData(uint _regis, string memory _date, string memory _time, string memory _location, string memory _camid) public {
        if (canAddFootage == 1) {
            data_stored[_regis] = Footage(_date, _time, _location, _camid);
        }
    }
}

"""

# Compile the contract
compiled_sol = compile_source(contract_source_code)
contract_interface = compiled_sol['<stdin>:footage']

# Set your Ethereum account as the default account
w3.eth.defaultAccount = your_ethereum_address

# Create a contract object
contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

# Deploy the contract
tx_hash = contract.constructor().transact()
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

# Get the contract address
contract_address = tx_receipt['contractAddress']
print(f'Contract deployed at address: {contract_address}')

