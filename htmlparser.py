from bs4 import BeautifulSoup
from sets import Set
import requests #allows us to download html from urls
import csv
import pandas as dapanda
import itertools as myitertool
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

detroitpistons = requests.get("http://www.2kratings.com/nba2k18-team/detroit-pistons")

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
#print(utahjazz)
#print(torontoraptors)
#print(detroitpistons)
#print(washingtonwizards)
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
#print(sunspage)
#print(pistonspage)
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

#print(pistonsresult)
#hawksratings = hawkspage.find_all('td',class_= "sorting_1")
ratingsarr = []
trashratingsarr = []
teamresultsarr = [hawkspage,celticspage,netspage,hornetspage,bullspage,cavalierspage,maverickspage,nuggetspage,pistonspage,warriorspage,rocketspage,pacerspage,clipperspage,lakerspage,grizzliespage,heatpage,buckspage,timberwolvespage,pelicanspage,knickspage,thunderpage,magicpage,philadelphiapage,sunspage,trailblazerspage,kingspage,spurspage,jazzpage,raptorspage,wizardspage]
   

hawksspan = hawkspage.find_all('span')
celticsspan = celticspage.find_all('span')
netsspan = netspage.find_all('span')
hornetsspan = hornetspage.find_all('span')
bullsspan = bullspage.find_all('span')
cavaliersspan = cavalierspage.find_all('span')
mavericksspan = maverickspage.find_all('span')
nuggetsspan = nuggetspage.find_all('span')
pistonsspan = pistonspage.find_all('span')
warriorsspan = warriorspage.find_all('span')
rocketsspan = rocketspage.find_all('span')
pacersspan = pacerspage.find_all('span')
clippersspan = clipperspage.find_all('span')
lakersspan = lakerspage.find_all('span')
grizzliesspan = grizzliespage.find_all('span')
heatspan = heatpage.find_all('span')
bucksspan = buckspage.find_all('span')
timberwolvesspan = timberwolvespage.find_all('span')
pelicansspan = pelicanspage.find_all('span')
knicksspan = knickspage.find_all('span')
thunderspan = thunderpage.find_all('span')
magicspan = magicpage.find_all('span')
philadelphiaspan = philadelphiapage.find_all('span')
sunsspan = sunspage.find_all('span')
trailblazersspan = trailblazerspage.find_all('span')
kingsspan = kingspage.find_all('span')
spursspan = spurspage.find_all('span')
jazzspan = jazzpage.find_all('span')
raptorsspan = raptorspage.find_all('span')
wizardsspan = wizardspage.find_all('span')

hawksratings = []
celticsratings = []
netsratings = []
hornetsratings = []
bullsratings = []
cavaliersratings = []
mavericksratings = []
nuggetsratings = []
pistonsratings = []
warriorsratings = []
rocketsratings = []
pacersratings = []
clippersratings = []
lakersratings = []
grizzliesratings = []
heatratings = []
bucksratings = []
timberwolvesratings = []
pelicansratings = []
knicksratings = []
thunderratings = []
magicratings = []
philadelphiaratings = []
sunsratings = []
trailblazersratings = []
kingsratings = []
spursratings = []
jazzratings = []
raptorsratings = []
wizardsratings = []

spanplayers = [hawksspan, celticsspan, netsspan, hornetsspan, bullsspan, cavaliersspan, mavericksspan, nuggetsspan, pistonsspan, warriorsspan, rocketsspan, pacersspan, clippersspan, lakersspan, grizzliesspan,heatspan, bucksspan, timberwolvesspan, pelicansspan, knicksspan, thunderspan, magicspan, philadelphiaspan, sunsspan, trailblazersspan, kingsspan, spursspan, jazzspan, raptorsspan, wizardsspan]
playerratings = []
for teams in spanplayers:
   for ratings in teams:
      trashratingsarr.append(ratings.get_text())

for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      playerratings.append(x)
#print(playerratings)
   
hawksplayers = []
celticsplayers = []
netsplayers = []
hornetsplayers = []
bullsplayers = []
cavaliersplayers = []
mavericksplayers = []
nuggetsplayers = []
pistonsplayers =  []
warriorsplayers = []
rocketsplayers = []
pacersplayers = []
clippersplayers = []
lakersplayers = []
grizzliesplayers = []
heatplayers = []
bucksplayers = []
timberwolvesplayers = []
pelicansplayers = []
knicksplayers = []
thunderplayers = []
magicplayers = []
philadelphiaplayers = []
sunsplayers = []
trailblazersplayers = []
kingsplayers = []
spursplayers = []
jazzplayers = []
raptorsplayers = []
wizardsplayers = []
for x in hawksresult:
    hawksplayers.append(x.get_text())
for x in celticsresult:
    celticsplayers.append(x.get_text())
for x in netsresult:
    netsplayers.append(x.get_text())
for x in hornetsresult:
    hornetsplayers.append(x.get_text())
for x in bullsresult:
    bullsplayers.append(x.get_text())
for x in cavaliersresult:
    cavaliersplayers.append(x.get_text())
for x in mavericksresult:
    mavericksplayers.append(x.get_text())
for x in nuggetsresult:
    nuggetsplayers.append(x.get_text())
for x in pistonsresult:
    pistonsplayers.append(x.get_text())
for x in warriorsresult:
    warriorsplayers.append(x.get_text())
for x in rocketsresult:
    rocketsplayers.append(x.get_text())
for x in pacersresult:
    pacersplayers.append(x.get_text())
for x in clippersresult:
    clippersplayers.append(x.get_text())
for x in lakersresult:
    lakersplayers.append(x.get_text())
