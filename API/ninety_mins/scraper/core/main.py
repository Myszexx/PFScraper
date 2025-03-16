import API.ninety_mins.scraper.ninety_minutes.parsers.ZPNs as ZPN
import API.ninety_mins.scraper.utils.utils as utils

debug = True
print(f'Witaj w scraperze danych piłkarskich, wybierz serwis z którego będziesz scrapował:\n1) minuts.pl\n2) TBD')
# type = input()
#wybieramy ZPN
html = utils.get_html_from_ninety('/ligireg.html')

zpns = ZPN.get_zpns_list(html)
print(str(zpns.get_all()).replace("'",'"'))
html = utils.chooser(zpns)
#Wybieramy poziom
leagues = ZPN.get_leagues_list(html)
# print(str(leagues.get_all()).replace("'",'"'))
html = utils.chooser(leagues)#,debug=debug)

# #Obrabiamy dostępne dane
league = ZPN.get_league_standings(html)
print(league.get_json())

# html = ZPN.utils.get_html_from_ninety(league.get_team_at(1)['url'])
# team = TP.get_team_data(html, league.get_team_at(1)['team'],league.get_team_at(1)['url'])
# print(team.get_all())

fixtures = ZPN.get_fixtures(html, league)
# print("TAK")
print(fixtures.get_all())
API.scraper.utils.utils.save_to_file(fixtures.get_json(), 'fixtures.json')