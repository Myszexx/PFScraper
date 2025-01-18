import ninety_minutes.parsers.ZPNs as ZPN
from scraper.utils.utils import chooser
debug = True
print(f'Witaj w scraperze danych piłkarskich, wybierz serwis z którego będziesz scrapował:\n1) minuts.pl\n2) TBD')
# type = input()
#wybieramy ZPN
html = ZPN.utils.get_html_from_ninety('/ligireg.html')
zpns = ZPN.get_zpns_list(html)
html = chooser(zpns,debug=debug)
#Wybieramy poziom
leagues = ZPN.get_leagues_list(html)
html = chooser(leagues,debug=debug)
#Obrabiamy dostępne dane
league = ZPN.get_league_standings(html)
league.print()
print(league.show_team_at(5))