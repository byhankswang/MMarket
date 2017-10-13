# -*- coding: utf-8 -*-
"""
    Created on 2017-09-28
    Author - Hanks.Wang
    Contact - byhankswang@163.com
    Description - 本模块中的类和函数基于各交易所的数据绘制图表

    TODO List:
        (1)添加子图标题;

"""

import numpy as np
import matplotlib.pyplot as plt


"""
    #8月21日至9月19日的动力煤1801合约数据;
    #x为日期数据,y为结算价格,zd为多头持仓量,zk为空头持仓量,z为净持仓量;
    #日期: ['0821','0822','0823','0824','0825','0828','0829','0830','0831',
            '0901','0905','0906','0907','0908','0911','0912','0913','0914','0915','0918','0919','0920', '0921', '0922', '0925', '0926', '0927', '0928', '0929',
            '1009', '1010', '1011', '1012', '1013']
"""
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]

# ZC1801日结算价
y = [600.8, 597, 590.4, 591.4, 612.6, 611.4, 609.4, 616.8, 619.2,
     623.6, 635.4, 636.4, 635.6, 634, 639.2, 644.6, 657.2, 656.2, 656.8, 653.2, 643.8, 658.6,
     658, 645.2, 633.6, 627.4, 636.4, 638, 640.4, 625.6,
     626, 611.6, 613.6, 612, 616.8]

#YAQH's 多空持仓量及净持仓量
zd = [3588, 2367, 5935, 9939, 16417, 14124, 4065, 3963, 3859,
      4073, 4540, 4820, 4713, 4726, 5386, 13815, 20739, 21181, 21911, 23482, 23341, 25483, 27845, 27245, 27314, 27864, 30508, 30468, 29802, 27370,
      19877, 13787, 15614, 13836, 13087]
zk = [7816, 5471, 5218, 3945, 7700,  7718,  7256, 6046, 6939, 6946, 8233, 8962, 9478, 8921, 8058, 7820,  8075,  9156,  9611,  9372,  9723,  10792,
      11179, 8645, 8234, 6612, 6389, 6874, 4066, 4184,
      4408, 5308, 5163, 4828, 4346]
zj = list(map(lambda x:x[0] - x[1], zip(zd, zk)))

def open_position_char(contract = "ZC1801",organization = "YA"):
    chart = plt.figure(figsize=(20,12))
    subchart1 = chart.add_subplot(3, 1, 1)
    subchart2 = chart.add_subplot(3, 1, 2)
    subchart3 = chart.add_subplot(3, 1, 3)

    #ax1为ZC1801的日结算价图,ax2净持仓量, ax3多空持仓量
    subchart1.set_title("%s Settlement Price Trend" % contract)
    subchart1.plot(x, y, "b--", linewidth=1)
    subchart2.set_title("%s Net Open Interest" % organization)
    subchart2.plot(x, zj, "y--", linewidth=1)
    subchart3.set_title("%s More & Empty Interest" % organization)
    subchart3.plot(x, zd, "b--", linewidth=1)
    subchart3.plot(x, zk, "r--", linewidth=1)

    plt.savefig("ZC1801-YAQH")
    chart.show()

open_position_char()