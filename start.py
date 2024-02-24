# подключаем urlopen из модуля urllib
from urllib.request import urlopen

# подключаем библиотеку BeautifulSout
from bs4 import BeautifulSoup

url = [
"https://thecode.media/is-not-defined-jquery/",
"https://thecode.media/arduino-projects-2/",
"https://thecode.media/10-raspberry/",
"https://thecode.media/easy-css/",
"https://thecode.media/to-be-front/",
"https://thecode.media/cryptex/",
"https://thecode.media/ali-coders/",
"https://gb.ru/lessons/391723",
"https://thecode.media/shtykov/",

]

# открываем текстовый файл, куда будем добавлять заголовки
file = open("zag.txt", "a")

# перебираем все адреса из списка
for x in url:
    # получаем исходный код очередной страницы из списка
    html_code = str(urlopen(x).read(),'utf-8')
    # отправляем исходный код страницы на обработку в библиотеку
    soup = BeautifulSoup(html_code, "html.parser")

    # находим название страницы с помощью метода find()
    s = soup.find('title').text

    # выводим его на экран
    print(s)

    # сохраняем заголовок в файле и переносим курсор на новую строку
    file.write(s + '. ')

# закрываем файл
file.close()