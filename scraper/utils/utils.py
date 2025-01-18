import datetime
import requests
from bs4 import BeautifulSoup

from scraper.classes.LinksList import LinksList


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