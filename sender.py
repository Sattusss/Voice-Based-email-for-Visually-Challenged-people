import requests
def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/sandboxb8f7e2805db544d3a0bf819f8a34f752.mailgun.org",
		auth=("api", "key-ea34841b8ae974d1935841b25f04c4d3"),
		data={"from": "Excited User <mailgun@YOUR_DOMAIN_NAME>",
			"to": ["bar@example.com", "YOU@YOUR_DOMAIN_NAME"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomeness!"})