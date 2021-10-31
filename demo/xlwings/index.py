# -*- coding: utf-8 -*-

import datetime
import os
import sys
import time
import xlwings as xw
sys.path.append(os.getcwd())
from myio.xlwings.SelfXlwings import *
from myio.xlwings.formatMethods import *

dateFormat = 'yyyy"年"m"月"d"日"'
curYear = time.localtime(time.time()).tm_year
selfxw = SelfXlwings()
wb = selfxw.new_xlsx()
comIntroSht = wb.sheets[0]
comIntroSht.name = '公司简介'

projectsSht = wb.sheets.add('招投标', after=comIntroSht)

recruitSht = wb.sheets.add('招聘信息', after=projectsSht)


# 公司主要信息
formatHeader_comInfo(comIntroSht)

# 值
comIntroSht.range('A3').value = '航天精一（广东）信息科技有限公司'
comIntroSht.range('F3').value = '有限责任公司'
comIntroSht.range('I3').value = '2002/3/5'
comIntroSht.range('I3').number_format = dateFormat
comIntroSht.range('K3').value = '724.6'
comIntroSht.range('M3').value = '董石峰'
comIntroSht.range('O3').value = '专业从事研发、时空数据分析及挖掘、测绘服务、地理信息数据采集/处理及应用系统开发'
comIntroSht.range('S3').value = '公共安全（公安、武警、边海防）、安监、疾控等政府机关'
comIntroSht.range('F4').value = r'阿里巴巴（Alibaba.com）是全球企业间（B2B）电子商务的著名品牌，是全球国际贸易领域内最大、最活跃的网上交易市场和商人社区。　　良好的定位，稳固的结构，优秀的服务使阿里巴巴成为全球首家拥有超过800万网商的电子商务网站，遍布220个国家和地区，每日向全球各地企业及商家提供810万条商业供求信息，成为全球商人网络推广的首选网站，被商人们评为“最受欢迎的B2B网站”。　　杰出的成绩使阿里巴巴受到各界人士的关注。WTO首任总干事萨瑟兰出任阿里巴巴顾问，美国商务部、日本经济产业省、欧洲中小企业联合会等政府和民间机构均向本地企业推荐阿里巴巴。　　阿里巴巴两次入选哈佛大学商学MBA案例，在美国学术界掀起研究热潮；连续五次被美国权威财经杂志《福布斯》选为全球最佳B2B站点之一；多次被相关机构评为全球最受欢迎的B2B网站、中国商务类优秀网站、中国百家优秀网站、中国最佳贸易网。被国内外媒体、硅谷和国外风险投资家誉为与Yahoo、Amazon、eBay、AOL比肩的五大互联网商务流派代表之一。　　2003年5月，阿里巴巴投资1亿人民币推出个人网上交易平台淘宝网（Taobao.com），致力打造全球最大的个人交易网站，2004年7月，又追加投资3.5亿人民币。截至2005年7月10日，淘宝网在线商品数量超过800万件、网页日浏览量突破9000万、注册会员数突破760万、2005年二季度成交额达16.5亿人民币，遥遥领跑中国个人电子商务市场。在全球权威Alexa2004年排名中，淘宝网在全球网站综合排名中位居前20名，中国电子商务网站排名第1名。'

selfxw.formatHeader_shareHolders(comIntroSht)
l = [['1', 'aaa', '57.59%', '69%', '1234d', '2020/04/04'], ['2', 'bbb', '57.59%', '69%', '1234d', '2020/04/04']]
selfxw.fill_holdersInfo(comIntroSht, l)

selfxw.formatHeader_mainStaff(comIntroSht)
l2 = [['1','AAAS','CCC','-','-'],['2','BB','DD','0','-'],['3','EI','IE','-','-']]
selfxw.fill_mainStaffInfo(comIntroSht, l2)

