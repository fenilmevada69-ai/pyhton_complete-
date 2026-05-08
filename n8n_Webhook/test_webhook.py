import requests

user_message = "Can you tell me about black holes in 3-4 lines?"
request_message = {"message" : user_message}
url = "http://localhost:5678/webhook-test/31b14723-5dd3-4132-ac94-5e9be7cab254"
response = requests.post(url, json=request_message)

print(response.status_code)
print(response.json()[0]["output"])