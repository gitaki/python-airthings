import requests
data = {'id': 9,'name': 'temp: 28.4'}
response = requests.post('http://localhost:5000/post',data)
print(response.status_code)
print(response.text)