# -*- coding:utf-8 -*-
import requests


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
OPEN_PROXY_TARGET_URL = "http://svip.kuaidaili.com/api/getproxy/?orderid=910838254256636&num=100&area=%E5%8C%97%E4%BA%AC&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=1&method=2&an_an=1&an_ha=1&sep=1"


http://svip.kuaidaili.com/api/getproxy/?orderid=910838254256636&num=1&area_ex=%E6%B9%96%E5%8D%97&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=1&method=2&an_an=1&an_ha=1&sep=1

"""
    快代理HTTP请求时各个字段的含义:
		参数			    字段      是否必填	说明     
		订单号          	orderid		是      查看我的订单,订单账户中存有该编号
		提取数量        	num		    是		普通用户：1 ~ 999; VIP/SVIP/专业版：1 ~ 9999
		所在地区        	area		否		ip所在地区,支持按 国家/省/市 筛选；多个地区用英文逗号分隔,如:北京,上海
		排除地区        	area_ex		否		多个地区用英文逗号分隔, 如:中国,美国
		筛选端口号		port		否		多个端口号用英文逗号分隔, 如 8080,18186
		排除端口号		port_ex		否		多个端口号用英文逗号分隔, 如 8080,8000
		筛选IP			ipstart		否		筛选以特定部分开头的IP, 比如: 120.52.
		排除IP			ipstart_ex	否		排除以特定部分开头的IP, 比如: 120.52.
		运营商			carrier		否		0: 全部, 1: 联通/网通, 2: 电信, 3: 移动, 4: 铁通，5: 教育网，6: 阿里云
		匿名度			多选			否	    多个字段可以同时复用，如an_ha=1&an_an=1
					    an_ha		否		an_ha=1(高匿名代理)
					    an_an		否		an_an=1(匿名代理)
					    an_tr		否		an_tr=1(透明代理)
		响应速度		    多选		    否		多个字段可以同时复用，如sp1=1&sp3=1
					    sp1 		否		sp1=1(极速代理,响应速度<1秒)
					    sp2		    否		sp2=1(快速代理,响应速度1~3秒)
					    sp3	    	否		sp3=1(慢速代理,响应速度>3秒)
		代理协议		    protocol	否		按代理协议筛选(1: HTTP, 2: HTTPS(同时也支持HTTP))
		POST支持		    method		否		按支持 GET/POST 筛选(1: 支持HTTP GET, 2: 支持 HTTP POST(同时也支持GET))
		代理稳定性		quality		否		快代理不间断地监测每个代理ip的历史数据，根据算法智能判别当前的稳定性(0: 不筛选(默认) 1: VIP稳定 2: SVIP专业版非常稳定)
		结果排序		    sort		否		返回的代理列表的排序方式,默认值为0，1为按响应速度排序（从快到慢），2为按最后检测时间(从近到远)
		结果定制		    多选	    	否		提取结果包含的字段,顺序排列, 英文逗号分隔)
					    f_loc		否		VIPSVIP专业版提取结果包含地区信息,取值为1
					    f_an		否		VIPSVIP专业版提取结果包含匿名度信息，取值为1
					    f_pr		否		VIPSVIP专业版提取结果包含代理协议信息,data-title="取值说明" 目前支持的协议有HTTP和HTTPS（支持HTTPS的代理ip同时也支持HTTP）
					    f_sp		否		VIPSVIP专业版提取结果包含响应速度信息，取值为1
					    f_fc		否		专业版提取结果包含该代理的历史提取次数，取值为1
		浏览器支持		多选		    否		
					    b_pcchrome	否		b_pcchrome=1(谷歌浏览器)
					    b_pcie		否		b_pcie=1(IE/360浏览器)
					    b_pcff		否		b_pcff=1(Firefox火狐浏览器)
					    b_android	否		b_android=1(安卓手机浏览器)
					    b_iphone	否		b_iphone=1(iPhone手机浏览器)
					    b_ipad		否		b_ipad=1(iPad浏览器)
		IP去重			dedup		否		过滤今天提取过的IP，取值固定为1
		返回格式		    format		否		接口返回内容的格式，如format=jason或者format=xml
		结果分隔符
            
            

    参考链接 ：www.kuaidaili.com/genapiurl?orderid=910838254256636
"""


