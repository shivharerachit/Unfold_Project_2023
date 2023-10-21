// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.5.0 <0.9.0;
contract footage{
    uint canAddFootage;
    struct Footage {
        string Date;
        string Time;
        string Location;
        string Camera_id;
    }
    mapping(uint=>Footage) public data_stored;
    constructor() {
        canAddFootage = 1;
    }
    function data(uint _regis,string memory _date,string memory _time,string memory _location,string memory _camid) public {
    if(canAddFootage==1){
        data_stored[_regis]=Footage(_date,_time,_location,_camid);
    }
    }
}