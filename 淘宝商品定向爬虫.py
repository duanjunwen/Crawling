'''
1.提交商品搜索请求，循环获取页面
2.对于每个页面，提取商品名称和价格信息
3.将信息输出到屏幕上
'''
import requests
import re

def getHTMLText(url):
    try:
        kv = {    'authority': 'www.taobao.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    'sec-fetch-dest': 'iframe',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'referer': 'https://www.taobao.com/?spm=a230r.1.0.0.1dd868b8xPNoBx',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cookie': 'miid=1527960904344275438; thw=cn; cna=P/j5FoOItXsCAXVXzYhM1G6g; v=0; cookie2=19a46230dbfdf004bc04940967b817cb; t=b5010581611be150a55e285f25b4826a; _tb_token_=5338b683de319; _samesite_flag_=true; sgcookie=EV6LHW84OL0Ge%2F5Gm1jCy; uc3=nk2=G5ptEks%3D&lg2=W5iHLLyFOGW7aA%3D%3D&id2=UUBRc3t8pkVPoQ%3D%3D&vt3=F8dBxd9hjDitkqAvX4A%3D; csg=22916bf3; lgc=xzdjw; dnk=xzdjw; skt=1bbc2fe230674214; existShop=MTU4NTExOTE4MA%3D%3D; uc4=nk4=0%40GSn6sXiEnmxR%2Fj%2F0ya6qMg%3D%3D&id4=0%40U2LDbVzY5y91bFyi9x60HHFQnoPT; tracknick=xzdjw; _cc_=UtASsssmfA%3D%3D; tg=0; enc=FXYHLTkplWk3BVQGyLg8kE4ilSDdwbrzajAEOt%2BWSRju5aggVjuKN0U01E%2FQIQu0bTR%2F6Hgf1%2B5UltVHk9WxHQ%3D%3D; tfstk=c2rhBQiUOyuCMsLyleiQe4RdmiehamQEOurabko3PIliMpZZLsbB7EuP6OcLtuL5.; mt=ci=1_1; hng=CN%7Czh-CN%7CCNY%7C156; l=dBETZNhnqkFcPEW_BOfi-AoG-__tqIOb4sPy7D5usICPOWCH5WSOWZ4gCs8MCnMVh6AeJ353T9A8BeYBq6CKnxvtIosM_nMmn; uc1=cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&existShop=false&cookie21=VFC%2FuZ9ainBZ&tag=8&lng=zh_CN&pas=0&cookie14=UoTUP2OZ5zhAug%3D%3D&cookie15=V32FPkk%2Fw0dUvg%3D%3D; isg=BMbGpRm35Kouy7OEzTp7jVtpF7xIJwrhLqpC9rDvsunEs2bNGLda8axFj_9_GwL5',
    'if-none-match': 'W/"2c65-1602480f459"', }
        r = requests.get(url,timeout = 30,headers = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(ilt,html):    #解析获得的页面 lit为结果列表类型
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html) #\表示引入“view_price”":",获取\d\.形成的相关信息，获得的所有信息保存在plt列表中
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html) #匹配“raw title”，“”作为值的键值对
        for i in range(len(plt)): #len函数返回对象长度
            price = eval(plt[i].split(':')[1]) #对price信息进行提取，去掉view price字段只获取价格，split对plt进行分割切片以':'为分隔
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title]) #append用于在ilt列表后添加对象
    except:
         print("")
def printGoodList(ilt):
    tplt = "{:4}\t{:8}\t{:16}" #设计打印模板第一个位置长度为4第二个为8
    print(tplt.format("序号","价格","商品名称")) #打印输出信息的表头
    count = 0 #定义输出信息的计数器
    for g in ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1])) #count表示商品的序号，g0表示商品的价格，g1表示商品的名称
    print("")
def main():
    goods = "书包"
    depth = 2   #访问深度 2指访问第一第二个页面
    start_url = "https://s.taobao.com/search?q=" + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + "&s=" + str(44*1) #每一个页面起始值s，s以44为倍数
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue

    printGoodList(infoList)

main()
