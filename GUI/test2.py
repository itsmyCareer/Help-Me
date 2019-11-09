import requests, time

url = 'http://127.0.0.1:5000/help'
data = {'location': '1', 'time': time.strftime('%c', time.localtime(time.time())), 'device_id': 'DEVICE005'}

requests.post(url, json = data)