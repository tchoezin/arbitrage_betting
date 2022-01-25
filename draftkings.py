from optparse import TitledHelpFormatter
from bs4 import BeautifulSoup
import urllib.request
#import re
from scraping import oddsAndTeamsExtractor
from scraping import gamesDictCreator

url = "https://sportsbook.draftkings.com/leagues/basketball/88670846"

#open the given url and assign the content to page var, if not send error
try:
    page = urllib.request.urlopen(url)
except:
    print("Error Occured")

#allows us to parse html content of given url page using Beautiful Soup
soup = BeautifulSoup(page, 'html.parser')

oddsClass = 'sportsbook-odds american no-margin default-color'
teamsClass = 'event-cell__name-text'

oddsList, teamsList = oddsAndTeamsExtractor(soup, oddsClass, teamsClass)

gamesDict = gamesDictCreator(oddsList, teamsList)

print(gamesDict)
