// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0;

import "./SimpleStorage.sol";

contract StorageFactory {

    SimpleStorage[] public simpleStorageArray;

    function createSimpleStorageContract() public {
        SimpleStorage simpleStorage = new SimpleStorage();
        simpleStorageArray.push(simpleStorage);
    }

    function sfStore(uint256 _simpleStorageIndex, uint256 _simpleStorageNumber) public {
        require(simpleStorageArray.length > _simpleStorageIndex, "There is no contract at that index.");
        SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
        simpleStorage.store(_simpleStorageNumber);
    }

    function retrieveFavoriteNumberFromContractAtIndex(uint256 index) public view returns(uint256){
        require(simpleStorageArray.length > index, "There is no contract at that index.");
        SimpleStorage _contract = simpleStorageArray[index];
        uint256 favoriteNumber = _contract.retrieve();
        return favoriteNumber;
    }

}
