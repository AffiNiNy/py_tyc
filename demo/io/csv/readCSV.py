import csv

filePath = 'D:\DEVELOP\VSCode_Projects\ALittlePythonProg\io\sourceFiles\companyList.csv'

result = []
with open(filePath, "r", encoding='utf-8') as f:
    reader = csv.reader(f)
    for item in reader:
        result.append(item)

print(result)
