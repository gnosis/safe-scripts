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