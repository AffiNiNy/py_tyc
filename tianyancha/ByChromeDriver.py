import os
import random
import sys
import time
import re
sys.path.append(os.path.split(sys.path[0])[0])

from pyquery import PyQuery as pq
from seleniumDrivers import chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tianyancha.partID import getIDObj
import tianyancha.extractMethod as methods


chromeBrowser = chrome.get_chromeBrowser()
wait = WebDriverWait(chromeBrowser, 10)
ids = getIDObj.get_idObjs()

# 股东信息部分的 ID
holderID = '#_container_holderCount'


def setLogin():
    try:
        chromeBrowser.find_element_by_xpath('//*[@id="tyc_banner_close"]').click() # 动作模仿 - 关闭弹窗
        time.sleep(1)
    except:
        pass
    # 登录/注册
    loginCSS = '.container.rel .right .tyc-nav > div:last-child > a'
    loginPart = chromeBrowser.find_element_by_css_selector(loginCSS)
    loginPart.click()
    # 密码登录
    wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, 
        '.sign-in .title-tab > div:nth-child(2)'
    )))
    chromeBrowser.find_element_by_css_selector('.sign-in .title-tab > div:nth-child(2)').click()
    # 请输入手机号
    inputPhone = chromeBrowser.find_element_by_css_selector('#TYC-login .mimadenglu .live-search-wrap > input')
    # 请输入密码
    inputPassw = chromeBrowser.find_element_by_css_selector('#TYC-login .input-warp > input')
    #Fault account
    # inputPhone.send_keys('13344405592')
    # inputPassw.send_keys('ffff59999')
    denglu = chromeBrowser.find_element_by_css_selector('.sign-in .mobile_box > .btn-primary')
    denglu.click()
    time.sleep(1)
    inputPassw.send_keys(Keys.ENTER)
    time.sleep(11)
    # 人工拉滑条....

# 切换到最新打开选项卡
def switchToNewTab():
    # 切换到当前最新打开的窗口
    if chromeBrowser.current_window_handle != chromeBrowser.window_handles[len(chromeBrowser.window_handles)-1]:
        chromeBrowser.switch_to.window(chromeBrowser.window_handles[-1])
        # handleNum = chromeBrowser.window_handles
        # if handleNum == 2:
        #     chromeBrowser.switch_to.window(chromeBrowser.window_handles[1])
        # elif handleNum == 3:
        #     chromeBrowser.switch_to.window(chromeBrowser.window_handles[2])

# 检测页面是否为搜索结果页面还是详细页面
def handleResultListPage():
    html = chromeBrowser.page_source
    doc = pq(html)
    # 检测是否包含"筛选条件"部分
    filterPart = doc('.container-left .header-block-container')
    if len(filterPart.text()) > 0 :
        print(r"**** 进入搜索结果页面 ****")
        fisrtResult = chromeBrowser.find_element_by_css_selector('#search_company_0 .content .header > a')
        fisrtResult.click()
        switchToNewTab()
    
    time.sleep(random.uniform(2, 2.5))
    # 网页往下滚动
    chromeBrowser.execute_script('window.scrollTo(0, 500)')
    time.sleep(1)

def closeOtherTabs(firstHandle):
    # Loop through until find the first handle
    for window_handle in chromeBrowser.window_handles:
        if window_handle != firstHandle:
            chromeBrowser.switch_to.window(window_handle)
            chromeBrowser.close()
            time.sleep(1)
    
    chromeBrowser.switch_to.window(firstHandle)
    time.sleep(1)

# 翻页
def get_pageCount(pqDoc, partID):
    part = pqDoc(partID)
    pager = part.find('.company_pager.pagination-warp')
    alis = pq(pager).find('li .num').items()
    maxPage = 0
    for a in alis:
        if len(a.text()) > 0:
            maxPage = a.text()
            
    return int(re.findall(r"\d{1,4}", maxPage)[0])

# table 翻页
def click_listNextPage(containerID):
    # nextBtn = chromeBrowser.find_element_by_css_selector(containerID + ' .company_pager.pagination-warp .num.-next')
    nextBtn = wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, 
        containerID + ' .company_pager.pagination-warp .num.-next'
    )))
    nextBtn.click()
    # 用 table 中的 tr 定位
    wait.until(EC.presence_of_all_elements_located((
        By.CSS_SELECTOR, 
        containerID + ' > .table > tbody > tr'
    )))
    # 等待最后一行的 "详情" 链接可用
    wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, 
        containerID + ' > .table > tbody > tr:last-child > td:nth-child(9) > a'
    )))

# 企业简介、工商信息、股东信息、主要人员(高管信息)、核心团队、企业业务、招聘信息、资质证书、招投标、软件著作权 保存到excel
def mainProcess(doc):
    print(r'**** 进入主要处理 ****')

    # 招聘信息
    # maxPage = get_pageCount(doc, ids.recruitID) 
    # print('maxPage: ', maxPage)
    # recruitHeader = methods.get_recruitHeader(doc)
    # print('header: ', recruitHeader)
    # dataList = methods.get_recruitInfos(doc)
    # if maxPage > 1:
    #     for i in range(1, 3): # range(1, maxPage)
    #         click_listNextPage(ids.recruitID)
    #         time.sleep(random.uniform(1.5, 2.3)) # 列表翻页后等待
    #         nextPageList = methods.get_recruitInfos(doc)
    #         if len(nextPageList) > 0:
    #             dataList.append(nextPageList)

    bidsMaxPage = get_pageCount(doc, ids.bidsID)
    print('bidsMaxPage: ', bidsMaxPage)
    header = methods.get_bidHeader(doc)
    print('bidHeader: ', header)
    
    dataList = methods.get_bidInfos(doc, chromeBrowser)
    print('first page: ', dataList)

    click_listNextPage(ids.bidsID)
    time.sleep(random.uniform(1.5, 2.3)) # 列表翻页后等待
    newPageSrc = chromeBrowser.page_source
    doc = pq(newPageSrc)
    nextPageList = methods.get_bidInfos(doc, chromeBrowser)
    if len(nextPageList) > 0:
        dataList.append(nextPageList)

    print('two pages: ', dataList)



if __name__ == '__main__':
    url = "https://www.tianyancha.com/"
    chromeBrowser.get(url)
    time.sleep(2.5)
    setLogin()

    # Store the ID of the original window
    search_window = chromeBrowser.current_window_handle
    
    comList = ['阿里巴巴']
    for com in comList:
        try:
            inputBox = wait.until(EC.element_to_be_clickable((
                By.ID, 'home-main-search'
            )))
        except:
            inputBox = wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR, 
                '.input-group.search-group.company .input.-sm.js-live-search-auto'
            )))
        inputBox.clear()
        inputBox.send_keys(Keys.CONTROL + 'a')
        inputBox.send_keys(com)
        # time.sleep(random.uniform(2, 2.5))
        inputBox.send_keys(Keys.ENTER)
        time.sleep(3)
        handleResultListPage()
        
        # 删除右侧组件 <div class="back_to_top_container">
        chromeBrowser.execute_script("$('.back_to_top_container').remove()")
        # 提取信息
        pageSource = chromeBrowser.page_source
        doc = pq(pageSource)
        mainProcess(doc)

        # closeOtherTabs(search_window)