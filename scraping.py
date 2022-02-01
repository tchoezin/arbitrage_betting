from optparse import TitledHelpFormatter
from bs4 import BeautifulSoup
import re
from datetime import date

"""
Thoughts:

To accomadate for BetOnline, Search through div classes and compare the date to current date.
If match, then search for moneyline class and within those, scrape the odds since all of the odds
regardless of if for spread, moneyline or total all have the same class.
"""

"""
name: oddsAndTeamsExtractor
parameters: soup object -> soup, string -> oddsClass, string -> teamsClass
returns: list -> oddsList, list -> teamsList

Creates a list for all of the odds for each team that is playing a game.
"""
def oddsAndTeamsExtractor(soup, oddsClass, teamsClass=None):
    #create regular expression matching pattern for desired info
    oddsRegex = re.compile(oddsClass)
    teamRegex = re.compile(teamsClass)

    spansOddsList = soup.find_all("span", oddsRegex)

    oddsList = []
    for span in spansOddsList:
        oddsList.append(int(span.text))

    divTeamsList = soup.find_all("div", teamRegex)

    teamsList = []
    for div in divTeamsList:
        teamsList.append(div.text)
    return oddsList,teamsList

#oddsList, teamsList = oddsAndTeamsExtractor(soup, oddsClass, teamsClass)

"""
name: gamesDictCreator
parameters: list -> oddsList: list of odds, list -> teamsList: list of teams in respective order
to odds
returns: dictionary -> gameDict: dictionary containing each game and each team's odds to win

Takes an oddsList and a teamsList and creates a dictionary containing each NBA game and each team's
odds
"""
def gamesDictCreator(oddsList, teamsList):
    teamsDictList = []
    for i in range(0, len(teamsList), 2):
        gameDict = {}
        gameDict[teamsList[i]] = oddsList[i]
        gameDict[teamsList[i+1]] = oddsList[i+1]
        teamsDictList.append(gameDict)

    gamesDict = {}
    for dict in teamsDictList:
        teamNames = []
        for key in dict:
            teamNames.append(key)
        gameKey = teamNames[0][teamNames[0].find(" ")+1:] + ' vs. ' + teamNames[1][teamNames[1].find(" ")+1:]
        gamesDict[gameKey] = dict
    return gamesDict

#gamesDict = gamesDictCreator(oddsList, teamsList)

#print(gamesDict)

#Thoughts:
#I think it might be better to create a dictionary with each game as a key
#Probably nested dictionaries for each specific team with different keys for spread, total, moneyline????
#Currently only have the moneylines for each game
#I think we should definitely do dictionaries actually because we currently need a different scraper for each
    # betting website and would be easier to search for odds for the same game between different websites
# maybe could use pandas dataframe, but currently don't see a necessity for it unless we think modeling
    # and visualizations would be helpful
