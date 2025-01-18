# PFScraper
# Football Data Scraper
## Overview
This is a Python-based football data scraper designed to fetch information from various football websites. Currently, **90minut.pl** is the only supported source, but the project is designed to be extendable for other sources in the future. The scraper collects data such as fixtures, league tables, results, and events for specific leagues and seasons, and outputs the data in structured JSON format.
## Features
- **Modular Design:** Easily extendable to support additional football data sources.
- **League Selection:** Allows selection of regional leagues (e.g., ZPNs for 90minut.pl).
- **League Standings:** Fetches league standings, including teams' ranks, matches played, wins, losses, goals, and more.
- **Fixtures:** Collects fixtures for a specified league, including match events like goals and penalties.
- **Match Events:** Scrapes detailed data on match events (e.g., penalties, own goals, regular goals).
- **Data Export:** Outputs data (such as fixtures and standings) in JSON format for analysis or storage.

## Current Support
As of now, the scraper supports the following source:
- **90minut.pl** – A Polish football website providing fixtures, tables, and results for regional and national leagues.

Planned future updates will include support for additional websites/platforms.

## Technology and Tools Used
- **Python:** Core programming language for implementation.
- **BeautifulSoup:** HTML parser for extracting data from web pages.
- **Requests:** Makes HTTP requests to fetch webpage content from football websites.
- **JSON:** For exporting scraped data in a machine-readable format.
