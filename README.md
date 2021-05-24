# bud-batch-insert

## Requirements
To install python required libraries:
```
pip install -r requirements.txt
```  

Create "fileInput" folder where you will place the excel file to be loaded

Create "logs" folder where logs of the execution will be places with timestamp
### Environment Variables:

```bash
# POSTGRES
# ----------------------------
POSTGRES_HOST='localhost'
POSTGRES_PORT='5432'
POSTGRES_USER='business'
POSTGRES_PASSWORD='changeme' #Nescesary for local development only
POSTGRES_DB='business'

# AUTH0
# ----------------------------
AUTHZ_DOMAIN='dev-q3g5h8jb.us.auth0.com'
AUTHZ_CLIENT_ID=
AUTHZ_CLIENT_SECRET=

#AWS
# ----------------------------
#AWS_REGION=
#AWS_CREDENTIALS_ACCESS_KEY_ID - The AWS access key ID for this application
#AWS_CREDENTIALS_SECRET_ACCESS_KEY - The AWS secret access key for this application
```

## Usage

Load all data to database:
```bash
python load_to_database.py
```

Optional arg:  
env: string to define environment variables to be used, if empty will use .env  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sample:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`python main.py development` - Will use .env.development

----
Send verification email to all users:
```bash
python send_verification.py
```

Optional arg:  
env: string to define environment variables to be used, if empty will use .env  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sample:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`python main.py development` - Will use .env.development