for x in grizzliesresult:
    grizzliesplayers.append(x.get_text())
for x in heatresult:
    heatplayers.append(x.get_text())
for x in bucksresult:
    bucksplayers.append(x.get_text())
for x in timberwolvesresult:
    timberwolvesplayers.append(x.get_text())
for x in pelicansresult:
    pelicansplayers.append(x.get_text())
for x in knicksresult:
    knicksplayers.append(x.get_text())
for x in thunderresult:
    thunderplayers.append(x.get_text())
for x in magicresult:
    magicplayers.append(x.get_text())
for x in philadelphiaresult:
    philadelphiaplayers.append(x.get_text())
for x in sunsresult:
    sunsplayers.append(x.get_text())
for x in trailblazersresult:
    trailblazersplayers.append(x.get_text())
for x in kingsresult:
    kingsplayers.append(x.get_text())
for x in spursresult:
    spursplayers.append(x.get_text())
for x in jazzresult:
    jazzplayers.append(x.get_text())
for x in raptorsresult:
    raptorsplayers.append(x.get_text())
for x in wizardsresult:
    wizardsplayers.append(x.get_text())
#print(wizardsplayers)
#print(pistonsplayers)
playerroster = [hawksplayers, celticsplayers, netsplayers, hornetsplayers, bullsplayers, cavaliersplayers, mavericksplayers, nuggetsplayers, pistonsplayers, warriorsplayers, rocketsplayers, pacersplayers, clippersplayers, lakersplayers, grizzliesplayers, heatplayers, bucksplayers, timberwolvesplayers, pelicansplayers, knicksplayers, thunderplayers, magicplayers, philadelphiaplayers, sunsplayers, trailblazersplayers, kingsplayers, spursplayers, jazzplayers, raptorsplayers, wizardsplayers]
soloplayerroster = []
for teams in playerroster:
   # print("1")
    for players in teams:
      # print("2")
       player = players.encode('ascii','ignore')
       player = players.replace("Rookie","")
       soloplayerroster.append(player)

soloplayerroster = [x.encode('utf8') for x in soloplayerroster]
soloplayerroster = [x.replace("Rookie","") for x in soloplayerroster]
soloplayerroster = [x.replace("\xe2\x80\x99","'") for x in soloplayerroster]
soloplayerroster = [x.rstrip() for x in soloplayerroster]
#print(soloplayerroster)
thenbaroster = dict(zip(soloplayerroster,playerratings))
#print(thenbaroster.get('Blake Griffin'))
#for x,y in thenbaroster.items():
#   print(x,y)
#for x in sorted(thenbaroster.iterkeys()):
#   print "%s: %s" % (x, thenbaroster[x])
#hawksdictionary = dict(zip(hawksplayers,hawksratings))
#print(hawksdictionary)

#print(netsplayers)

# ------- THIS WORKS ----------#

    #print(prettyhawks.find_all('a'))
'''
with open('DKSalaries.csv') as csvfile:
   lines = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
   for x in lines:
      print x
'''

mycsv = dapanda.read_csv('pid-file-nba.csv',names = ['Position', 'Name+ID','Name','ID','RosterPosition','Salary','Gameinfo','Teamabbr'])
#print(mycsv)
#csvcolumns = [x.replace(" ","") for x in mycsv.columns]

#print(mycsv)



#print(columns)
namecolumn = mycsv.Name
salarycolumn = mycsv.Salary
positioncolumn = mycsv.Position
twokratingg = []
for x in namecolumn:
   if thenbaroster.get(x) != None:
      twokratingg.append(thenbaroster.get(x))

#fix these lists
namecolumn = list(namecolumn)
namecolumn.pop(0)
namecolumn = [x for x in namecolumn if str(x) != 'nan']
#print(namecolumn)

salarycolumn = list(salarycolumn)
salarycolumn.pop(0)
salarycolumn = [x for x in salarycolumn if str(x) != 'nan']
salarycolumn = [int(x) for x in salarycolumn]

positioncolumn = list(positioncolumn)
positioncolumn.pop(0)

playerinfo = zip(namecolumn,salarycolumn,twokratingg,positioncolumn)
#for x in playerinfo:
#   print(x)

#pg = []
pgwithpgsg = []
#sg = []
sgwithsgsf = []
#sf = []
sfwithsfpf = []
#pf = []
pfwithpfc = []
c = []
pgandsg = []
for x in range(0,len(playerinfo)):
   if playerinfo[x][3] == 'PG':
      pg.append(playerinfo[x])
   else if playerinfo[x][3] == 'PG/SG':
      pg.append(playerinfo[x])
      sg.append(playerinfo[x])
   else if playerinfo[x][3] == 'SG':
      sg.append(playerinfo[x])
   else if playerinfo[x][3] == 'SG/SF':
      sg.append(playerinfo[x])
      sf.append(playerinfo[x])
   else if playerinfo[x][3] == 'SF':
      sf.append(playerinfo[x])
   else if playerinfo[x][3] == 'SF/PF':
      sf.append(playerinfo[x])
      pf.append(playerinfo[x])
   else if playerinfo[x][3] == 'PF':
      pf.append(playerinfo[x])
   else if playerinfo[x][3] == 'PF/C':
      pf.append(playerinfo[x])
      c.append(playerinfo[x])
   else if layerinfo[x][3] == 'C':
      c.append(playerinfo[x])

def calculate(pg, sg, sf, pf, c):
   result = []
   temp = []
   for a in pg:
      for b in sg:
         for c in sf:
            for d in pf:
               for e in c:
   
for x in pg:
   print(x)
   print('hey')
