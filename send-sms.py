from twilio.rest import Client
import requests

account_sid = '' # Removed account id for privacy purposes 
auth_token = '' # Removed auth_token for privacy purposes 

client = Client(account_sid, auth_token) # ensure proper authentication

response = requests.get('http://api.open-notify.org/astros.json')
people = response.json()
num_people = people['number']

txtmssg = "Hi Nimra! There are " + str(num_people) + " people in space right now."
message = client.messages.create(
    to = "4372194466",
    from_ = "+12109879583",
    body = txtmssg
)

