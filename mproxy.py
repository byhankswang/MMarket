# -*- coding:utf-8 -*-
import requests
from urllib import urlencode
from urllib import quote
import chardet

'''
    @TODO LIST
    (1)后台程序定时监测快代理的稳定性, 并统计可用城市及可用城市的IP数量;
'''


header = {
    "Host": "www.kuaidaili.com",
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}

#免费代理页面
FREE_PROXY_TARGET_URL = ("http://www.kuaidaili.com/free/inha/1")
#开放代理SVIP账户页面
OPEN_PROXY_TARGET_URL = "http://svip.kuaidaili.com/api/getproxy/?orderid=910838254256636&num=5&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=1&method=2&an_an=1&an_ha=1&sep=1&f_loc=1&area=%s"



"""
    快代理HTTP请求时各个字段的含义:
		参数			字段          	是否必填	说明     
		订单号          	orderid		是           	查看我的订单,订单账户中有该编号
		提取数量        	num		    是		普通用户：1 ~ 999; VIP/SVIP/专业版：1 ~ 9999
		所在地区        	area		否		ip所在地区, 支持按 国家/省/市 筛选; 多个地区用英文逗号分隔，如 北京,上海
		排除地区        	area_ex		否		多个地区用英文逗号分隔，如 中国,美国
		筛选端口号		port		否		多个端口号用英文逗号分隔，如 8080,18186
		排除端口号		port_ex		否		多个端口号用英文逗号分隔，如 8080,8000
		筛选IP			ipstart		否		筛选以特定部分开头的IP, 比如: 120.52.
		排除IP			ipstart_ex	否		排除以特定部分开头的IP, 比如: 120.52.
		运营商			carrier		否		0: 全部, 1: 联通/网通, 2: 电信, 3: 移动, 4: 铁通，5: 教育网，6: 阿里云
		匿名度			多选		    否		多个字段可以同时复用，如an_ha=1&an_an=1
					    an_ha		否		an_ha=1(高匿名代理)
					    an_an		否		an_an=1(匿名代理)
					    an_tr		否		an_tr=1(透明代理)
		响应速度		    多选		    否		多个字段可以同时复用，如sp1=1&sp3=1
					    sp1		    否		sp1=1(极速代理,响应速度<1秒)
					    sp2		    否		sp2=1(快速代理,响应速度1~3秒)
					    sp3		    否		sp3=1(慢速代理,响应速度>3秒)
		代理协议		    protocol	否		protocol=1(筛选HTTP代理); protocol=2(筛选HTTPS代理, 同时也支持HTTP)
		POST支持		    method		否		method=1(支持HTTP GET方法); method=2(支持 HTTP POST, 同时也支持GET)
		代理稳定性		quality		否		quality=1(不筛选(默认)); quality=1(VIP稳定); quality=2(SVIP专业版非常稳定);不间断地监测每个代理ip的历史数据，根据算法智能判别当前的稳定性
		结果排序		    sort		否		返回的代理列表的排序方式, sort=0(默认值)，sort=1(按从快到慢响应速度排序)，sort=2(按从近到远最后检测时间排序)
		结果定制		    多选		    否		提取结果包含的字段,顺序排列, 英文逗号分隔)
					    f_loc		否		f_loc=1(VIP/SVIP专业版提取结果包含地区信息)
					    f_an		否		f_an=1(VIP/SVIP专业版提取结果包含匿名度信息)
					    f_pr		否		f_pr=1(VIP/SVIP专业版提取结果包含代理协议信息,data-title="取值说明" 目前支持的协议有HTTP和HTTPS(支持HTTPS的代理ip同时也支持HTTP))
					    f_sp		否		f_sp=1(VIP/SVIP专业版提取结果包含响应速度信息)
					    f_fc		否		f_fc=1(专业版提取结果包含该代理的历史提取次数)
		浏览器支持		多选		    否		
					    b_pcchrome	否		b_pcchrome=1(谷歌浏览器)
					    b_pcie		否		b_pcie=1(IE/360浏览器)
					    b_pcff		否		b_pcff=1(Firefox火狐浏览器)
					    b_android	否		b_android=1(安卓手机浏览器)
					    b_iphone	否		b_iphone=1(iPhone手机浏览器)
					    b_ipad		否		b_ipad=1(iPad浏览器)
		IP去重			dedup		否		dedup=1(过滤今天提取过的IP)
		返回格式		    format		否		接口返回内容的格式，format=jason(json格式), format=xml(xml格式)
		结果分隔符		sep		    否		提取结果列表中每个结果的分隔符, sep=1(\r\n分隔(默认)), sep=2(\n分隔), sep=3(空格分隔), sep=4(|分隔), 此外还支持自定义
            

    参考链接 ：www.kuaidaili.com/genapiurl?orderid=910838254256636
"""




