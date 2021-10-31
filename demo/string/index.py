import urllib.parse

s = '$A$1:$H$3'
# print(s.lstrip())
# print(s.rstrip())
# print(urllib.parse.quote_plus(s))

# a = s.split(':')
# print(type(a))
# print(a[0])
# print(a[0].find('$',2))
# print(a[0].find('A'))

s = 'abcd{0}'
print(s.format(123))