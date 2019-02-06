def find_long_words(text):
    splitted_item = text.split()
    for word in splitted_item:
        if len(word) > 6:
            all_long_words.append(word)


def sort_and_print_words():
    import operator

    for word in all_long_words:
        if word not in frequency_of_words:
            counter = int()
            for item in all_long_words:
                if item == word:
                    counter += 1
            frequency_of_words.update({word: counter})

    sorted_words = sorted(frequency_of_words.items(), key=operator.itemgetter(1), reverse=True)

    print('Вот топ 10 самых часто встречающихся слов:')

    i = 0
    while i < 10:
        print('{}. {} ({} раз)'.format(i + 1, sorted_words[i][0], sorted_words[i][1]))
        i += 1


all_long_words = []
frequency_of_words = {}


def json_homework():
    print('JSON Файл')

    import json

    with open('newsafr.json', encoding='utf-8') as news_json:
        parsed_news = json.load(news_json)
        for item in parsed_news['rss']['channel']['items']:
            find_long_words(item['description'])

    sort_and_print_words()


def xml_homework():
    print('XML Файл')

    import xml.etree.ElementTree as ET

    tree = ET.parse('newsafr.xml')

    root = tree.getroot()

    news_items = root.findall('channel/item')

    all_long_words = []
    frequency_of_words = {}

    for item in news_items:
        find_long_words(item.find('description').text)

    sort_and_print_words()


json_homework()
xml_homework()
