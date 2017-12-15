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
import re
import datetime
from urllib import urlencode
from urllib2 import urlopen, Request, HTTPError
from httplib import IncompleteRead
import pandas as pd

DATE_PATTERN = re.compile(r'^([0-9]{4})[-/]?([0-9]{2})[-/]?([0-9]{2})')
FUTURE_SYMBOL_PATTERN = re.compile(r'(^[A-Za-z]{1,2})[0-9]+')

CZCE_COLUMNS = ['pre_settle','open','high','low','close','settle','change1','change2','volume','open_interest','oi_chg','turnover','final_settle']
OUTPUT_COLUMNS = ['symbol', 'date', 'open', 'high', 'low', 'close', 'volume', 'open_interest', 'turnover', 'settle', 'pre_settle', 'variety']
CZCE_DATAHOLDING_COLUMNS = []
CZCE_DATAHOLDING_OUTPUT_COLUMNS = []


CZCE__FUTURE_DAILY_URL = 'http://www.czce.com.cn/portal/DFSStaticFiles/Future/%s/%s/FutureDataDaily.txt'
CZCE_FUTURE_DATAHOLDING_URL = "http://www.czce.com.cn/portal/DFSStaticFiles/Future/%s/%s/FutureDataHolding.txt"

# 郑州商品交易所获取数据时需要伪装成浏览器访问
czce_request_header = {
    "Host":"www.czce.com.cn",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Cookie":"uid=c647f5527115643f3a2c01068f40c003; a5787_times=2; TS014ada8c=0169c5aa3235993b7ce07c1ddc8071a9febf1fd174459fdcb5ffbffb0e8858f6848d93985ac5c5f4cfe1281b8820d503c8023f5cf7; BIGipServerwww_cbd=842836160.23067.0000; a5787_pages=11; JSESSIONID=671SZMyGJjp1wZjnHTXWk5ns07j4x1gZ7t8R2GGsNz8vDvTmccvp!-1351565760"
}

#
def convert_date(date):
    """
    transform a date string to datetime.date object.
    :param day, string, e.g. 2016-01-01, 20160101 or 2016/01/01
    :return: object of datetime.date(such as 2016-01-01) or None
    """
    if isinstance(date, datetime.date):
        return date
    elif isinstance(date, str):
        match = DATE_PATTERN.match(date)
        if match:
            groups = match.groups()
            if len(groups) == 3:
                return datetime.date(year=int(groups[0]), month=int(groups[1]), day=int(groups[2]))
    return None

# 获取“郑州商品交易所->交易数据->期货交易数据->期货持仓排名”的数据
def get_czce_future_dataholding(date=None):

    day = convert_date(date) if date is not None else datetime.date.today()
    request_obj = Request(CZCE_FUTURE_DATAHOLDING_URL % (day.strftime('%Y'),day.strftime('%Y%m%d')), headers=czce_request_header)

    try:
        html_init = urlopen(request_obj).read().decode('gbk', 'ignore')
    except HTTPError as reason:
        if reason.code != 404:
            print(CZCE_FUTURE_DATAHOLDING_URL % (day.strftime('%Y'),day.strftime('%Y%m%d')), reason)
        return

    print(html_init)
    if html_init.find(u'网页错误') >= 0:
        return

    print("-----------------------A")



    return pd.DataFrame(dict_data)[output_columns]

# 获取“郑州商品交易所->交易数据->期货交易数据->期货”的数据
def get_czce_future_data_daily(date = None):
    day = convert_date(date) if date is not None else datetime.date.today()
    request_obj = Request(CZCE__FUTURE_DAILY_URL % (day.strftime('%Y'), day.strftime('%Y%m%d')),
                          headers=czce_request_header)
    testdata = urlopen(request_obj)
    html = testdata.read().decode('gbk', 'ignore')


    html = [i.replace(' ','').split('|') for i in html.split('\n')[:-4] if i[0][0] != u'小']
    print(html)

    #TODO change string to DataFrame and return DataFrame
    #return pd.DataFrame(dict_data)[output_columns]