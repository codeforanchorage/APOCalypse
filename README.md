# APOCalypse
Gaining insight into APOC, Alaska Public Offices Commission at http://doa.alaska.gov/apoc/

## Feeder.py

This script loads up SQS with URI to try for data. 


### Installation

This script uses boto to call the AWS API. It uses the python module Config to mange AWS c
redentials. On your filesystem NOT IN GIT make a file with the following structure:

```
credentials:
[
  {
    aws_access_key_id : 'YOUR_ACCESS_KEY_HERE'
    aws_secret_access_key : 'YOUR_SECRET_KEY_HERE'
    region : 'us-west-2'
  }
]
```
For more information on Config look at  https://pypi.python.org/pypi/config/0.3.7

With the above file on your filesystem, go into `feeder.py` and change the line:
```
    f = file('/Users/spustay/.aws/cfa_credentials_python_module_Config')
```
to the path in your filesystem with your credential file. You will need virtualenv installed lovcally. With it you can run:    

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python feeder.py

Which loads up the SQS queue.
