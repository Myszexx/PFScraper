import ninety_minutes.parsers.ZPNs as ZPN

debug = True
print(f'Witaj w scraperze danych piłkarskich, wybierz serwis z którego będziesz scrapował:\n1) minuts.pl\n2) TBD')
# type = input()
#wybieramy ZPN
html = ZPN.utils.get_html_from_ninety('/ligireg.html')
zpns = ZPN.get_zpns_list(html)
html = ZPN.utils.chooser(zpns,debug=debug)
#Wybieramy poziom
leagues = ZPN.get_leagues_list(html)
html = ZPN.utils.chooser(leagues,debug=debug)
#Obrabiamy dostępne dane
league = ZPN.get_league_standings(html)
fixtures = ZPN.get_fixtures(html, league)
print("TAK")
print(fixtures.get_all())
ZPN.utils.save_to_file(fixtures.get_json(), 'fixtures.json')