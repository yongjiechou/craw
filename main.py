import requests
from lxml import etree

url = "https://movie.douban.com/subject/26871906/reviews?start=%d"
headers = {

    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
    'Connection': 'keep-alive',
    'Cookie': 'll="119089"; bid=RTl0_IxyCC4; ap_v=0,6.0',
    'Host': 'movie.douban.com',
    'Referer': 'https://movie.douban.com/subject/26871906/reviews?start=0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
}

if __name__ == '__main__':
    for i in range(1):
        if i == 25:
            url_climb = url % (490)
        else:
            url_climb = url % (i * 20)
        response = requests.get(url_climb, headers=headers)
        response.encoding = 'utf-8'
        text = response.text
        # with open('./cilmb.html', mode='w', encoding='utf-8') as fp:
        #     fp.write(text)
        html=etree.HTML(text)
        comments=html.xpath('//div[@class="main review-item"]')
        for comment in comments:
            author=comment.xpath("./div[@class='name']")[0].strip()
            print(author)
