#coding=utf-8

import requests
#session=requests.session()
#token='eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIiwianRpIjoiMCVpMk9fK05dYC52aCJ9.eyJqdGkiOiIwJWkyT18rTl1gLnZoIiwiaWF0IjoxNjE2MDU0OTc4LCJleHAiOjE2MTYxNDEzNzgsImlkIjo0NywibmFtZSI6Ilx1Njc0ZVx1NWI1MFx1NTE0OSJ9.'


# class Gg_api(object):
#     def int__(self):
#         pass
def Gg_a():
        url = 'https://testads-sc-api.jhongnet.com/admin/login'
        data = {"email": "li.zg@jiahongnet.com", "pwd": "123456", "code": "1234"}
        #headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        rep=requests.post(url=url,data=data)
        #print (rep.text)
        #login_token=rep.json().get('data')
        login_token=(rep.json()["data"]["token"])
        #print(login_token)
        return login_token
        #print(rep)
        #js=rep.json()
        # if js["msg"]==u"操作成功":
        #     print('登录接口联调成功')
        #     assert True
        # else:
        #     print('登录接口联调失败')
def Gg_dsl(login_token):
        #testads-sc-api.jhongnet.com/admin/work-order-recharge/list
        dsl_url='https://testads-sc-api.jhongnet.com/admin/work-order-recharge/list'
        #dsl_data={"createTime":"","tStatus":["1"],"agentId":[],"minAmount":"","maxAmount":"","companyName":"","advCName":"","auName":"","searchName":"","searchFlag":"1","position":[],"order_param":"","order_sort":"","merchantId":"","multiSearchType":"","searchValue":"","page":1,"pageSize":10,"total":17085,"endTime":""}
        dsl_data='{"createTime":"","tStatus":[1],"agentId":[],"minAmount":"","maxAmount":"","companyName":"","advCName":"","auName":"","searchName":"","searchFlag":"1","position":[],"order_param":"","order_sort":"","merchantId":"","multiSearchType":"","searchValue":"","page":1,"pageSize":10,"total":17085,"endTime":""}'
        #print(dsl_data)
        #dsl_headers={'Content-Type': 'application/x-www-form-urlencoded','token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIiwianRpIjoiMCVpMk9fK05dYC52aCJ9.eyJqdGkiOiIwJWkyT18rTl1gLnZoIiwiaWF0IjoxNjE1OTU5NDEyLCJleHAiOjE2MTYwNDU4MTIsImlkIjo0NywibmFtZSI6Ilx1Njc0ZVx1NWI1MFx1NTE0OSJ9.'}
        #dsl_headers={'Content-Type': 'application/json;','token':login_token}

        zzz=requests.post(url=dsl_url,data=dsl_data,headers=headers)
        print(zzz.text)
        #js = rep.json()


def Gg_cz(recgargeId):
        cz_url='https://testads-sc-api.jhongnet.com/admin/work-order-recharge/accept'
        cz_data={"rechargeId":recgargeId}
        #
        hecz_headers={'Content-Type': 'application/x-www-form-urlencoded','token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIiwianRpIjoiMCVpMk9fK05dYC52aCJ9.eyJqdGkiOiIwJWkyT18rTl1gLnZoIiwiaWF0IjoxNjE1OTU5NDEyLCJleHAiOjE2MTYwNDU4MTIsImlkIjo0NywibmFtZSI6Ilx1Njc0ZVx1NWI1MFx1NTE0OSJ9.'}
        rep=requests.post(url=cz_url,data=cz_data,headers=headers)

        print(rep.text)

if __name__=='__main__':
    # d=Gg_api()

    Gg_a()
    headers = {'Content-Type': 'application/json;', 'token': Gg_a()}
    Gg_dsl(Gg_a())
    Gg_cz()