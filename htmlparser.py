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

#hawksratings = hawkspage.find_all('td',class_= "sorting_1")
ratingsarr = []
trashratingsarr = []
teamresultsarr = [hawkspage,celticspage,netspage,hornetspage,bullspage,cavalierspage,maverickspage,nuggetspage,pistonspage,warriorspage,rocketspage,pacerspage,clipperspage,lakerspage,grizzliespage,heatpage,buckspage,timberwolvespage,pelicanspage,knickspage,thunderpage,magicpage,philadelphiapage,sunspage,trailblazerspage,kingspage,spurspage,jazzpage,raptorspage,wizardspage]

# vvvvv MULTICASE TEAM RATING vvvvv #
'''for x in teamresultsarr:
   teamspan = x.find_all('span')
   for y in teamspan:
      trashratingsarr.append(y.get_text())
   for z in trashratingsarr:
      if len(z) == 2:
         z = int(z)
         ratingsarr.append(z)
#ratingsarr.sort(reverse=True)
for x in ratingsarr:
  print(x)'''
# ^^^^^ MULTICASE TEAM RATING ^^^^^ #
   

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

# VVVVV WORKING SOLO CASE VVVVV #
# KEEP IN CASE OTHERS FUCK UP #
'''for x in hawksspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x)==2:
       x=int(x)
       ratingsarr.append(x)
ratingsarr.sort(reverse=True)
trashratingsarr = [] #reset array after each time
'''
# ^^^^^ WORKING SOLO CASE ^^^^^ #

for x in hawksspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      hawksratings.append(x)
hawksratings.sort(reverse = True)
trashratingsarr = []

for x in celticsspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      celticsratings.append(x)
celticsratings.sort(reverse = True)
trashratingsarr = []

for x in netsspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      netsratings.append(x)
netsratings.sort(reverse = True)
trashratingsarr = []

for x in hornetsspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      hornetsratings.append(x)
hornetsratings.sort(reverse = True)
trashratingsarr = []

for x in bullsspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      bullsratings.append(x)
bullsratings.sort(reverse = True)
trashratingsarr = []

for x in cavaliersspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      cavaliersratings.append(x)
cavaliersratings.sort(reverse = True)
trashratingsarr = []

for x in mavericksspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      mavericksratings.append(x)
mavericksratings.sort(reverse = True)
trashratingsarr = []

for x in nuggetsspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      nuggetsratings.append(x)
nuggetsratings.sort(reverse = True)
trashratingsarr = []

for x in pistonsspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      pistonsratings.append(x)
pistonsratings.sort(reverse = True)
trashratingsarr = []

for x in warriorsspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      warriorsratings.append(x)
warriorsratings.sort(reverse = True)
trashratingsarr = []

for x in rocketsspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      rocketsratings.append(x)
rocketsratings.sort(reverse = True)
trashratingsarr = []

for x in pacersspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      pacersratings.append(x)
pacersratings.sort(reverse = True)
trashratingsarr = []

for x in clippersspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      clippersratings.append(x)
clippersratings.sort(reverse = True)
trashratingsarr = []

for x in lakersspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      lakersratings.append(x)
lakersratings.sort(reverse = True)
trashratingsarr = []

for x in grizzliesspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      grizzliesratings.append(x)
grizzliesratings.sort(reverse = True)
trashratingsarr = []

for x in heatspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      heatratings.append(x)
heatratings.sort(reverse = True)
trashratingsarr = []

for x in bucksspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      bucksratings.append(x)
bucksratings.sort(reverse = True)
trashratingsarr = []

for x in timberwolvesspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      timberwolvesratings.append(x)
timberwolvesratings.sort(reverse = True)
trashratingsarr = []

for x in pelicansspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      pelicansratings.append(x)
pelicansratings.sort(reverse = True)
trashratingsarr = []

for x in knicksspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      knicksratings.append(x)
knicksratings.sort(reverse = True)
trashratingsarr = []

for x in thunderspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      thunderratings.append(x)
thunderratings.sort(reverse = True)
trashratingsarr = []

for x in magicspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      magicratings.append(x)
magicratings.sort(reverse = True)
trashratingsarr = []

for x in philadelphiaspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      philadelphiaratings.append(x)
philadelphiaratings.sort(reverse = True)
trashratingsarr = []

for x in sunsspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      sunsratings.append(x)
sunsratings.sort(reverse = True)
trashratingsarr = []

for x in trailblazersspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      trailblazersratings.append(x)
trailblazersratings.sort(reverse = True)
trashratingsarr = []

for x in kingsspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      kingsratings.append(x)
kingsratings.sort(reverse = True)
trashratingsarr = []

for x in spursspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      spursratings.append(x)
spursratings.sort(reverse = True)
trashratingsarr = []

for x in jazzspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      jazzratings.append(x)
jazzratings.sort(reverse = True)
trashratingsarr = []

for x in raptorsspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      raptorsratings.append(x)
raptorsratings.sort(reverse = True)
trashratingsarr = []

for x in wizardsspan:
   trashratingsarr.append(x.get_text())
for x in trashratingsarr:
   if len(x) == 2:
      x = int(x)
      wizardsratings.append(x)
wizardsratings.sort(reverse = True)
trashratingsarr = []

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

#for x in hawksratings:
  #  myarr.append(x.get_text())
for x in hawksplayers:
   x = x.encode("utf-8")
   if "\xe2\x80\x99" in x:
      x = x.replace("\xe2\x80\x99","'")
   if "Rookie" in x:
        x = x.replace("Rookie","")
for x in celticsplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in netsplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in hornetsplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in bullsplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in cavaliersplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in mavericksplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in nuggetsplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in pistonsplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in warriorsplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in rocketsplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in pacersplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in clippersplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in lakersplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in grizzliesplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in heatplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in bucksplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in timberwolvesplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in pelicansplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in knicksplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in thunderplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in magicplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in philadelphiaplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in sunsplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in trailblazersplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in kingsplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in spursplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in jazzplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in raptorsplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")
for x in wizardsplayers:
    if "Rookie" in x:
        x = x.replace("Rookie","")

#for x in hawksplayers:
  # x = x.encode("utf-8")
#hawksplayers = [x.encode('utf8') for x in hawksplayers]
print(hawksplayers)
print(hawksratings)
#hawksdictionary = dict(zip(hawksplayers,hawksratings))
#print(hawksdictionary)

# ------- THIS WORKS ----------#

    #print(prettyhawks.find_all('a'))
