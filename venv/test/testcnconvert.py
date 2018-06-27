# -*- coding: UTF-8 -*-
#小猪短租爬取
import requests
from BeautifulSoup import BeautifulSoup
import json
def get_xinxi(i):
    url = 'http://hotel.qunar.com/city/huhehaote/dt-4868/'
    html = requests.get(url)

    print json.dumps(html.content).decode("unicode-escape")
    '''
    soup = BeautifulSoup(html.content)
    #获取地址
    dizhis=soup.select(' div > a > span')
    #获取价格
    prices = soup.select(' span.result_price')
    #获取简单信息
    ems = soup.select(' div > em')
    datas =[]
    for dizhi,price,em in zip(dizhis,prices,ems):
        data={
            '价格':price.get_text(),
            '信息':em.get_text().replace('\n','').replace(' ',''),
            '地址':dizhi.get_text()
        }
        print(json.dumps(data).decode("unicode-escape"))
    '''
get_xinxi(1)
