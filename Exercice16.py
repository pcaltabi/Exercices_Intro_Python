
import requests

url = 'http://python.something.ch/admin/index.php'

params = {'action': 'add', 'name':'Pietro','collection':'2018_de_la_muerte','price':'99', 'stock':'12'}
ret = requests.post(url = url, params = params)
#data = ret.json()

