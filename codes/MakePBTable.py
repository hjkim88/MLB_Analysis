###
#   File name  : MakePBTable.py
#   Author     : Hyunjin Kim
#   Date       : August 15, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Make a matrix (table) of Pitcher - Hitter based on Batting Average
#                The rows are pitchers and the columns are hitters
#                With given year, only collect data since that year
#
#                There should be 5 tables:
#                1. AB
#                2. H
#                3. BB
#                4. AVG
#                5. OBP
#
#   Instruction
#               1. import MakePBTable.py
#               2. Run the function MakePBTable.start()
#               3. The results will be generated in the output path
###

### import modules
import timeit
import csv
import numpy
import copy

### a function starting this script
def start():
    print("MakePBTable.py")

    start_time = timeit.default_timer()
    ALL_PLAYERS = load_all_players("E:/HJ_Personal/Python/MLB_Analysis/data/regular/", 1990, 2018)
    PITCHERS = get_pitchers_only(ALL_PLAYERS)
    BATTERS = get_batters_only(ALL_PLAYERS)
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function to get player IDs based on ROS files
### e.g., dataPath="E:/HJ_Personal/Python/MLB_Analysis/data/regular/"
def load_all_players(dataPath, start_year, end_year):
    player_list = []
    for year in range(start_year, end_year+1):
        with open(dataPath+"TEAM"+str(year), 'r') as f1:
            teams = list(csv.reader(f1))
        for team in teams:
            with open(dataPath+team[0]+str(year)+".ROS", 'r') as f2:
                players = list(csv.reader(f2))
            player_list.extend(players)
            player_list = [list(y) for y in sorted(set([tuple(x) for x in player_list]))]

    return player_list


### a function to return pitcher information list only from a given player list
def get_pitchers_only(player_list):
    pitcher_list = []
    for player in player_list:
        if player[6] == "P":
            pitcher_list.append(player)

    return sorted(pitcher_list)


### a function to return batter information list only from a given player list
def get_batters_only(player_list):
    batter_list = []
    for player in player_list:
        if player[6] != "P":
            batter_list.append(player)

    return sorted(batter_list)


### a function to return AtBat table of given pitchers vs given batters
def make_AB_table(PITCHERS, BATTERS, start_year, end_year):
    unique_pitcher_list = list(sorted(set([x[0] for x in PITCHERS])))
    unique_batter_list = list(sorted(set([x[0] for x in BATTERS])))

    AB_table = [[-1]*(len(unique_batter_list)) for i in range(len(unique_pitcher_list))]
    



