from bs4 import BeautifulSoup
import requests #allows us to download html from urls

page = requests.get("https://www.draftkings.com/draft/contest/56828613") #for the game you parse

soup = BeautifulSoup(page.content, 'html.parser') #.content call returns actual html

##these requests update the complete nba roster data struture##
atlantahawks = requests.get("https://www.2kratings.com/nba2k18-team/atlanta-hawks")

bostonceltics = requests.get("https://www.2kratings.com/nba2k18-team/boston-celtics")

brooklynnets = requests.get("https://www.2kratings.com/nba2k18-team/brooklyn-nets")

charlottehornets = requests.get("https://www.2kratings.com/nba2k18-team/charlotte-hornets")

chicagobulls = requests.get("https://www.2kratings.com/nba2k18-team/chicago-bulls")

clevelandcavaliers = requests.get("https://www.2kratings.com/nba2k18-team/cleveland-cavaliers")

dallasmavericks = requests.get("https://www.2kratings.com/nba2k18-team/dallas-mavericks")

denvernuggets = requests.get("https://www.2kratings.com/nba2k18-team/denver-nuggets")

detroitpistons = requests.get("https://www.2kratings.com/nba2k18-team/detriot-pistons")

goldenstatewarriors = requests.get("https://www.2kratings.com/nba2k18-team/golden-state-warriors")

houstonrockets = requests.get("https://www.2kratings.com/nba2k18-team/houston-rockets")

indianapacers = requests.get("https://www.2kratings.com/nba2k18-team/indiana-pacers")

losangelesclippers = requests.get("https://www.2kratings.com/nba2k18-team/los-angeles-clippers")

memphisgrizzlies = requests.get("https://www.2kratings.com/nba2k18-team/memphis-grizzlies")

miamiheat = requests.get("https://www.2kratings.com/nba2k18-team/miami-heat")

milwaukeebucks = requests.get("https://www.2kratings.com/nba2k18-team/milwaukee-bucks")

minnesotatimberwolves = requests.get("https://www.2kratings.com/nba2k18-team/minnesota-timberwolves")

neworleanspelicans = requests.get("https://www.2kratings.com/nba2k18-team/new-orleans-pelicans")

newyorkknicks = requests.get("https://www.2kratings.com/nba2k18-team/new-york-knicks")

oklahomacitythunder = requests.get("https://www.2kratings.com/nba2k18-team/oklahoma-city-thunder")

orlandomagic = requests.get("https://www.2kratings.com/nba2k18-team/orlando-magic")

philadelphia76ers = requests.get("https://www.2kratings.com/nba2k18-team/philadelphia-76ers")

phoenixsuns = requests.get("https://www.2kratings.com/nba2k18-team/phoenix-suns")

portlandtrailblazers = requests.get("https://www.2kratings.com/nba2k18-team/portland-trail-blazers")

sacramentokings = requests.get("https://www.2kratings.com/nba2k18-team/sacramento-kings")

sanantoniospurs = requests.get("https://www.2kratings.com/nba2k18-team/san-antonio-spurs")

utahjazz = requests.get("https://www.2kratings.com/nba2k18-team/utah-jazz")

torontoraptors = requests.get("https://www.2kratings.com/nba2k18-team/toronto-raptors")

washingtonwizards = requests.get("https://www.2kratings.com/nba2k18-team/washington-wizards")

hawkspage = BeautifulSoup(atlantahawks.content,'html.parser')
tag = hawkspage.td
#tag.name = "wololo"
print(tag.attrs)
#myarr = [hawkspage]
#print(myarr[0])
