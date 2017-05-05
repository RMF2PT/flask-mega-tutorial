## Test script to see if can send emails from Cloud9 with Mailgun ##

import requests
from config import MAILGUN_API_KEY, MAILGUN_DOMAIN, ADMINS

key = MAILGUN_API_KEY
sandbox = MAILGUN_DOMAIN
recipient = ADMINS

request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
request = requests.post(request_url, auth=('api', key), data={
    'from': 'hello@example.com',
    'to': recipient,
    'subject': 'Hello',
    'text': 'Hello from Mailgun'
})

print('Status: {0}'.format(request.status_code))
print('Body:   {0}'.format(request.text))