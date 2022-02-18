import requests
import json
lists = json.load(open("words.json","r"))
words = []
for k in lists.keys():
    words.extend([i.strip() for i in lists[k].split(",")])
words = set(words)
print(len(words))
def download(word):
    word = word.strip()
    if word == "":
        pass
    else:
        url = "http://dict.youdao.com/dictvoice?audio=" + word.replace(" ","+")
        try:
            f = requests.get(url)
            with open("MP3/{}.mp3".format(word.replace(" ","_")),"wb") as fp:
                fp.write(f.content)
        except:
            print(word)
count = 0
for word in words:
    print(count+1)
    count += 1
    download(word)