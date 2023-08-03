import base64
import json
import re
import requests

## Bing Info
bing_submission_url = "https://ssl.bing.com/webmaster/api.svc/json/SubmitUrlbatch?apikey="
print(r"""
░█▀▄░▀█▀░█▀█░█▀▀░█▀▀░█░█░█▀▄░█░░
░█▀▄░░█░░█░█░█░█░█░░░█░█░█▀▄░█░░
░▀▀░░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀
""")
x = 'Enter Api:'
bing_api_key =  input(x)
r = 'Enter URL:'
l = 'Url List: '
bing_submission_urls = { "siteUrl": input(r), "urlList": [input(l)]} #CreateURL list to submit to Bing.
headers = { "Content-Type": "application/json; charset=utf-8","Host": "ssl.bing.com" } #Bing response headers.
## Make request to Bing.
submission_request = requests.post(f"{bing_submission_url}{bing_api_key}", headers=headers, json=bing_submission_urls)
if submission_request.status_code == 200:
	print("Submission to Bing was successful.")
else:
	print("Submission was not successful. Please try again.")
