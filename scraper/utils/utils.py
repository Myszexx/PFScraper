import datetime
import requests
from bs4 import BeautifulSoup

from scraper.classes.LinksList import LinksList

MONTHS = {
    "stycznia": 1,
    "lutego": 2,
    "marca": 3,
    "kwietnia": 4,
    "maja": 5,
    "czerwca": 6,
    "lipca": 7,
    "sierpnia": 8,
    "września": 9,
    "października": 10,
    "listopada": 11,
    "grudnia": 12
}

def give_season(theDate):
    if theDate.month > 8:
        return '{0}/{1}'.format(theDate.year, theDate.year+1)
    else:
        return '{0}/{1}'.format(theDate.year-1, theDate.year)

def give_current_season():
    return give_season(datetime.datetime.now())

def get_html_from_ninety(link):
    r = requests.get('http://www.90minut.pl'+link)
    html = BeautifulSoup(r.text, 'html.parser')

    return html

def chooser(ll: LinksList, debug=False):
    ll.print()
    a = None
    if not debug:
        while type(a) != int:
            a = int(input("Wybierz pozycję: "))
    else:
        a = 1
    choosed = ll.get_to(a)
    print(f'Przechodzimy do {choosed["to"]}')
    html = get_html_from_ninety(choosed['link'])

    return html

def save_to_file(text, filename):
    with open(filename, 'w') as f:
        f.write(text)

def parse_dates(input_date, season):
    try:
        day, month_name, time = input_date.replace(",", "").split()
        day = int(day)  # Konwertujemy dzień na liczbę
        month = MONTHS.get(month_name)  # Pobranie numeru miesiąca z mapy
        hour, minute = map(int, time.split(":"))  # Konwersja godziny i minut

        # Dopasowanie roku w zależności od miesiąca i sezonu
        season_start, season_end = map(int, season.split("/"))
        if month >= 8:  # Jeśli od sierpnia, jest to drugi rok sezonu
            year = season_start
        else:  # W innym przypadku należy do początku sezonu
            year = season_end

        # Zwracanie daty
        return datetime.datetime(year, month, day, hour, minute)

    except (ValueError, KeyError) as e:
        raise ValueError(f"Nieprawidłowy format daty '{input_date}' lub sezonu '{season}'") from e
