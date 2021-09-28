import os
import sys
import time
sys.path.append(os.path.split(sys.path[0])[0])
from tianyancha.partID import getIDObj
from pyquery import PyQuery as pq

ids = getIDObj.get_idObjs()
curYear = time.localtime(time.time()).tm_year

# 企业简介、工商信息、股东信息、主要人员、核心团队、企业业务、招聘信息、资质证书、招投标、软件著作权
# 企业简介 .summary.mt8 .detail-content
# 工商信息 #_container_baseInfo
# 股东信息 holderID
# 主要人员 staffID
# 核心团队 mainTeamID
# 企业业务 firmProductID
# 招聘信息 recruitID   2年 改成 3 年
# 资质证书 certificateID
# 招投标 bidsID 5年 详情页面主要类名: lawsuitcontent bidcontent link-warp
# 软件著作权 copyrightID 3 年

def get_commonHeader(doc, containerID):
    header = []
    holderHeader = doc(containerID + ' .table thead tr > th')
    for i in range(holderHeader.size()):
        header.append(holderHeader[i].text)
    return header

def get_shortHeader(doc, containerID):
    header = []
    holderHeader = doc(containerID + ' .table > thead > tr').children()
    for i in range(holderHeader.size() - 1):
        header.append(holderHeader[i].text)

    return header

# 企业简介
def get_companyInfo(doc):
    comIntroduce = doc('.summary.mt8 .detail-content')
    rElem = comIntroduce.find('.label').text()
    comIntroduce.find('span').remove()
    return comIntroduce.text()

# ['股东信息', 数量]
def get_holderTitile(doc):
    """
    ['股东信息', 数量]
    """
    h = []
    h.append(doc('#nav-main-holderCount .data-title').text())
    h.append(doc('#nav-main-holderCount .data-count').text())
    
    return h

# 股东信息表头
def get_holderHeader(doc):
    header = []
    holderHeader = doc(ids.holderID + ' .table thead tr > th')
    
    for i in range(holderHeader.size()):
        currentHeader = ''
        h = holderHeader[i]
        if i == 1:
            currentHeader = pq(h).remove('span').text()
        elif i == 4:
            currentHeader = pq(h)('.child-span').remove('div').text()
        else:
            currentHeader = h.text
        header.append(currentHeader)
    
    return header

# 股东信息列表
def get_holderInfos(doc):
    infosList = []
    trs = doc(ids.holderID + ' .table > tbody').children()
    for tr in trs:
        dataList = []
        tds = pq(tr).children()
        for i in range(len(tds)):
            td = pq(tds[i])
            if i == 0:
                serialNum = td.text()
                dataList.append(serialNum)
            elif i == 1:
                holderName = td('.table-toco .link-click.name-max').text()
                dataList.append(holderName)
            elif i == 3:
                dataList.append(td.find('span').text().split(' ')[0])
            else:
                dataList.append(td.find('span').text())
        infosList.append(dataList)
    
    return infosList

# 主要人员表头
def get_staffHeader(doc):
    return get_commonHeader(doc, ids.staffID)
        
# 主要人员列表
def get_staffInfos(doc):
    infosList = []
    trs = doc(ids.staffID + ' .table > tbody').children()
    for tr in trs:
        dataList = []
        tds = pq(tr).children()
        for i in range(len(tds)):
            td = pq(tds[i])
            if i == 1: # 姓名
                dataList.append(td.find('.table-toco > tbody > tr > td:nth_child(2) > a').text())
            elif i == 2: # 职位
                dataList.append(td.find('span').text())
            else:
                dataList.append(td.text())
        infosList.append(dataList)
    
    return infosList

# 核心团队表头
def get_mainTeamHeader(doc):
    return get_commonHeader(doc, ids.mainTeamID)

