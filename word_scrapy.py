import requests
from lxml import etree

words = []
with open("words.txt","r")as fp:
    lines = fp.readlines()
    for line in lines:
        line = line.strip()
        if len(line) > 0:
            words.append(line)

fp = open("dictionary.txt","w",encoding="utf-8")
count = 0
for word in words:
    url = 'http://dict.cn/' + word
    r = requests.get(url)

    html = etree.HTML(r.text)
    tree = etree.ElementTree(html)

    #print("="*80)
    ls1 = tree.xpath('//*[@class = "dict-basic-ul"]/li/span')
    ls2 = tree.xpath('//*[@class = "dict-basic-ul"]/li/strong')
    tmp = ""
    for i in range(len(ls1)):
        tmp += ls1[i].text + ls2[i].text
    count += 1
    #tmp.encode('utf-8').decode('unicode_escape')
    print("[{}/{}]{}:{}".format(count,len(words),word,tmp))
    fp.write("[{}]{}\n".format(word,tmp))
