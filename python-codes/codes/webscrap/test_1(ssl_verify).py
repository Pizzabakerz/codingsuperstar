import bs4 as bs
import urllib.request as r

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

sauce = r.urlopen("https://facebook.com").read()
print(sauce)

soup = bs.BeautifulSoup(sauce,'lxml')
print(soup.title)

print(soup.title.text)
#
# print(soup.find_all('a'))
# print(soup.find_all('p'))
#
# for p in soup.find_all('p'):
#     print(p.text)
#
# print('------------')
# print(soup.get_text())
#
# print('------------')
#
# for a in soup.find_all('a'):
#     print(a.get('href'))



