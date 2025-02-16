import datetime
import re
import scraper.utils.utils as utils
from scraper.classes.FixtureCollection import FixtureCollection, Match, MatchEvents, Fixture
from scraper.classes.LeagueTable import LeagueTable
from scraper.classes.LinksList import LinksList


def parse_home_events(home_events_raw: str) -> MatchEvents:

    home_events = MatchEvents()


    players_events = re.findall(r"([a-zA-Z\s]+)\s([\d,\s\(k\)\(own\)]+)", home_events_raw)
    for player_name, event_info in players_events:
        player_name = player_name.strip()
        minute_events = re.findall(r"\d+\s?\(?[a-z]*\)?", event_info)
        for event in minute_events:
            if "(k)" in event:
                sub_event = "penalty"
            elif "(own)" in event:
                sub_event = "own goal"
            else:
                sub_event = "regular"

            time = int(re.search(r"\d+", event).group())
            home_events.add_event("home",player_name, sub_event, time)

    return home_events


def parse_away_events(away_events_raw: str) -> MatchEvents:
    away_events = MatchEvents()

    players_events = re.findall(r"([a-zA-Z\s]+)\s([\d,\s\(k\)\(own\)]+)", away_events_raw)
    for player_name, event_info in players_events:
        player_name = player_name.strip()
        minute_events = re.findall(r"\d+\s?\(?[a-z]*\)?", event_info)
        for event in minute_events:
            if "(k)" in event:
                sub_event = "penalty"
            elif "(own)" in event:
                sub_event = "own goal"
            else:
                sub_event = "regular"
            time = int(re.search(r"\d+", event).group())
            away_events.add_event("away",player_name, sub_event, time)

    return away_events


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
            re.search(r'-(.*)$', cells[7].text).group(1), #Goals conceded
            cells[1].find('a')['href'] if cells[1].find('a') else 'URL not found'  # URL
        )
        # teams.add(row.find_all('td')[0].text, row.find_all('td')[1].text, row.find_all('td')[2].text, row.find_all('td')[3].text)
    return teams

def get_fixtures(soup, table: LeagueTable):
    round_number = 0
    matches = False
    vs = Match(False,None,None,datetime.datetime.now(),None,None,MatchEvents(),MatchEvents(),)
    tables = soup.find_all('table')
    fixture = Fixture(0)
    fixtures = FixtureCollection()
    #print(len(tables[1].find_all('td', class_='main')))

    rows = tables[1].find_all('td', class_='main')[10].find_all('table')
    for row in rows:
        utils.save_to_file(str(row), "ZPNs.html")
        if "Kolejka" in row.text.strip():
            if fixture.matches_count() > 0:
                fixtures.add_fixture(fixture)
            round_number = int(re.search(r'Kolejka\s+(\d+)', row.text).group(1))
            fixture = Fixture(round_number)
            matches = True
            print(f'\n\nKolejka {round_number}')
        elif matches and round_number>0:
            for match in row.find_all('tr'):
                match_data = match.find_all('td')
                if not match_data[0].find_all('b'):
                    try:
                        vs = Match(
                            False,
                            match_data[0].text,
                            match_data[2].text,
                            None,
                            -1,
                            -1,
                            MatchEvents(),
                            MatchEvents()
                        )
                        fixture.add_match(vs)
                        print(f'Meczyk: {vs.home_team} - {vs.away_team}')
                    except:
                        print(f'Row skipped: {str(match_data)}')
                elif table.is_team_in_league(match_data[0].text):

                    try:
                        vs = Match(
                            True,
                            match_data[0].text,
                            match_data[2].text,
                            utils.parse_dates(match_data[3].text, utils.give_current_season()),
                            int(re.search(r'^(.*?)-', match_data[1].text).group(1)),
                            int(re.search(r'-(.*)$', match_data[1].text).group(1)),
                            MatchEvents(),
                            MatchEvents()
                        )
                        fixture.add_match(vs)
                        print(f'Meczyk: {vs.home_team} - {vs.away_team}')
                    except:
                        print(f'match_data0: {match_data[0].text}; match_data1: {match_data[1].text}; match_data2: {match_data[2].text}; match_data3: {match_data[3].text}')
                else:
                    if '(wo)' in match_data[0].text:
                        vs.add_event(MatchEvents().add_event('W.O','','',0),vs.home_goals > 0)
                    else:
                        away_events = parse_away_events(match_data[0].text)
                        home_events = parse_home_events(match_data[0].text)
                        if home_events: vs.add_event(home_events,True)
                        if away_events: vs.add_event(away_events,False)
            matches = False
    return(fixtures)