selfxw.formatHeader_mainTeam(comIntroSht)
l3 = [['1','caj','ceo','asdfasdfasdf'], ['2','jie','ddo','erererererererere']]
selfxw.fill_mainTeamInfo(comIntroSht, l3)

selfxw.formatHeader_firmProd(comIntroSht)
l4 = [['1','铴在','1999/9/9','dddf','sdf','qwer','ouk']]
selfxw.fill_firmPordInfo(comIntroSht, l4)

fileTail = datetime.datetime.now().strftime('%Y-%m-%d')
wb.sheets[0].activate()
wb.save(r'D:\\VSCode_Projects\\py_tyc\demo\\output_Excel_' + fileTail + '.xlsx')
wb.close()
# wb.save(r'D:\DEVELOP\\VSCode_Projects\ALittlePythonProg\demo\\output_Excel.xlsx')
# wb.save()

selfxw.kill()



# ###  招投标
# yearDiff = curYear - 5
# bidsTitleRange = projectsSht.range('A1:H1')
# selfxw.formatTitle(bidsTitleRange, '中标项目(%s-至今)' % yearDiff)

# cA2 = projectsSht.range('A2')
# cA2.value = '公司名称'
# cACols = projectsSht.range('A3:A30')
# cACols.value = '公司名称|公司名称|公司名称'
# cACols.column_width = 14.5
# cACols.merge()
# cACols.font.size = 18
# cACols.font.bold = True
# cACols.wrap_text = True

# cB2 = projectsSht.range('B2')
# cB2.value = '项目名称'
# cB2.column_width = 60
# cC2 = projectsSht.range('C2')
# cC2.value = '中标时间'
# cC2.column_width = 17
# cD2 = projectsSht.range('D2')
# cD2.value = '中标金额\r\n(万元)'
# cD2.column_width = 14
# cE2 = projectsSht.range('E2')
# cE2.value = '招标单位'
# cE2.column_width = 32.5
# cF2 = projectsSht.range('F2')
# cF2.value = '其它投标供应商'
# cF2.column_width = 32.5
# cG2 = projectsSht.range('G2')
# cG2.value = '项目省份/城市'
# cG2.column_width = 19
# cH2 = projectsSht.range('H2')
# cH2.value = '备注'
# cH2.column_width = 66.5
# proTableHeader = projectsSht.range('A2:H2')
# selfxw.formatHeader(proTableHeader)
# # 值
# startCell = endCell = 3
# projectsSht.range('B%s' % startCell).value = '江苏省政府采购中心关于[江苏省公安厅警务地理平台升级改造]\r\nJSZC-G2020-382项目'
# projectsSht.range('C3').value = '2021/6/17'
# projectsSht.range('C3').number_format = dateFormat
# projectsSht.range('D3').value = '7390000'
# projectsSht.range('D3').number_format = '#,###'
# projectsSht.range('E3').value = '普宁市公安局'
# projectsSht.range('F3').value = '奥格科技股份有限公司\r\n广东南方数码科技股份有限公司\r\n广州城市信息研究所有限公司'
# projectsSht.range('G3').value = '广东揭阳市'
# projectsSht.range('H3').value = '/'

# rowValues = projectsSht.range('A1:H%s'%(startCell))
# print('address', rowValues.address)
# print('get_address', rowValues.get_address())
# selfxw.formatFontAndBorders(rowValues)
# projectHeaderRng = projectsSht.range('A2:H2')
# projectHeaderRng.font.bold = True
# # 表头垂直水平居中
# selfxw.formatInAllCenter(projectHeaderRng)
# selfxw.formatInAllCenter(projectsSht.range('C3:G3'))
# # 列设置 靠左
# selfxw.formatLeftCenter(projectsSht.range('F3:F3'))
# selfxw.formatLeftCenter(projectsSht.range('B3:B3'))
# selfxw.formatLeftCenter(projectsSht.range('H3:H3'))

# projectsSht.range('H3:H3').wrap_text = True