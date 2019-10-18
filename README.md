## Safe scripts
This is a collection of script to interact with the Safe contract or verify information regarding a Safe.

### Setup
* Create Python3 virtual env
  * `python3 -m venv env`
* Activate virtual env
  * `. env/bin/activate`
* Install requirements
  * `pip install -r requirements.txt`

### Scripts

#### Verify seed (verify_seed.py)
This scripts allows you to verify that a mnemonic belongs to owners of a Safe (either a recovery phrase or an extension). It will also output which indices have been used to generate the owners.

##### Usage
* Add menmonic to `key_file`
  * `echo "<your mnemonic>" > key_file` 
* Call `verify_seed.py` with `key_file` and Safe address
  * `python verify_seed.py key_file <safe_address>`

##### Output
The script will output the owners of the Safe and an array of indices that can be used with the provided mnemonic to create an owner of the Safe.
In case of a recovery phrase gernerated by the mobile app the script should output 2 indices (0 and 1). To get the owner private key generate a HD node with the derivation path `m/44'/60'/0'/0` and derive a child with the appropriate index.

Example output:
```
safe: 0x1f6AD913fC2c8053Ed2951cA257e62f3c36b9874
owners: ['0x7A1784B429dBFEce6580EB1A891F0f4cf53E5705', '0x5921ed112f672AFB9943E5050b02824A4Ceb84b2', '0x8a872BEb182531aF4397224A3C12599E11932ec6', '0xCd55b245c44bbA97b2b7ebDe5157b2750968Fb6C']
owner indices: [0, 1]
```