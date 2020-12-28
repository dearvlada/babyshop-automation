import requests
from lxml.html import fromstring

# получаем содержимое сайта
r = requests.get('https://www.babyshop.com')
# превращаем его в строгое xml-дерево при помощи
# функции fromstring из функции html из библиотеки lxml
tree = fromstring(r.content)
# и используем получение данных по xpath
mainmenu = tree.xpath('//*[@class="navigation__item"]/a/text()')
# смотрим, что мы получили
print(mainmenu)
