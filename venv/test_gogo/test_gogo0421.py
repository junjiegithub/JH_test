import requests
import jsonpath
import json
import pymysql
import re
def get_oms_conn():
    return pymysql.connect(
        host='172.29.76.72',
        port=3320,
        user='testoms',
        password='Test123456',
        database='testoms',
        charset='utf8'
    )

def get_os_conn():
    return pymysql.connect(
        host='172.29.76.112',
        port=3306,
        user='root',
        password='123456',
        database='jh_os',
        charset='utf8'
    )

headers ={"X-SHOPPY-ACCESS-TOKEN":"0c0aa7b4188f434bd829049a6587c052820d0798"}

url="https://openapi.xshoppy.top/order/orders/list"
data={
    'time_start':1618193378,
    'time_end':1618193398,
    'page':1,
    'limit':100,
    'financial_status':'paid'
    }

def xshoppy_orders_list():
    ret=requests.get(url,params=data,headers=headers)
    result=ret.json()
    #print(result)
    sku=jsonpath.jsonpath(result,'$.data.data[0].products[0].sku')
    email=jsonpath.jsonpath(result,'$.data.data[0].shipping.email')
    order_number=jsonpath.jsonpath(result,'$.data.data[0].order_number')
    #sku_string=string(sku[0])
    #print(sku[0])
    #print(type(sku[0]))
    slist = []
    s1 = sku[0].split('+')                          #字符串切割
    for ss1 in s1:
        sl = ss1.split('*')
        slist += sl

    list=[sku[0],email[0],order_number[0],slist[0],slist[1],slist[2],slist[3],slist[4],slist[5]]
    #sku002=re.findall(r"([A-Z0-9]*)[\*]?",sku[0])     #正则
    return list

def os_sku_sql():
    a=xshoppy_orders_list()[3]
    sql=f"SELECT valid_sku FROM `jh_os`.`jh_coding_sku` WHERE `sku` = '{a}'"
   #print( sql)
    return sql

def query_data_os():
    conn=get_os_conn()
    try:
        sql=os_sku_sql()
        cursor=conn.cursor(pymysql.cursors.DictCursor)
        result=cursor.execute(sql)
        re=cursor.fetchall()
        #print(re[0]['valid_sku'])
        valid_sku=re[0]['valid_sku']
        return  valid_sku
    finally:
        conn.close()

def 

def query_data_oms(oms_sku_sql):
    conn=get_oms_conn()
    try:
        cursor=conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(oms_sku_sql)
        print(cursor.fetchall())
        return cursor.fetchall()
    finally:
        conn.close()


if __name__ == '__main__':
    xshoppy_orders_list()
    os_sku_sql()
    query_data_os()
