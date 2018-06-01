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

losangeleslakers = requests.get("https://www.2kratings.com/nba2k18-team/los-angeles-lakers")

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
celticspage = BeautifulSoup(bostonceltics.content,'html.parser')
netspage = BeautifulSoup(brooklynnets.content,'html.parser')
hornetspage = BeautifulSoup(charlottehornets.content,'html.parser')
bullspage = BeautifulSoup(chicagobulls.content,'html.parser')
cavalierspage = BeautifulSoup(clevelandcavaliers.content,'html.parser')
maverickspage = BeautifulSoup(dallasmavericks.content,'html.parser')
nuggetspage = BeautifulSoup(denvernuggets.content,'html.parser')
pistonspage = BeautifulSoup(detroitpistons.content,'html.parser')
warriorspage = BeautifulSoup(goldenstatewarriors.content,'html.parser')
rocketspage = BeautifulSoup(houstonrockets.content,'html.parser')
pacerspage = BeautifulSoup(indianapacers.content,'html.parser')
clipperspage = BeautifulSoup(losangelesclippers.content,'html.parser')
lakerspage = BeautifulSoup(losangeleslakers.content,'html.parser')
grizzliespage = BeautifulSoup(memphisgrizzlies.content,'html.parser')
heatpage = BeautifulSoup(miamiheat.content,'html.parser')
buckspage = BeautifulSoup(milwaukeebucks.content,'html.parser')
timberwolvespage = BeautifulSoup(minnesotatimberwolves.content,'html.parser')
pelicanspage = BeautifulSoup(neworleanspelicans.content,'html.parser')
knickspage = BeautifulSoup(newyorkknicks.content,'html.parser')
thunderpage = BeautifulSoup(oklahomacitythunder.content,'html.parser')
magicpage = BeautifulSoup(orlandomagic.content,'html.parser')
philadelphiapage = BeautifulSoup(philadelphia76ers.content,'html.parser')
sunspage = BeautifulSoup(phoenixsuns.content,'html.parser')
trailblazerspage = BeautifulSoup(portlandtrailblazers.content,'html.parser')
kingspage = BeautifulSoup(sacramentokings.content,'html.parser')
spurspage = BeautifulSoup(sanantoniospurs.content,'html.parser')
jazzpage = BeautifulSoup(utahjazz.content,'html.parser')
raptorspage = BeautifulSoup(torontoraptors.content,'html.parser')
wizardspage = BeautifulSoup(washingtonwizards.content,'html.parser')

#print(hawkspage.find("div",class_="roster-entry").text)
#prettyhawks = hawkspage.prettify()

#result = hawkspage.find('td',class_ = "roster-entry")
#print(result.get_text())

# ----- TESTING IF STRING FUNCTIONS WORK ON UNICODE STRING ----- #
#removed = result.get_text().replace("Dennis","")
#print(removed)


# ------- THIS WORKS ----------#
hawksresult = hawkspage.find_all('td',class_ = "roster-entry")
celticsresult = celticspage.find_all('td',class_ = "roster-entry")
netsresult = netspage.find_all('td',class_ = "roster-entry")
hornetsresult = hornetspage.find_all('td',class_ = "roster-entry")
bullsresult = bullspage.find_all('td',class_ = "roster-entry")
cavaliersresult = cavalierspage.find_all('td',class_ = "roster-entry")
mavericksresult = maverickspage.find_all('td',class_ = "roster-entry")
nuggetsresult = nuggetspage.find_all('td',class_ = "roster-entry")
pistonsresult = pistonspage.find_all('td',class_ = "roster-entry")
warriorsresult = warriorspage.find_all('td',class_ = "roster-entry")
rocketsresult = rocketspage.find_all('td',class_ = "roster-entry")
pacersresult = pacerspage.find_all('td',class_ = "roster-entry")
clippersresult = clipperspage.find_all('td',class_ = "roster-entry")
lakersresult = lakerspage.find_all('td',class_ = "roster-entry")
grizzliesresult = grizzliespage.find_all('td',class_ = "roster-entry")
heatresult = heatpage.find_all('td',class_ = "roster-entry")
bucksresult = buckspage.find_all('td',class_ = "roster-entry")
timberwolvesresult = timberwolvespage.find_all('td',class_ = "roster-entry")
pelicansresult = pelicanspage.find_all('td',class_ = "roster-entry")
knicksresult = knickspage.find_all('td',class_ = "roster-entry")
thunderresult = thunderpage.find_all('td',class_ = "roster-entry")
magicresult = magicpage.find_all('td',class_ = "roster-entry")
philadelphiaresult = philadelphiapage.find_all('td',class_ = "roster-entry")
sunsresult = sunspage.find_all('td',class_ = "roster-entry")
trailblazersresult = trailblazerspage.find_all('td',class_ = "roster-entry")
kingsresult = kingspage.find_all('td',class_ = "roster-entry")
spursresult = spurspage.find_all('td',class_ = "roster-entry")
jazzresult = jazzpage.find_all('td',class_ = "roster-entry")
raptorsresult = raptorspage.find_all('td',class_ = "roster-entry")
wizardsresult = wizardspage.find_all('td',class_ = "roster-entry")

myarr = []
for x in hawksresult:
    myarr.append(x.get_text())
for x in celticsresult:
    myarr.append(x.get_text())
for x in netsresult:
    myarr.append(x.get_text())
for x in hornetsresult:
    myarr.append(x.get_text())
for x in bullsresult:
    myarr.append(x.get_text())
for x in cavaliersresult:
    myarr.append(x.get_text())
for x in mavericksresult:
    myarr.append(x.get_text())
for x in nuggetsresult:
    myarr.append(x.get_text())
for x in pistonsresult:
    myarr.append(x.get_text())
for x in warriorsresult:
    myarr.append(x.get_text())
for x in rocketsresult:
    myarr.append(x.get_text())
for x in pacersresult:
    myarr.append(x.get_text())
for x in clippersresult:
    myarr.append(x.get_text())
for x in lakersresult:
    myarr.append(x.get_text())
for x in grizzliesresult:
    myarr.append(x.get_text())
for x in heatresult:
    myarr.append(x.get_text())
for x in bucksresult:
    myarr.append(x.get_text())
for x in timberwolvesresult:
    myarr.append(x.get_text())
for x in pelicansresult:
    myarr.append(x.get_text())
for x in knicksresult:
    myarr.append(x.get_text())
for x in thunderresult:
    myarr.append(x.get_text())
for x in magicresult:
    myarr.append(x.get_text())
for x in philadelphiaresult:
    myarr.append(x.get_text())
for x in sunsresult:
    myarr.append(x.get_text())
for x in trailblazersresult:
    myarr.append(x.get_text())
for x in kingsresult:
    myarr.append(x.get_text())
for x in spursresult:
    myarr.append(x.get_text())
for x in jazzresult:
    myarr.append(x.get_text())
for x in raptorsresult:
    myarr.append(x.get_text())
for x in wizardsresult:
    myarr.append(x.get_text())

for x in myarr:
    if "Rookie" in x:
        x = x.replace("Rookie","")
    print(x)
# ------- THIS WORKS ----------#

    #print(prettyhawks.find_all('a'))