'''
i = '北京'
j = '广州'
print(quote(i))
print(quote(j))

#快代理的GET请求中中文地名使用urlencode的编码方式, Python中通过quote函数获取该编码
html = requests.get(url=(OPEN_PROXY_TARGET_URL % quote(j)), headers=header, timeout=30).content
print(html)
'''


province_list = ["江苏省", "广东省", "北京市", "浙江省","四川省", "山东省", "上海市",
"河南省", "重庆市", "陕西省", "广西", "安徽省", "云南省", "山西省",
"河北省", "福建省", "吉林省", "湖北省", "内蒙古", "黑龙江省", "辽宁省",
"新疆", "江西省", "湖南省", "西藏自治区", "海南省", "贵州省", "天津市",
"甘肃省", "青海省", "东京都"]

province_utf82urlencode_list = [
#省份（UTF-8）          urlencode
{"江苏省": "%E6%B1%9F%E8%8B%8F%E7%9C%81"},
{"广东省": "%E5%B9%BF%E4%B8%9C%E7%9C%81"},
{"北京市": "%E5%8C%97%E4%BA%AC%E5%B8%82"},
{"浙江省": "%E6%B5%99%E6%B1%9F%E7%9C%81"},
{"四川省": "%E5%9B%9B%E5%B7%9D%E7%9C%81"},
{"山东省": "%E5%B1%B1%E4%B8%9C%E7%9C%81"},
{"上海市": "%E4%B8%8A%E6%B5%B7%E5%B8%82"},
{"河南省": "%E6%B2%B3%E5%8D%97%E7%9C%81"},
{"重庆市": "%E9%87%8D%E5%BA%86%E5%B8%82"},
{"陕西省": "%E9%99%95%E8%A5%BF%E7%9C%81"},
{"广西": "%E5%B9%BF%E8%A5%BF"},
{"安徽省": "%E5%AE%89%E5%BE%BD%E7%9C%81"},
{"云南省": "%E4%BA%91%E5%8D%97%E7%9C%81"},
{"山西省": "%E5%B1%B1%E8%A5%BF%E7%9C%81"},
{"河北省": "%E6%B2%B3%E5%8C%97%E7%9C%81"},
{"福建省": "%E7%A6%8F%E5%BB%BA%E7%9C%81"},
{"吉林省": "%E5%90%89%E6%9E%97%E7%9C%81"},
{"湖北省": "%E6%B9%96%E5%8C%97%E7%9C%81"},
{"内蒙古": "%E5%86%85%E8%92%99%E5%8F%A4"},
{"黑龙江省": "%E9%BB%91%E9%BE%99%E6%B1%9F%E7%9C%81"},
{"辽宁省": "%E8%BE%BD%E5%AE%81%E7%9C%81"},
{"新疆": "%E6%96%B0%E7%96%86"},
{"江西省": "%E6%B1%9F%E8%A5%BF%E7%9C%81"},
{"湖南省": "%E6%B9%96%E5%8D%97%E7%9C%81"},
{"西藏自治区": "%E8%A5%BF%E8%97%8F%E8%87%AA%E6%B2%BB%E5%8C%BA"},
{"海南省": "%E6%B5%B7%E5%8D%97%E7%9C%81"},
{"贵州省": "%E8%B4%B5%E5%B7%9E%E7%9C%81"},
{"天津市": "%E5%A4%A9%E6%B4%A5%E5%B8%82"},
{"甘肃省": "%E7%94%98%E8%82%83%E7%9C%81"},
{"青海省": "%E9%9D%92%E6%B5%B7%E7%9C%81"},
{"东京都": "%E4%B8%9C%E4%BA%AC%E9%83%BD"}]






for i in province_list:
    print("{\"%s\": \"%s\"}," % (i,quote(i)))

    #print(chardet.detect(i))
    #print(quote(i))
    #print(type(quote(i)))
