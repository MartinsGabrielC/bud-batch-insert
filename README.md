# bud-batch-insert

## Requirements
To install python required libraries:
```
pip install -r requirements.txt
```

## Usage

Load all data to database:
```
python load_to_database.py
```

Optional arg:  
env: string to define environment variables to be used, if empty will use .env  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sample:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`python main.py development` - Will use .env.development

----
Send verification email to all users:
```
python send_verification.py
```

Optional arg:  
env: string to define environment variables to be used, if empty will use .env  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sample:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`python main.py development` - Will use .env.development
