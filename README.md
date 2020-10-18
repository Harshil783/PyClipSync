# PyClipSync

A Open Source Project Helps To Sync ClipBoard From Anywhere

## To Do List
- :white_check_mark: Using Firebase For Storing Data
- :white_check_mark: Create GUI for handling frontend stuff
- :white_check_mark: Create an algorithm to track Clip Board
- :heavy_check_mark: Password Reset Email Sending
- :heavy_check_mark: Email Verification

- [ ] Create rest API to get and store data
- [ ] Create GUI for handling frontend stuff
- [ ] Create an algorithm to track Clip Board

## Instruction for running these files.
- Create virtual environment
- Install all modules of requirements.txt (Use `pip install -r requirements.txt` to install all modules)
- Create your own config file.  
    Create one file named `config.py`. In that config file include the following code:
     ```
    from firebase import Firebase

    config = {
      "apiKey": "apiKey",
      "authDomain": "projectId.firebaseapp.com",
      "databaseURL": "https://databaseName.firebaseio.com",
      "storageBucket": "projectId.appspot.com"
    }

    firebase = Firebase(config)
    ```
- Now, run the file.
