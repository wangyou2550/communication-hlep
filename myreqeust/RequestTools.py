

import requests
import json

class RequestTools(object):
    '''
    功能：封装requests各种方法
    '''
    # get方法封装

    @classmethod
    def get_method(clc,url,data=None,header=None):

        if header is not None:
           res = requests.get(url,params=data,headers=header)
        else:
           res = requests.get(url,params=data)
        return res.json()["data"]

    # post方法封装
    @classmethod
    def post_method(clc, url, data=None, header=None):
        global res
        if header is not None:
            res = requests.post(url, json=data, headers=header)

        else:
             res = requests.post(url, json=data)
        if str(res) == "":
            return res.json()

        else:
            return res.text

    # put方法封装
    @classmethod
    def put_method(clc,url,data=None,header=None):
         if header is not None:
            res = requests.put(url,json=data,headers=header)
         else:
            res = requests.delete(url, json=data)
         return res.json()

   # delete方法封装
    @classmethod
    def delete_method(clc, url, data=None, header=None):
         if header is not None:
            res = requests.delete(url, json=data, headers=header)
         else:
            res = requests.delete(url, json=data)
         return res.json()

# 调用主方法
    @classmethod
    def send_requests(clc,method,url,data=None,header=None):
          if method == 'get' or method == 'GET':
             res = clc.get_method(url,data,header)
          elif method == 'post' or method =='POST':
             res = clc.post_method(url,data,header)
          elif method == 'put' or method == 'PUT':
             res = clc.post_method(url,data,header)
          elif method == 'delete' or method == 'DELETE':
             res = clc.post_method(url,data,header)
          else:
             res = "请求方式有误！"


          res = json.loads(res)
          return res

