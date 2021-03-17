#coding=utf-8
import requests
import json
url='https://testads-sc-api.jhongnet.com/admin/login'
data={"email":"li.zg@jiahongnet.com","pwd":"123456","code":"1234"}


#headers={'Content-Type': 'application/json'}
headers={'Content-Type': 'application/x-www-form-urlencoded'}
rep=requests.post(url=url,data=data,headers=headers)

print (rep.text)