#coding=utf-8
#随机生成4位字符
import random
import string
# def fun():
#     num=string.ascii_letters+string.digits
#     print(num)
#     l=[]
#     for i in range(4):
#         a=random.choice(num)
#         l.append(a)
#     print(''.join(l))
#     print(l)
#     return l
# fun()

def fun():
    s=""
    for i in range(0,4):
        if random.randint(0,1)==0:
            #生成字母
            s=s+chr(random.randint(65,90))
        else:
            #生成数字
            s=s+str(random.randint(0,9))
    print(s)
    return s

fun()

"""sq_data="""{"merchantId":1011,"accountList":[{"accountName":"""+c+""","timeZone":2,"adsName":"","creditCode":"","license":"","domains":"www.baidu.com","gmails":"665@qq.com"}],"num":1}""""""
