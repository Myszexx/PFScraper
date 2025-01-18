import scraper.utils.utils as utils
from scraper.classes.LeagueTable import LeagueTable
from scraper.classes.LinksList import LinksList
import re

def get_zpns_list(soup):
    tables = soup.find_all('table')
    zpns = LinksList()
    [zpns.add(zpn.text, zpn.attrs['href']) for zpn in tables[3].find_all('a') if 'ZPN' in zpn.text]

    return zpns

def get_leagues_list(soup):
    tables = soup.find_all('table')
    leagues = LinksList()
    [leagues.add(league.text, league.attrs['href']) for league in tables[3].find_all('a') if str(utils.give_current_season()) in league.text]

    return leagues


def get_league_standings(soup):
    tables = soup.find_all('table')
    teams = LeagueTable()
    rows = [row for row in tables[3].find_all('tr') if row.get('bgcolor') != '#B81B1B' and row.get('bgcolor')]
    for row in rows:
        cells = row.find_all('td')
        teams.add(
            cells[1].text, #Team name
            cells[0].text.replace('.',''), #Standing
            cells[3].text, #Points
            cells[4].text, #Wins
            cells[6].text, #Loses
            cells[5].text, #Draws
            re.search(r'^(.*?)-', cells[7].text).group(1), #Goals shot
            re.search(r'-(.*)$', cells[7].text).group(1) #Goals conceded
        )
        # teams.add(row.find_all('td')[0].text, row.find_all('td')[1].text, row.find_all('td')[2].text, row.find_all('td')[3].text)
    return teams
