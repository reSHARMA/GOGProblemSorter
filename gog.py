#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
from pprint import pprint
import string
import time
import sys
def run(cat,page):
    headers = {}
    headers['Accept'] = \
        'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    headers['Accept-Encoding'] = 'gzip, defalte'
    headers['Connection'] = 'keep-alive'
    headers['User-Agent'] = \
        'Mozilla/5.0 (X11; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0'
    print("[")
    for x in range(1,page + 1):
        with urllib.request.urlopen("https://www.geeksforgeeks.org/category/"+ cat +"/page/" + str(x)  +"/") as conn:
            rr=conn.read()
        a = BeautifulSoup(rr,'html.parser')
        b = a.select("article")
        for y in b:
            rate = 0
            print('{ "head" : "' + (y.select(".entry-title > a"))[0].text + '",')
            print(' "link" : "<a target=\'_blank\' href = \'' + (y.select(".entry-title > a"))[0]['href']  +'\'> Go to question </a>",')
            xx = y.select(".articleRating")
            for nn in xx:
                rate = float(nn.text)
            if x == page and y == b[-1]:
                print(' "rate" : "' + str(rate) + '"}')
            else:
                 print(' "rate" : "' + str(rate) + '"},')
    print("]")

cat = sys.argv[1]
page = sys.argv[2]
run(cat,int(page))
