import os
from pyquery import PyQuery as pq


# 企业简介
def get_companyInfo(doc):
    comIntroduce = doc('.summary.mt8 .detail-content')
    rElem = comIntroduce.find('.label').text()
    comIntroduce.find('span').remove()
    print(rElem, comIntroduce.text())

# 工商信息 Industrial and commercial
def get_ICInfo(doc):
    icInfos = doc('#_container_baseInfo tbody')
    trs = icInfos.children()
    # tr 行计数
    trCnt = 0

    for td in trs:
        tds = pq(td).children()
        if trCnt == 0:
            print(tds[0].text, pq(tds[1]).find('a').text()) # 法定代表人
            print(tds[2].text, tds[3].text) # 经营状态
            print(tds[4].text, pq(tds[5])('.sort-score-value').text()) # 天眼评分
        elif trCnt == 1:
            print(tds[0].text, tds[1].text) # 成立日期
        elif trCnt == 2:
            print(tds[0].text, tds[1].find('div').text) # 注册资本
        elif trCnt == 6:
            print(tds[0].text, tds[1].text) # 企业类型
            print(tds[2].text, tds[3].text) # 行业
            print(tds[4].text, tds[5].text) # 人员规模
        elif trCnt == 8:
            print(tds[0].text, tds[1].find('span').text) # 曾用名
            print(tds[2].text, tds[3].find('span').text) # 英文名称
        elif trCnt == 9:
            print(tds[0].text, tds[1].find('span').text) # 注册地址
        elif trCnt == 10:
            print(tds[0].text, tds[1].find('span').text) # 经营范围
        trCnt += 1


holderID = '#_container_holderCount'
# 股东信息
def get_holderInfo(doc):
    thCnt = 0
    # 表头及数量
    holderTitle = doc('#nav-main-holderCount .data-title')
    holderCount = doc('#nav-main-holderCount .data-count')
    print(holderTitle.text(), holderCount.text())

    holderHeader = doc(holderID + ' .table thead tr > th')
    
    for h in holderHeader:
        t = h.text
        if thCnt == 1:
            tempHeader = pq(h).remove('span')
            print(tempHeader.text())
        elif thCnt == 4:
            tempHeader = pq(h)('.child-span').remove('div')
            print(tempHeader.text())
        else:
            print(t)
        thCnt += 1

    pages = get_pageCount(holderID)

    trs = doc(holderID + ' .table > tbody').children()
    # print('len(trs): ', len(trs))
    for tr in trs:
        tds = pq(tr).children()
        for i in range(len(tds)):
            td = pq(tds[i])
            if i == 0:
                serialNum = td.text()
                print(serialNum)
            elif i == 1:
                holderName = td('.table-toco .link-click.name-max').text()
                print(holderName)
            elif i == 3:
                print(td.find('span').text().split(' ')[0])
            else:
                print(td.find('span').text())


# 翻页
def get_pageCount(cssIdSelector):
    part = doc(cssIdSelector)
    pager = part.find('.company_pager.pagination-warp')
    alis = pq(pager).find('li .num').items()
    maxPage = 0
    for a in alis:
        if len(a.text()) > 0:
            maxPage = a.text()
    
    return int(maxPage)


if __name__ == '__main__':
    filePath = 'D:\DEVELOP\VSCode_Projects\ALittlePythonProg\website_info\html\\tyc\广东引道信息技术有限公司_电话_工商信息_风险信息_嗨皮出行 - 天眼查.html'
    # filePath = 'D:\DEVELOP\VSCode_Projects\ALittlePythonProg\website_info\html\\tyc\天眼查-商业查询平台_企业信息查询_公司查询_工商查询_企业信用信息系统.html'
    with open(filePath, "r", encoding='utf8') as f:
        str = f.read()
    
    doc = pq(str)
    print(type(doc))
    # nextBtn = doc(holderID + ' .company_pager.pagination-warp .num.-next')
    # print(nextBtn)

    get_companyInfo(doc)
    # get_ICInfo(doc)
    # get_holderInfo(doc)
