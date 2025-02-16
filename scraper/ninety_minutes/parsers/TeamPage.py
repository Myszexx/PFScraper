from scraper.classes.LinksList import LinksList
from scraper.classes.Team import Team


def get_team_data(soup,name,url):
    tables = soup.find_all('table')[1].find_all('table')
    rows = []
    plays = False
    team = Team(name,url,LinksList())
    for row in tables[1].find_all('tr'):
        if plays:
            team.append_season({'to': row.find_all('td')[0].text, 'link': row.find_all('td')[0].find('a')['href']})
        if 'Rozgrywki z udziałem' in row.text:
            plays = True
    return team