'''
		参数			字段          	是否必填	说明     
		订单号          	orderid		是           	查看我的订单,订单账户中有该编号
		提取数量        	num		是		普通用户：1 ~ 999; VIP/SVIP/专业版：1 ~ 9999
		所在地区        	area		否		ip所在地区, 支持按 国家/省/市 筛选; 多个地区用英文逗号分隔，如 北京,上海
		排除地区        	area_ex		否		多个地区用英文逗号分隔，如 中国,美国
		筛选端口号		port		否		多个端口号用英文逗号分隔，如 8080,18186
		排除端口号		port_ex		否		多个端口号用英文逗号分隔，如 8080,8000
		筛选IP			ipstart		否		筛选以特定部分开头的IP, 比如: 120.52.
		排除IP			ipstart_ex	否		排除以特定部分开头的IP, 比如: 120.52.
		运营商			carrier		否		0: 全部, 1: 联通/网通, 2: 电信, 3: 移动, 4: 铁通，5: 教育网，6: 阿里云
		匿名度			多选		否		多个字段可以同时复用，如an_ha=1&an_an=1
					an_ha		否		an_ha=1(高匿名代理)
					an_an		否		an_an=1(匿名代理)
					an_tr		否		an_tr=1(透明代理)
		响应速度		多选		否		多个字段可以同时复用，如sp1=1&sp3=1
					sp1		否		sp1=1(极速代理,响应速度<1秒)
					sp2		否		sp2=1(快速代理,响应速度1~3秒)
					sp3		否		sp3=1(慢速代理,响应速度>3秒)
		代理协议		protocol	否		protocol=1(筛选HTTP代理); protocol=2(筛选HTTPS代理, 同时也支持HTTP)
		POST支持		method		否		method=1(支持HTTP GET方法); method=2(支持 HTTP POST, 同时也支持GET)
		代理稳定性		quality		否		quality=1(不筛选(默认)); quality=1(VIP稳定); quality=2(SVIP专业版非常稳定);不间断地监测每个代理ip的历史数据，根据算法智能判别当前的稳定性
		结果排序		sort		否		返回的代理列表的排序方式, sort=0(默认值)，sort=1(按从快到慢响应速度排序)，sort=2(按从近到远最后检测时间排序)
		结果定制		多选		否		提取结果包含的字段,顺序排列, 英文逗号分隔)
					f_loc		否		f_loc=1(VIP/SVIP专业版提取结果包含地区信息)
					f_an		否		f_an=1(VIP/SVIP专业版提取结果包含匿名度信息)
					f_pr		否		f_pr=1(VIP/SVIP专业版提取结果包含代理协议信息,data-title="取值说明" 目前支持的协议有HTTP和HTTPS(支持HTTPS的代理ip同时也支持HTTP))
					f_sp		否		f_sp=1(VIP/SVIP专业版提取结果包含响应速度信息)
					f_fc		否		f_fc=1(专业版提取结果包含该代理的历史提取次数)
		浏览器支持		多选		否		
					b_pcchrome	否		b_pcchrome=1(谷歌浏览器)
					b_pcie		否		b_pcie=1(IE/360浏览器)
					b_pcff		否		b_pcff=1(Firefox火狐浏览器)
					b_android	否		b_android=1(安卓手机浏览器)
					b_iphone	否		b_iphone=1(iPhone手机浏览器)
					b_ipad		否		b_ipad=1(iPad浏览器)
		IP去重			dedup		否		dedup=1(过滤今天提取过的IP)
		返回格式		format		否		接口返回内容的格式，format=jason(json格式), format=xml(xml格式)
		结果分隔符		sep		否		提取结果列表中每个结果的分隔符, sep=1(\r\n分隔(默认)), sep=2(\n分隔), sep=3(空格分隔), sep=4(|分隔), 此外还支持自定义


'''

html = requests.get(url=OPEN_PROXY_TARGET_URL, headers=header, timeout=30).content
print(html)