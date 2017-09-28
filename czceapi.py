# -*- coding:utf-8 -*-
"""
    Created on 2017-09-28
    Author - Hanks.Wang
    Contact - byhankswang@163.com
    Description - 本模块中的类和函数用于从郑州商品交易所获取交易数据，并对交易数据进行数据清洗

    TODO List:
        (1)先以函数的方式进行定义，后面把函数集成到类中;
        (2)增加其他郑州商品交易所接口；

"""


from urllib import urlencode
from urllib2 import urlopen, Request, HTTPError
from httplib import IncompleteRead


request_header = {
    "Host":"www.czce.com.cn",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0",  # 伪装成浏览器访问
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    #"Accept-Language": "en-US,en;q=0.5",
    "Cookie":"uid=c647f5527115643f3a2c01068f40c003; a5787_times=2; TS014ada8c=0169c5aa3235993b7ce07c1ddc8071a9febf1fd174459fdcb5ffbffb0e8858f6848d93985ac5c5f4cfe1281b8820d503c8023f5cf7; BIGipServerwww_cbd=842836160.23067.0000; a5787_pages=11; JSESSIONID=671SZMyGJjp1wZjnHTXWk5ns07j4x1gZ7t8R2GGsNz8vDvTmccvp!-1351565760"
}


# 获取“郑州商品交易所->交易数据->期货交易数据->期货持仓排名”的数据
def get_czce_dataholding():
    request_obj = Request('http://www.czce.com.cn/portal/DFSStaticFiles/Future/2017/20170926/FutureDataHolding.txt',
                          headers=request_header)
    testdata = urlopen(request_obj)
    df = testdata.read().decode('gbk', 'ignore')
    print(df)


def get_czce_():
    return