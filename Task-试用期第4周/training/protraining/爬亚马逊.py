# 爬取亚马逊商品页面
import requests

url = "http://www.amazon.cn/gp/product/B01M8L5Z3Y"

try: 
    r = requests.get(url, headers = {'user-agent':'Mozilla/5.0'})
    r.raise_for_status() # 如果状态不是200,引发HTTPError异常
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取失败")