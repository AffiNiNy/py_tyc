import os
import re
import sys
import time

from selenium.webdriver.chrome.webdriver import WebDriver
sys.path.append(os.path.split(sys.path[0])[0])
from tianyancha.partID import getIDObj
from pyquery import PyQuery as pq
from seleniumDrivers import chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

ids = getIDObj.get_idObjs()
curYear = time.localtime(time.time()).tm_year
# 招标金额的正则式
pattern = '(\d{1,3},)+\d{2,3}\.\d{2,3}'


# 企业简介、工商信息、股东信息、主要人员、核心团队、企业业务、招聘信息、资质证书、招投标、软件著作权

def get_selfName(doc):
    return doc('#company_web_top .box.-company-box > .content .header .name').text()

# 通用表头
def get_commonHeader(doc, containerID):
    header = []
    holderHeader = doc(containerID + ' .table thead tr > th')
    for i in range(holderHeader.size()):
        header.append(holderHeader[i].text)
    return header

# 短表头
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

# 股东数量
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

# chromeBrowser = chrome.get_chromeBrowser()
# 招投标列表
def get_bidInfos(doc, chromeBrowser):
    infosList = []
    comSelfName = get_selfName(doc)
    containerID = ids.bidsID
    trs = doc(containerID + ' > .table > tbody').children()
    for trIdx in range(len(trs)):
        dataList = []
        tds = pq(trs[trIdx]).children()
        if curYear - int(tds[1].text.split('-')[0]) > 5: # 获取 5 年内招投标
            break
        
        nextTrFlag = False
        recordFullDocFlag = False
        findBidMoneyFlag = False
        for i in range(len(tds) - 1):
            tdText = pq(tds[i]).text()
            dataList.append(tdText)
            if i == 4 and tdText == '招标': # 招标类型
                nextTrFlag = True
                break
            elif i == 5: # 采购人
                buyer = tdText
                if buyer == '-':
                    nextTrFlag = True
                    break
            elif i == 6: # 供应商
                supplier = tdText
                if supplier == '-':
                    recordFullDocFlag = True
            elif i == 7: # 中标金额
                bidMoney = tdText
                if bidMoney == '-':
                    findBidMoneyFlag = True
        if nextTrFlag:
            continue

        wait = WebDriverWait(chromeBrowser, 12)
        detailBtn = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            containerID + ' .table > tbody > tr:nth-child('+str(trIdx + 1)+') > td:nth-child(9)'
        )))
        detailBtn.click()
        time.sleep(1)

        # 打开招投标详情页面获取其它供应
        wait = WebDriverWait(chromeBrowser, 12)
        detailPage = wait.until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, '#tyc_banner_left'
        )))
        doc = pq(chromeBrowser.page_source)
        supplierList = get_suppliersInfos(doc, [comSelfName, buyer])
        if len(supplierList) > 0:
            dataList[6] = supplierList

        # table缺失信息
        if findBidMoneyFlag:
            bmResult = re.search(pattern, doc.text())
            if bmResult != None:
                dataList[7] = bmResult.group()
        # if recordFullDocFlag:
        #     dataList.append(doc(ids.bidDetailID).text())
        
        infosList.append(dataList)
        chrome.closeLastTab(chromeBrowser)

    return infosList

# 详情 - 所有供应商
def get_suppliersInfos(doc, excludeList):
    comsID = ids.relatedComID
    otherSuppList = []

    spanATagList = doc(comsID + ' > a').items()
    for a in spanATagList:
        curComName = a.text()
        if filt_companyName(curComName, excludeList):
            otherSuppList.append(curComName)

    return otherSuppList

# 在关联公司中筛选不要的公司名
def filt_companyName(curComName, excludeList):
    if excludeList.count(curComName) > 0:
        return False
    if curComName.find('招标') > -1 or curComName.find('咨询') > -1:
        return False
    
    return True

# 软件著作权表头
# 软件著作权列表



if __name__ == '__main__':
    lenovoPath = 'D:\VSCode_Projects\py_tyc'
    xpsPath = 'D:\DEVELOP\VSCode_Projects\ALittlePythonProg'
    if 1 == 1:
        fileHeader = lenovoPath
    else:
        fileHeader = xpsPath
    
    filePath = fileHeader + '\website_info\html\\tyc\阿里巴巴（中国）网络技术有限公司_电话_工商信息_风险信息_阿里巴巴 - 天眼查.html'
    # with open(filePath, "r", encoding='utf8') as f:
    #     str = f.read()
    #     selfName = get_selfName(pq(str))
    #     print('selfName', selfName)
    
    # filePath = fileHeader + '\website_info\html\\bids\广东省住房和城乡建设厅省住房城乡建设厅注册类相关系统整合及数据治理（一期）项目（运营部分）成交结果公告_招投标信息查询 - 天眼查.html'
    # filePath = fileHeader + '\website_info\html\\bids\东莞市智慧招商综合地理信息系统升级改造项目中标（成交）结果公告_招投标信息查询 - 天眼查.html'
    with open(filePath, "r", encoding='utf8') as f:
        str = f.read()

    doc = pq(str)
    # 测试招投标详情页面
    # l = get_suppliersInfos(doc, ['奥格科技股份有限公司'])
    # print(l)

    print(get_holderInfos(doc))
    # print('infos: ', get_bidInfos(doc, chromeBrowser))
    # l = get_bidInfos(doc, chromeBrowser)
    # for e in l:
    #     print(e)
    # chromeBrowser.close()