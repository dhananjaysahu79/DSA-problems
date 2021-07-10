import requests

x = requests.get('https://api.wazirx.com/api/v2/tickers')

print(x.text)