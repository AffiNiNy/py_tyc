import csv

filePath = 'D:\DEVELOP\VSCode_Projects\ALittlePythonProg\myio\csv\companyList.csv'

def get_companyList():
    result = []
    with open(filePath, "r", encoding='utf-8') as f:
        reader = csv.reader(f)
        for item in reader:
            result.append(item[0])
    
    return result