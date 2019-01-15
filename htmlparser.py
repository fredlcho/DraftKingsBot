from bs4 import BeautifulSoup
from sets import Set
import requests #allows us to download html from urls
import csv
import copy
import pandas as dapanda
import itertools as myitertool
import sys


def cleannames(array):
    result = []
    result = [x.encode('utf8') for x in array]
    result = [x.replace("Rookie","") for x in result]
    result = [x.replace(".","") for x in result]
    result = [x.replace("Jr","") for x in result]
    result = [x.replace("\xe2\x80\x99","") for x in result]
    result = [x.rstrip() for x in result]
    return result

starters_total_salary = int(sys.argv[2])

nba_2k19 = "https://www.2kratings.com/nba2k19-team/"
nba_teams = ["atlanta-hawks","boston-celtics","brooklyn-nets","charlotte-hornets","chicago-bulls","cleveland-cavaliers",
"dallas-mavericks","denver-nuggets","detroit-pistons","golden-state-warriors","houston-rockets","indiana-pacers",
"los-angeles-clippers","los-angeles-lakers","memphis-grizzlies","miami-heat","milwaukee-bucks","minnesota-timberwolves",
"new-orleans-pelicans","new-york-knicks","oklahoma-city-thunder","orlando-magic","philadelphia-76ers","phoenix-suns",
"portland-trail-blazers","sacramento-kings","san-antonio-spurs","utah-jazz","toronto-raptors","washington-wizards"]

players_array = []
bad_ratings = []
for x in nba_teams:
    #print(nba2k19 + x)
    current_team = requests.get(nba_2k19 + x)
    team_page = BeautifulSoup(current_team.content,'html.parser')
    team_result = team_page.find_all('td',class_ = "roster-entry")
    team_span = team_page.find_all('span')
    for y in team_result:
        players_array.append(y.get_text())
    for z in team_span:
        bad_ratings.append(z.get_text())


players = cleannames(players_array)
ratings = [int(x) for x in bad_ratings if len(x) == 2]
players_and_ratings = {player:rating for player,rating in zip(players,ratings)}
#print(playersandratings)

# ------- THIS WORKS ----------#

column_names = ['Position', 'Name+ID','Name','ID','RosterPosition','Salary','Gameinfo','Teamabbr','AvgPPG']
mycsv = dapanda.read_csv(sys.argv[1],header = None)
mycsv.columns = column_names
#print(mycsv.Name)
#csvcolumns = [x.replace(" ","") for x in mycsv.columns]

#print(mycsv)
dirty_name_list = [x for x in mycsv.Name]
dirty_name_list.pop(0)
name_list = cleannames(dirty_name_list)
# for x in namelist:
#     print(x)
tonights_player_2kratings = [players_and_ratings.get(x) for x in name_list]
salary_list = [x for x in mycsv.Salary]
salary_list.pop(0)
salary_list = [int(x) for x in salary_list]
position_list = [x for x in mycsv.Position]
position_list.pop(0)

salary_position_2krating = zip(salary_list,position_list,tonights_player_2kratings)
dirty_player_dict = {key:value for key,value in zip(name_list,salary_position_2krating)} #dirty b/c there's players with a "None"
                                                                                      #2k rating (b/c they're not important enough
                                                                                      #that their names are correct from both draftkings
                                                                                      #and 2k rating website)
player_dict = {key:value for key,value in dirty_player_dict.iteritems() if value[2] is not None}
pg = {}
sg = {}
sf = {}
pf = {}
center = {}
pg_list = []
sg_list = []
sf_list = []
pf_list = []
c_list = []
for x in player_dict:
    # print(x,playerdict.get(x)[0]
    player_value = player_dict.get(x)
    position = player_dict.get(x)[1]
    if position == 'PG':
        pg[x] = 1
    elif position == 'SG':
        sg[x] = 1
    elif position == 'SF':
        sf[x] = 1
    elif position == 'PF':
        pf[x] = 1
    elif position == 'C':
        center[x] = 1
    elif position == 'PG/SG':
        pg[x] = 1
        sg[x] = 1
    elif position == 'PG/SF':
        pg[x] = 1
        sf[x] = 1
        #pg_list.append(x)
        #sf_list.append(x)
    elif position == 'SG/SF':
        sg[x] = 1
        sf[x] = 1
    elif position == 'SF/PF':
        sf[x] = 1
        pf[x] = 1
    elif position == 'PF/C':
        pf[x] = 1
        center[x] = 1

def calculate_average(array,dictionary):
    answer = 0
    for x in array:
        answer += dictionary.get(x)[2]
    return answer / len(array)

def calculate_salary(array,dictionary):
    answer1 = 0
    for x in array:
        answer1 += dictionary.get(x)[0]
        #print(dictionary.get(x)[0])
    #print(answer1, "this is answer 1")
    return answer1


answer = [None] * 5
finalanswer = []
# for v,w,x,y,z in zip(pg,sg,sf,pf,center):
#     print(v,w,x,y,z)
average = 0
temp_average = 0
total_salary = 0
for a in pg:
    if a in sg:
        sg.pop(a)
        sg_list.append(a)
    if a in sf:
        sf.pop(a)
        sf_list.append(a)
    answer[0] = a
    for b in sg:
        if b in sf:
            sf.pop(b)
            sf_list.append(b)
        answer[1] = b
        for c in sf:
            if c in pf:
                pf.pop(c)
                pf_list.append(c)
            answer[2] = c
            for d in pf:
                if d in center:
                    center.pop(d)
                    c_list.append(d)
                answer[3] = d
                for e in center:
                    answer[4] = e
                    temp_average = calculate_average(answer,player_dict)
                    total_salary = calculate_salary(answer,player_dict)
                    if temp_average > average and total_salary <= starters_total_salary:
                        average = temp_average
                        finalanswer = answer[:]
                if c_list:
                    center[c_list.pop()] = 1
            if pf_list:
                pf[pf_list.pop()] = 1
        if sf_list:
            sf[sf_list.pop()] = 1
    if sg_list:
        sg[sg_list.pop()] = 1
    if sf_list:
        sf[sf_list.pop()] = 1


print(finalanswer)
for x in finalanswer:
     print(player_dict.get(x)[0])
print(average,total_salary,starters_total_salary)
