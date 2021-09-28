import http.cookiejar, urllib.request

filename = '.\\demo\\txt\\cookies.txt'
# 将 cookie 保存成文件使用 MozillaCookieJar
cookie = http.cookiejar.MozillaCookieJar(filename)
# LWP 格式的 Cookies 文件
#cookie = http.cookiejar.LWPCookieJar(filename)

# cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
# https://docs.python.org/3.9/ 没有 cookie?
response = opener.open('https://cn.bing.com')

print(response.status)

for item in cookie:
    print(item.name+" = "+item.value)

# MozillaCookieJar
cookie.save(ignore_discard=True, ignore_expires=True)