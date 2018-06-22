import requests
import json

token_url = 'http://192.168.6.224:8000/api2/auth-token/'
librarys_url = 'http://192.168.6.224:8000/api2/repos/'
token_p = {'username': 'wd@wdcloud.cc', 'password': '123456'}
wdlibraryid = ''

r = requests.post(token_url, token_p)

token = r.json()[u'token']
token_headers={'Authorization':'Token {0}'.format(token)}
r = requests.get(librarys_url, headers=token_headers)

librarys = r.json()
for i in range(len(librarys)):
    if librarys[i][u'name'] == 'wd':
        wdlibraryid = librarys[i][u'id']

filename = 'JPEG_20180613_114816_263654347.jpg'
fileinfor_url = 'http://192.168.6.224:8000/api2/repos/{0}/file/detail/?p=/{1}'.format(wdlibraryid, filename)
r = requests.get(fileinfor_url, headers=token_headers)

fileinfor = r.json()

hasfile = u'id' in fileinfor



