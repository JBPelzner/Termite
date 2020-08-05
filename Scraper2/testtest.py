import requests
import json

hostname = 'http://ec2-18-224-6-72.us-east-2.compute.amazonaws.com'

test_user_agreement = requests.get(hostname + ":3005/user/user_agreements_frontend?id="+'Jen Jen Jen')

information = json.loads(test_user_agreement.text)


print(information)