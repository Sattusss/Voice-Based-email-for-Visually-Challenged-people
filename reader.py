import json, requests, argparse
from datetime import datetime

# argparse
parser = argparse.ArgumentParser(description="You can add tag to filter emails")
parser.add_argument('--tag', required=False)
args = parser.parse_args()

tag = None
if args.tag:
    tag = args.tag

# load credentials file which has api key and namespace for Testmail.app
f = open('credentials.json')
data = json.load(f)

api_key = data['myAccount']['apiKey']
namespace = data['myAccount']['namespace']

f.close()

# show inbox
url = ''
if tag:
    url = f'https://api.testmail.app/api/json?apikey={api_key}&namespace={namespace}&tag={tag}&pretty=true'
else:
    url = f'https://api.testmail.app/api/json?apikey={api_key}&namespace={namespace}&pretty=true'
response = requests.get(url).json()

print("INBOX:")
print()
for email in response['emails']:
    print('-'*60)
    print('From: '+email['from'])
    print('Subject: '+email['subject'])
    print('Time: ',datetime.fromtimestamp(email['timestamp'] / 1000))
    print('Testmail.app Tag: '+email['tag'])
    print('Content:\n'+email['text'])
    print()
print('-'*60)