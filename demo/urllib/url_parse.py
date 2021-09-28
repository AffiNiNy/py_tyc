from urllib.parse import quote, unquote

url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))
print(unquote('%3A'))
print(unquote('%3D'))

content = '&cql_filter=1=1'
print(quote(content))