# 核心团队列表
def get_mainTeamInfos(doc):
    infosList = []
    trs = doc(ids.mainTeamID + ' .table > tbody').children()
    for tr in trs:
        dataList = []
        tds = pq(tr).children()
        for i in range(len(tds)):
            td = pq(tds[i])
            if i == 1: # 姓名
                dataList.append(td.find('.table-toco > tbody > tr > td:nth_child(2) > a').text())
            elif i == 3: # 简介
                dataList.append(td.find('.detail-content').text())
            else:
                dataList.append(td.text())
        infosList.append(dataList)
    
    return infosList

# 企业业务表头
def get_firmProdHeader(doc):
    return get_commonHeader(doc, ids.firmProductID)

# 企业业务列表
def get_firmProdInfos(doc):
    infosList = []
    trs = doc(ids.firmProductID + ' .table > tbody').children()
    for tr in trs:
        dataList = []
        tds = pq(tr).children()
        for i in range(len(tds)):
            td = pq(tds[i])
            if i == 1: # 产品名称
                dataList.append(td.find('.lazy-img > tbody > tr > td:nth_child(2) > a').text())
            elif i == 4: # 产品标签
                dataList.append(td.find('.link-click').text())
            elif i == 6: # 产品介绍
                dataList.append(td.find('.detail-content').text())
            else:
                dataList.append(td.text())
        infosList.append(dataList)
    
    return infosList

# 招聘信息表头
def get_recruitHeader(doc):
    return get_shortHeader(doc, ids.recruitID)

# 招聘信息列表
def get_recruitInfos(doc):
    infosList = []
    trs = doc(ids.recruitID + ' > .table > tbody').children()
    for tr in trs:
        dataList = []
        tds = pq(tr).children()
        if curYear - int(tds[1].text.split('-')[0]) > 3:
            break
        for i in range(len(tds) - 1):
            td = pq(tds[i])
            dataList.append(td.text())
        infosList.append(dataList)

    return infosList

# 资质证书表头
def get_certificateHeader(doc):
    return get_shortHeader(doc, ids.certificateID)

# 资质证书列表
def get_certificateInfos(doc):
    infosList = []
    trs = doc(ids.certificateID + ' .table > tbody').children()
    for tr in trs:
        dataList = []
        tds = pq(tr).children()
        for i in range(len(tds) - 1):
            td = pq(tds[i])
            if i == 0:
                dataList.append(td.text())
            else:
                dataList.append(td.find('span').text())
        infosList.append(dataList)

    return infosList

# 招投标表头
def get_bidHeader(doc):
    return get_shortHeader(doc, ids.bidsID)

# 招投标列表
def get_bidInfos(doc):
    infosList = []
    trs = doc(ids.bidsID + ' > .table > tbody').children()
    for tr in trs:
        dataList = []
        tds = pq(tr).children()
        if curYear - int(tds[1].text.split('-')[0]) > 5:
            break
        for i in range(len(tds) - 1):
            tdText = pq(tds[i]).text()
            dataList.append(tdText)
            if i == 4:
                bidType = tdText
            elif i == 5:
                buyer = tdText
            elif i == 6:
                supplier = tdText
            elif i == 7:
                bidMoney = tdText
            
        infosList.append(dataList)

    return infosList

# 软件著作权表头
# 软件著作权列表



if __name__ == '__main__':
    filePath = 'D:\DEVELOP\VSCode_Projects\ALittlePythonProg\website_info\html\\tyc\阿里巴巴（中国）网络技术有限公司_电话_工商信息_风险信息_阿里巴巴 - 天眼查.html'
    # filePath = 'D:\DEVELOP\VSCode_Projects\ALittlePythonProg\website_info\html\\tyc\天眼查-商业查询平台_企业信息查询_公司查询_工商查询_企业信用信息系统.html'
    with open(filePath, "r", encoding='utf8') as f:
        str = f.read()
    
    doc = pq(str)
    print(get_bidHeader(doc))
    # print('infos: ', get_bidInfos(doc))
    l = get_bidInfos(doc)
    for e in l:
        print(e)