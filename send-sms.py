from twilio.rest import Client
import requests

account_sid = 'AC88f37128bf012799675177ce00e4c02e'
auth_token = 'a677f41c3cf8489a925e8b19cd2c9c73'

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

