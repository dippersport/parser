# открываем текстовый файл
f = open('tom1.txt', "r", encoding="utf-8")
# закидываем его содержимое в переменную
text = f.read()
# выводим начало, чтобы убедиться, что всё считалось правильно
print(text[:300])



# переводим символы в нижний регистр, чтобы всё было одинаково
text = text.lower()
# подключаем встроенный модуль работы со строками
import string
# добавляем к стандартным знакам пунктуации кавычки и многоточие
spec_chars = string.punctuation + '«»\t—…’'
# очищаем текст от знаков препинания
text = "".join([ch for ch in text if ch not in spec_chars])
# подключаем регулярные выражения
import re
# меняем переносы строк на пробелы
text = re.sub('\n', ' ', text)
# убираем из текста цифры
text = "".join([ch for ch in text if ch not in string.digits])
# смотрим на результат
print(text[:300])

# подключаем библиотеку для работы с текстом
import nltk
#nltk.download('punkt')
nltk.download('stopwords')

# из библиотеки обработки текста подключаем модуль для токенизации слов
from nltk import word_tokenize
# токенизируем текст
text_tokens = word_tokenize(text)



# переводим токены в текстовый формат
text = nltk.Text(text_tokens)
# подключаем статистику 
from nltk.probability import FreqDist
# и считаем слова в тексте по популярности
fdist = FreqDist(text)
# выводим первые 5 популярных слов
print(fdist.most_common(5))

# подключаем модуль со стоп-словами
from nltk.corpus import stopwords
# добавляем русские и французские стоп-слова
russian_stopwords = stopwords.words("russian")
russian_stopwords += stopwords.words("french")
# перестраиваем токены, не учитывая стоп-слова
text_tokens = [token.strip() for token in text_tokens if token not in russian_stopwords]
# снова приводим токены к текстовому виду
text = nltk.Text(text_tokens)
# считаем заново частоту слов
fdist_sw = FreqDist(text)
# показываем самые популярные
print(fdist_sw.most_common(10))

# добавляем свои слова в этот список
russian_stopwords.extend(['это', 'чтò','всё','сказал', 'сказала','говорил','говорила'])
# перестраиваем токены, не учитывая стоп-слова
text_tokens = [token.strip() for token in text_tokens if token not in russian_stopwords]
# снова приводим токены к текстовому виду
text = nltk.Text(text_tokens)
# считаем заново частоту слов
fdist_sw = FreqDist(text)
# показываем самые популярные

# подключаем библиотеку для создания облака слов
from wordcloud import WordCloud
# и графический модуль, с помощью которого нарисуем это облако
import matplotlib.pyplot as plt
# переводим всё в текстовый формат
text_raw = " ".join(text)
# готовим размер картинки
wordcloud = WordCloud(width=1600, height=800).generate(text_raw)
plt.figure( figsize=(20,10), facecolor='k')
# добавляем туда облако слов
plt.imshow(wordcloud)
# выключаем оси и подписи
plt.axis("off")
# убираем рамку вокруг
plt.tight_layout(pad=0)
# выводим картинку на экран
plt.show()