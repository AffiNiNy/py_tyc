import re

pattern = "^(MEMO)(\d+)"
cot = "MEMO339"
# print(len(cot))

# match() 方法是从字符串的开头开始匹配的
# search()，它在匹配时会扫描整个字符串
res = re.match(pattern, cot)
print(res)
if res != None:
    print(res.group())
    print(res.group(1))
    print(res.group(2))
    print(res.span())
else:
    print("Not match.")