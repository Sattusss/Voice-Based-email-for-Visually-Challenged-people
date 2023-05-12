import requests

url = "https://testmail.app/api/json"
api_key = "a7847024-ea2a-47fb-8780-3bfffded880f"

payload = {
    "to": "satyamsln2001@gmail.com",
    "subject": "Test Email",
    "text": "This is a test email sent using the TestMail API"
}

headers = {
    "X-API-KEY": api_key
}

response = requests.post(url, json=payload, headers=headers)

print(response.status_code)
print(response.text)