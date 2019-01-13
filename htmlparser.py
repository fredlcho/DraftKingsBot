from bs4 import BeautifulSoup
from sets import Set
import requests #allows us to download html from urls
import csv
import pandas as dapanda
import itertools as myitertool


def cleannames(array):
    result = []
    result = [x.encode('utf8') for x in array]
    result = [x.replace("Rookie","") for x in result]
    result = [x.replace(".","") for x in result]
    result = [x.replace("\xe2\x80\x99","") for x in result]
    result = [x.rstrip() for x in result]
    return result


nba2k19 = "https://www.2kratings.com/nba2k19-team/"
nbateams = ["atlanta-hawks","boston-celtics","brooklyn-nets","charlotte-hornets","chicago-bulls","cleveland-cavaliers",
"dallas-mavericks","denver-nuggets","detroit-pistons","golden-state-warriors","houston-rockets","indiana-pacers",
"los-angeles-clippers","los-angeles-lakers","memphis-grizzlies","miami-heat","milwaukee-bucks","minnesota-timberwolves",
"new-orleans-pelicans","new-york-knicks","oklahoma-city-thunder","orlando-magic","philadelphia-76ers","phoenix-suns",
"portland-trail-blazers","sacramento-kings","san-antonio-spurs","utah-jazz","toronto-raptors","washington-wizards"]

haha = []
playersarray = []
badratings = []
for x in nbateams:
    #print(nba2k19 + x)
    currentteam = requests.get(nba2k19 + x)
    teampage = BeautifulSoup(currentteam.content,'html.parser')
    teamresult = teampage.find_all('td',class_ = "roster-entry")
    teamspan = teampage.find_all('span')
    for y in teamresult:
        playersarray.append(y.get_text())
    for z in teamspan:
        badratings.append(z.get_text())

ratings = [int(x) for x in badratings if len(x) == 2]

players = cleannames(playersarray)
for x,y in zip(players,ratings):
   print(x,y)

# ------- THIS WORKS ----------#

    #print(prettyhawks.find_all('a'))
'''
'''
with open('DKSalaries.csv') as csvfile:
   lines = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
   for x in lines:
      print x
'''
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
   '''
