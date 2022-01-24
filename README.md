# blockchain_learning
This repo contains various small code samples I create while learning blockchain.

Sources(s):
- freeCodeCamp.org's Solidity, Blockchain, and Smart Contract Course

## SimpleStorage.sol
This is a basic smart contract written in Solidity that I deployed to the Goerli Test Network using the Remix IDE for Ethereum. It allows transactions that add and retrieve "people" objects to and from the blockchain. 

Here's the last deployment I made: https://goerli.etherscan.io/address/0xc75ae43a4ccb4480c64431a26efdf49b02488968

## StorageFactory.sol
This is a solidity contract that allows users to create contracts based on SimpleStorage. Users can also set and retrieve properties from existing contracts.

Here's the last deployment I made: https://goerli.etherscan.io/address/0xf747bF6EeBca46CdC302A8eE7a749Abf0965f29C

## FundMe.sol
This is a solidity contract that allows people to fund it using an Ethereum-based wallet such as MetaMask. It also allows the creator to withdraw funds. 

Here's the last deployment I made: https://goerli.etherscan.io/address/0x6d840EF95F32Dc4AD00aef40ae1E54F4A6C05eeC

## deploy.py
This is a Python script that deploys the SimpleStorage smart contract to the Goerli test network and makes calls to the deployed contract's functions. 
