#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import re
import time
import json
from urllib.parse import quote
from bs4 import BeautifulSoup
s = requests.Session()
r = s.get("http://www.ahyycg.cn/NoticeBoard/YP_2014_NiBid.aspx")

string1 = re.findall(r'id="__VIEWSTATE" value="(.*)"',r.text)
string2 = re.findall(r'id="__VIEWSTATEGENERATOR" value="(.*)"',r.text)
string3 = re.findall(r'id="__EVENTVALIDATION" value="(.*)"',r.text)
pagenum = 2

print("分割线".center(80,'-'))

header = {
    'Content-Type':'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0',
    'Referer':'http://www.ahyycg.cn/NoticeBoard/YP_2014_NiBid.aspx',

    }

seq = "__VIEWSTATE="+quote(str(string1[0]), safe='')+"&"+\
      "__VIEWSTATEGENERATOR="+quote(str(string2[0]), safe='')+ "&" + \
       "__EVENTTARGET=ctl00%24ContentPlaceHolder1%24pager1"+ "&" + \
       "__EVENTARGUMENT="+str(pagenum)+ "&" + \
       "__EVENTVALIDATION="+quote(str(string3[0]), safe='')+ "&" + \
       "input="+ "&" + \
       "input="+ "&" + \
       "ctl00%24ContentPlaceHolder1$txtGoodsID="+ "&" + \
       "ctl00%24ContentPlaceHolder1$txtPack="+ "&" + \
       "ctl00%24ContentPlaceHolder1$txtComSC="+ "&" + \
       "ctl00%24ContentPlaceHolder1$txtProductName="+ "&" + \
       "ctl00%24ContentPlaceHolder1$txtMedicineModel="+ "&" + \
       "ctl00%24ContentPlaceHolder1$txtOutlookc="

r = s.post(url="http://www.ahyycg.cn/NoticeBoard/YP_2014_NiBid.aspx",headers=header,data=seq)
m=r.content.decode("utf-8")

soup=BeautifulSoup(m,"html.parser")
# 多属性爬
table=soup.find("table",{"class":"mainlist","id":"ctl00_ContentPlaceHolder1_gvwAppraiseInfo"})
# 继续爬
print(table)
