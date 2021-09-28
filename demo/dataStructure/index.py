# list 查元素索引
# l = ['a', 'b', 'c']
# print(l.index('a'))
# try:
#     l.index('z')
# except:
#     print('not include..')

from re import L


l = ['a']
l = ['b']
l = ['c']
l = ['d']
l.append('广州\n佛山ci士')
l.append(True)

for e in l:
    if e == 'd':
        mflag = True
print(mflag)