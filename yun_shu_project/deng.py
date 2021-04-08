import csv
import requests
from requests.auth import HTTPBasicAuth

b=[]
#data_xshoppy=csv.reader(open(r"C:\Users\pp\Desktop\xshoppy_shop.csv","r",encoding='utf-8'))。
data_xshoppy=csv.reader(open(r"C:\Users\Administrator\Desktop\xshoppy_shop.csv","r",encoding='utf-8'))

for ii in data_xshoppy:
    b.append(ii)
# print(b)
url_xshoppy='https://openapi.xshoppy.shop/order/orders/list'
for jj in b:
    if jj[2] == "" :
        head={'X-SHOPPY-ACCESS-TOKEN':jj[4]}
        re_xshoppy2=requests.get(url=url_xshoppy,headers=head)
        res_xshoppy2=re_xshoppy2.json()
        print(jj[0],res_xshoppy2["data"]["totalCount"])
    else:
        head = {'X-SAIL-ACCESS-TOKEN': jj[4]}
        re_xshoppy3=requests.get(url=url_xshoppy,headers=head,auth=HTTPBasicAuth(username=jj[2],password=jj[3]))
        #re_xshoppy=requests.get(url=url_xshoppy,headers=head)
        res_xshoppy=re_xshoppy3.json()
        if res_xshoppy["code"]==-1:
            print(res_xshoppy["code"])
        else:
            print(jj[0],res_xshoppy)
