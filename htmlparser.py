from bs4 import BeautifulSoup
import requests #allows us to download html from urls
import csv
import copy
import pandas as dapanda
import itertools as myitertool
import sys


def cleannames(array):
    # result = [x.decode('utf8') for x in array]
    result = [x.replace("Rookie","") for x in array]
    result = [x.replace(".","") for x in result]
    result = [x.replace("Jr","") for x in result]
    result = [x.replace("\xe2\x80\x99","") for x in result]
    result = [x.rstrip() for x in result]
    return result

def calculate_average(array,dictionary):
    answer = 0
    for x in array:
        answer += dictionary.get(x)[2]
    return answer / len(array)

def calculate_salary(array,dictionary):
    answer1 = 0
    for x in array:
        answer1 += dictionary.get(x)[0]
    return answer1

def calculate_fantasypts(array,dictionary):
    answer = 0
    for x in array:
        answer += dictionary.get(x)[3]
    return answer

def merge_dictionaries(*dict_args):
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

def remove_players(array,dictionary):
    for x in array:
        dictionary.pop(x)
    return dictionary


def optimize():
        starters_total_salary = 35000
        reserve_salary = 15000

        nba_2k19 = "https://www.2kratings.com/nba2k19-team/"
        nba_teams = ["atlanta-hawks","boston-celtics","brooklyn-nets","charlotte-hornets","chicago-bulls","cleveland-cavaliers",
        "dallas-mavericks","denver-nuggets","detroit-pistons","golden-state-warriors","houston-rockets","indiana-pacers",
        "los-angeles-clippers","los-angeles-lakers","memphis-grizzlies","miami-heat","milwaukee-bucks","minnesota-timberwolves",
        "new-orleans-pelicans","new-york-knicks","oklahoma-city-thunder","orlando-magic","philadelphia-76ers","phoenix-suns",
        "portland-trail-blazers","sacramento-kings","san-antonio-spurs","utah-jazz","toronto-raptors","washington-wizards"]

        players_array = []
        bad_ratings = []
        for x in nba_teams:
            current_team = requests.get(nba_2k19 + x)
            team_page = BeautifulSoup(current_team.content,'html.parser')
            team_result = team_page.find_all('td',class_ = "roster-entry")
            team_span = team_page.find_all('span')
            for y in team_result:
                players_array.append(y.get_text())
            for z in team_span:
                bad_ratings.append(z.get_text())

        removelist = ["Kevin Love", "Danilo Gallinari", "Tristan Thompson","Jordan Clarkson","Wendell Carter Jr.","Chandler Hutchison","John Henson","David Nwaba","Denzel Valentine","Carmelo Anthony","Luc Mbah a Moute"]
        removelist = cleannames(removelist)

        players = cleannames(players_array)
        ratings = [int(x) for x in bad_ratings if len(x) == 2]
        players_and_ratings = {player:rating for player,rating in zip(players,ratings)}
        players_and_ratings = remove_players(removelist,players_and_ratings)

        column_names = ['Position', 'Name+ID','Name','ID','RosterPosition','Salary','Gameinfo','Teamabbr','AvgPPG']
        mycsv = dapanda.read_csv(sys.argv[1],header = None)
        mycsv.columns = column_names

        dirty_name_list = [x for x in mycsv.Name]
        dirty_name_list.pop(0)
        name_list = cleannames(dirty_name_list)
        tonights_player_2kratings = [players_and_ratings.get(x) for x in name_list]
        salary_list = [x for x in mycsv.Salary]
        salary_list.pop(0)
        salary_list = [int(x) for x in salary_list]
        position_list = [x for x in mycsv.Position]
        position_list.pop(0)
        fantasy_points_list = [x for x in mycsv.AvgPPG]
        fantasy_points_list.pop(0)
        fantasy_points_list = [float(x) for x in fantasy_points_list]

        salary_position_2krating_fantasypoints = zip(salary_list,position_list,tonights_player_2kratings,fantasy_points_list)
        dirty_player_dict = {key:value for key,value in zip(name_list,salary_position_2krating_fantasypoints)} #dirty b/c there's players with a "None"
                                                                                              #2k rating (b/c they're not important enough
                                                                                              #that their names are correct from both draftkings
                                                                                              #and 2k rating website)
                                                                                              # || if value[1] > 3700
                                                                                              # value[0]>4500
        player_dict = {key:value for key,value in dirty_player_dict.items() if value[2] is not None and value[3]> 16}

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
            elif position == 'SG/SF':
                sg[x] = 1
                sf[x] = 1
            elif position == 'SF/PF':
                sf[x] = 1
                pf[x] = 1
            elif position == 'PF/C':
                pf[x] = 1
                center[x] = 1

        answer = [None] * 5
        finalanswer = []
        average = 0
        temp_average = 0
        fantasy_average = 0
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
                            fantasypts = calculate_fantasypts(answer,player_dict)
                            #print(total_salary)
                            if temp_average > average and total_salary <= starters_total_salary and fantasypts > fantasy_average:
                                fantasy_average = fantasypts
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

        #print(finalanswer)

        for x in finalanswer:
            if x in pg:
                pg.pop(x)
            if x in sg:
                sg.pop(x)
            if x in sf:
                sf.pop(x)
            if x in pf:
                pf.pop(x)
            if x in center:
                center.pop(x)


        guard_players = merge_dictionaries(pg,sg)
        forward_players = merge_dictionaries(sf,pf)
        all_players = merge_dictionaries(guard_players,forward_players,center)

        forward_players_list = []
        all_players_list = []


        reserves = [None] * 3
        reserve_answer = []

        reserve_average = 0
        reserve_temp_average = 0
        reserve_fantasy_average = 0
        reserve_total_salary = 0

        for a in guard_players:
            if a in forward_players:
                forward_players.pop(a)
                forward_players_list.append(a)
            if a in all_players:
                all_players.pop(a)
                all_players_list.append(a)
            reserves[0] = a
            for b in forward_players:
                if b in all_players:
                    all_players.pop(b)
                    all_players_list.append(b)
                reserves[1] = b
                for c in all_players:
                    reserves[2] = c
                    # print('hi')
                    reserve_temp_average = calculate_average(reserves,player_dict)
                    reserve_total_salary = calculate_salary(reserves,player_dict)
                    reserve_temp_fantasy_average = calculate_fantasypts(reserves,player_dict)
                    if reserve_temp_average > reserve_average and reserve_total_salary <= reserve_salary and reserve_temp_fantasy_average > reserve_fantasy_average:
                        reserve_fantasy_average = reserve_temp_fantasy_average
                        reserve_average = reserve_temp_average
                        reserve_answer = reserves[:]
                if all_players_list:
                    all_players[all_players_list.pop()] = 1
            if forward_players_list:
                forward_players[forward_players_list.pop()] = 1
            if all_players_list:
                all_players[all_players_list.pop()] = 1

        print(finalanswer)
        print(reserve_answer)

optimize()
