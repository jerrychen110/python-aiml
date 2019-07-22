#!/usr/bin/env python
# -*- coding: utf-8 -*-


# http://toy.weather.com.cn/SearchBox/searchBox?_=1362892474803&language=zh&keyword=%E5%8C%97%E4%BA%AC

import urllib
import sys
import json

import sys
reload(sys)
sys.setdefaultencoding('utf8')

ENCODING = 'utf-8'

# 武汉天气
def queryLocation(term):
    # term = term.encode(ENCODING) if type(term) == unicode else term
    # print(term)
    url = "http://toy1.weather.com.cn/search?cityname=" + term
    resp = urllib.urlopen(url)
    result = resp.read()[1:-1]
    data = json.loads(result)
    if not data:
        print(u"找不到地点".encode(ENCODING))
    for d in data:
        ref = d["ref"]
        ref_code = ref.split("~")
        code = ref_code[0]
        break
    return code

def queryRealTimeWeatherInfo(code):
    #url = "http://m.weather.com.cn/data/%s.html" % code
    url = "http://www.weather.com.cn/data/sk/%s.html" % code
    resp = urllib.urlopen(url)
    data = json.load(resp)
    if not data:
        print(u"天气预报还没出来".encode(ENCODING))
    return data['weatherinfo']

def showRealTimeWeatherInfo(info):
    template = u"{city} {time} 天气实况: 气温{temp}℃, {WD}{WS}, 湿度{SD}"
    print template.format(**info).encode(ENCODING)


def main():
    assert len(sys.argv) >= 3
    function = sys.argv[1]
    term = ''.join(sys.argv[2:])
    if function == 'realtime':
        # 实时
        showRealTimeWeatherInfo(queryRealTimeWeatherInfo(queryLocation(term)))

if __name__ == '__main__':
    main()
