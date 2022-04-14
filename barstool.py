from optparse import TitledHelpFormatter
from bs4 import BeautifulSoup
import urllib.request
#import re
from scraping import oddsAndTeamsExtractorBS
from scraping import gamesDictCreator

url = "https://www.barstoolsportsbook.com/sports/basketball/nba?category=upcoming"

try:
    page = urllib.request.urlopen(url)
except:
    print("Error Occured")

soup = BeautifulSoup(page, 'html.parser')

oddsClass = 'odds'
teamsClass = 'desc'

oddsList, teamsList = oddsAndTeamsExtractorBS(soup, oddsClass, teamsClass)

gamesDict = gamesDictCreator(oddsList, teamsList)

print(gamesDict)
