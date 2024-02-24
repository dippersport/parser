# подключаем urlopen из модуля urllib
from urllib.request import urlopen

# подключаем библиотеку BeautifulSoup
from bs4 import BeautifulSoup

url = ['https://gb.ru/']

# получаем исходный код страницы
inner_html_code = str(urlopen('https://gb.ru/').read(),'utf-8')

# открываем текстовый файл, куда будем добавлять заголовки
with open("zag.txt", "a", encoding="utf-8") as file:
    # перебираем все адреса из списка
    for x in url:
        # получаем исходный код очередной страницы из списка
        html_code = str(urlopen(x).read(),'utf-8')

        # отправляем исходный код страницы на обработку в библиотеку
        inner_soup = BeautifulSoup(inner_html_code, "html.parser")

        # находим название страницы с помощью метода find()
        s = inner_soup.find('title').text
        
        # очищаем код от выбранных элементов
        def delete_div(code,*args):
             for tag in args:
             # находим все указанные теги с параметрами
              for div in code.find_all(tag): 
                # и удаляем их из кода
                div.decompose()

        # удаляем боковые ссылки
        delete_div(inner_soup, "div",'h1', 'h2', {'class':'wp-block-lazyblock-link-aside'})

        # удаляем баннеры, перебирая все их возможные индексы в цикле (потому что баннеры в 
        #коде имеют номера от 1 до 99)
        for i in range(99):
            delete_div(inner_soup, "div", {'class':'wp-block-lazyblock-banner'+str(i)})

        # удаляем титры
        delete_div(inner_soup, "div", {'class':'mn-region'})
        
        # получаем текстовое содержимое страницы
        text_content = inner_soup.get_text()

        # записываем текстовое содержимое в файл
        file.write(text_content + "\n")
