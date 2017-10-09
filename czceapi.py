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

DATE_PATTERN = re.compile(r'^([0-9]{4})[-/]?([0-9]{2})[-/]?([0-9]{2})')

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

    testdata = urlopen(request_obj)
    html = testdata.read().decode('gbk', 'ignore')
    print(html)
    print("===========================byhankswang================================")
'''
    #TODO 当前需要做的工作是把返回内容以DataFrame格式存储；
    df = [i.replace(' ', '').split('|') for i in html.split('\n')[:-4] if i[0][0] != u'小']
    print(df)
    dict_data = list()
    day_const = int(day.strftime('%Y%m%d'))
    for row in html[2:]:
        m = ct.FUTURE_SYMBOL_PATTERN.match(row[0])
        if not m:
            continue
        row_dict = {'date': day_const, 'symbol': row[0], 'variety': m.group(1)}
        for i, field in enumerate(listed_columns):
            if row[i + 1] == "\r":
                row_dict[field] = 0.0
            elif field in ['volume', 'open_interest', 'oi_chg', 'exercise_volume']:
                row[i + 1] = row[i + 1].replace(',', '')
                row_dict[field] = int(row[i + 1])
            else:
                row[i + 1] = row[i + 1].replace(',', '')
                row_dict[field] = float(row[i + 1])
        dict_data.append(row_dict)

    return pd.DataFrame(dict_data)[output_columns]
'''

def get_czce_():
    return