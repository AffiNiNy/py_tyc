import os
from pyquery import PyQuery as pq

path = os.getcwd() + '\website_info\html\\bids'
kw1 = '联合体'
dir = os.listdir(path)

def putData(data, ctList):
    try:
        ctList.index(data)
    except:
        ctList.append(data)
    return ctList


for e in dir:
    if e.endswith('.html'):
        print(e)
        comList = []
        filePath = path + '\\' + e

        with open(filePath, 'rb') as f:
            rd = f.read().decode()
            hasKeyword = rd.find(kw1)
            
            if hasKeyword >= 0: #处理联合体供应商
                c1 = pq(rd).children()
                for each in c1:
                    childCtx = pq(each).text()
                    if childCtx.find(kw1) > 0:
                        cSplit = childCtx.split('\n')
                        gen = (cCtx for cCtx in cSplit if cCtx.find(kw1) > 0)
                        for g in gen:
                            tarText = g.replace(' ','').strip()
                            putData(tarText, comList)
                        print('联合体 list: ', comList)
            else:
                doc = pq(rd)
                atags = doc.find('.js-full-container > a').items()
                for a in atags:
                    comName = pq(a).text()
                    putData(comName, comList)
                print('非联合体 list: ', comList)

        print('---------------------------------End file---------------------------------')