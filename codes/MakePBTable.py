###
#   File name  : MakePBTable.py
#   Author     : Hyunjin Kim
#   Date       : August 15, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Make a matrix (table) of Pitcher - Hitter based on Batting Average
#                The rows are pitchers and the columns are hitters
#                With given year, only collect data since that year
#
#                There should be 6 tables:
#                1. AB: At-Bat
#                2. H: Hit
#                3. HR: Home Run
#                3. BB: Walk
#                4. AVG: Batting Average
#                5. OBP: On Base Percentage
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
    ALL_PLAYERS = load_all_players("F:/Documents/PycharmProjects/MLB_Analysis/data/regular/", 1990, 2018)
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


### a function to return 3-dimensional statistical table of given pitchers vs given batters
def make_stat_table(PITCHERS, BATTERS, dataPath, start_year, end_year):
    ### get unique pitcher and batter lists
    unique_pitcher_list = list(sorted(set([x[0] for x in PITCHERS])))
    unique_batter_list = list(sorted(set([x[0] for x in BATTERS])))

    ### statistics array
    statistics = ['AB', 'H', 'HR', 'BB', 'AVG', "OBP"]

    ### create an empty stat table
    stat_table = {z : {y : {x : -1 for x in statistics} for y in unique_batter_list} for z in unique_pitcher_list}

    ### fill out the stat table - compute the statistics
    for year in range(start_year, end_year+1):
        with open(dataPath+"TEAM"+str(year), 'r') as f1:
            teams = list(csv.reader(f1))
        for team in teams:
            with open(dataPath+str(year)+team[0]+".EV"+team[1], 'r') as f2:
                events = list(csv.reader(f2))





