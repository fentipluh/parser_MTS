from bs4 import BeautifulSoup
import json, re
def collect_data():
    data = {}

    with open("../parser_MTS/data/index.html", encoding='utf-8') as file:
        src = file.read()


    soup = BeautifulSoup(src, 'lxml')

    items_cards = soup.find_all("div", class_ = "card card__wrapper card__shadow card__clickable")

    all_cards = soup.find_all(class_ = "feature-description feature-description__text feature-description__margin")

    for item in items_cards:
        product_name = item.find("span", class_ = "card-title__link").text
        product_price = (item.find("div", class_ = "price-main").text).replace(' ', '')

        pattern = r'(\d+\s?[Гг][Б]|\d+\s?[Мм]инут|\d+\s?[Гг][б][Ии]т\/[Сс]|\d+\s?[Мм]бит\/[Сс]|\d+\s?\d*\s?[Тт][Вв])'
        result = re.findall(pattern, item.text)

        product_mobile_internet = next((value for value in result if re.search(r'\d\s[Гг][Б]', value)), None)
        product_TV = next((value for value in result if re.search(r'\d\s[Тт][Вв]', value)), None)
        product_internet_speed = next((value for value in result if re.search(r'\d+\s?[Гг][б]|\d+\s?[Мм]бит\/[Сс]', value)), None)
        product_minutes = next((value for value in result if re.search(r'\d+\s?[Мм]инут', value)), None)


        data[product_name] = {
            "product_price": product_price,
            "product_mobile_internet": product_mobile_internet,
            'product_TV': product_TV,
            'product_intenet_speed': product_internet_speed,
            'product_minutes' : product_minutes,
        }

    with open("../parser_MTS/data/collected_data.json", "w", encoding='utf-8') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)
    return data
