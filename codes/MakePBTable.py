###
#   File name  : MakePBTable.py
#   Author     : Hyunjin Kim
#   Date       : August 15, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Make a matrix (table) of Pitcher - Hitter based on Batting Average
#                The rows are pitchers and the columns are hitters
#                With given year, only collect data since that year
#
#                There should be 9 tables:
#                1. AB: At-Bat
#                2. H: Hit
#                3. HR: Home Run
#                4. SF: Sacrifice Fly
#                5. K: Strike Out
#                6. BB: Walk
#                7. HP: Hit by Pitch
#                8. AVG: Batting Average
#                9. OBP: On Base Percentage
#
#   Instruction
#               1. import MakePBTable.py
#               2. Run the function MakePBTable.start()
#               3. The results will be generated in the output path
###

### import modules
import timeit
import csv
import pickle

### a function starting this script
def start():
    print("MakePBTable.py")

    ### parameter setting
    # data_path = "E:/HJ_Personal/Python/MLB_Analysis/data/regular/"
    data_path = "F:/Documents/PycharmProjects/MLB_Analysis/data/regular/"
    start_year = 1990
    end_year = 2018
    out_path = "F:/Documents/PycharmProjects/MLB_Analysis/data/PBTable.obj"

    start_time = timeit.default_timer()

    ### player list
    all_players = load_all_players(data_path, start_year, end_year)
    pitchers = get_pitchers_only(all_players)
    batters = get_batters_only(all_players)

    ### calculate pitcher-batter table
    st_table = make_stat_table(pitchers, batters, data_path, start_year, end_year)

    ### save the result table
    file_pi = open(out_path, 'wb')
    pickle.dump(st_table, file_pi)

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
def make_stat_table(pitchers, batters, data_path, start_year, end_year):
    ### get unique pitcher and batter lists
    unique_pitcher_list = list(sorted(set([x[0] for x in pitchers])))
    unique_batter_list = list(sorted(set([x[0] for x in batters])))

    ### usually pitchers only pitch and batters only hit
    ### but sometimes (especially in NL), pitchers can be batters as well and vice versa
    ### so we consider all players can be potentially both pitchers & batters
    unique_player_list = list(sorted(set(unique_pitcher_list + unique_batter_list)))

    ### statistics array
    statistics = ['AB', 'H', 'HR', 'SF', 'K', 'BB', 'HP', 'AVG', "OBP"]

    ### create an empty stat table
    stat_table = {z : {y : {x : 0 for x in statistics} for y in unique_player_list} for z in unique_player_list}

    ### set AVG and OBP as -1 (because 0 does not mean NA)
    for pitcher in stat_table.keys():
        for batter in stat_table[pitcher].keys():
            stat_table[pitcher][batter]['AVG'] = -1
            stat_table[pitcher][batter]['OBP'] = -1

    ### fill out the stat table - compute the statistics
    for year in range(start_year, end_year+1):
        with open(data_path+"TEAM"+str(year), 'r') as f1:
            teams = list(csv.reader(f1))
        for team in teams:
            with open(data_path+str(year)+team[0]+".EV"+team[1], 'r') as f2:
                events = list(csv.reader(f2))
            ### there are always two (current) pitchers for each team
            pitcher = ["", ""]
            ### read each event and update the statistics
            for i in range(len(events)):
                if (events[i][0] == 'start' or events[i][0] == 'sub') and events[i][5] == '1':
                    pitcher[int(events[i][3])] = events[i][1]
                elif events[i][0] == 'play':
                    stat_table[pitcher[int(not int(events[i][2]))]][events[i][3]]['AB'] += 1
                    result = events[i][6][0]
                    if events[i][6][0:2] == 'HR' or events[i][6][0:2] == 'HP' or events[i][6][0:2] == 'BB':
                        result = events[i][6][0:2]
                    if result == 'S' or result == 'D' or result == 'T' or result == 'HR':
                        stat_table[pitcher[int(not int(events[i][2]))]][events[i][3]]['H'] += 1
                        stat_table[pitcher[int(not int(events[i][2]))]][events[i][3]]['AVG'] = (stat_table[pitcher[int(not int(events[i][2]))]][events[i][3]]['H']
                                                                                                / stat_table[pitcher[int(not int(events[i][2]))]][events[i][3]]['AB'])
                        if result == 'HR':
                            stat_table[pitcher[int(not int(events[i][2]))]][events[i][3]]['HR'] += 1
                    elif result == 'K':
                        stat_table[pitcher[int(not int(events[i][2]))]][events[i][3]]['K'] += 1
                    elif result == 'W' or result == 'I':
                        stat_table[pitcher[int(not int(events[i][2]))]][events[i][3]]['BB'] += 1
                    elif result == 'HP':
                        stat_table[pitcher[int(not int(events[i][2]))]][events[i][3]]['HP'] += 1
                    elif 'SF' in events[i][6]:
                        stat_table[pitcher[int(not int(events[i][2]))]][events[i][3]]['SF'] += 1
                    stat_table[pitcher[int(not int(events[i][2]))]][events[i][3]]['OBP'] = ((stat_table[pitcher[int(not int(events[i][2]))]][events[i][3]]['H']
                                                                                           + stat_table[pitcher[int(not int(events[i][2]))]][events[i][3]]['BB']
                                                                                           + stat_table[pitcher[int(not int(events[i][2]))]][events[i][3]]['HP'])
                                                                                            / (stat_table[pitcher[int(not int(events[i][2]))]][events[i][3]]['AB']
                                                                                              + stat_table[pitcher[int(not int(events[i][2]))]][events[i][3]]['BB']
                                                                                              + stat_table[pitcher[int(not int(events[i][2]))]][events[i][3]]['HP']
                                                                                              + stat_table[pitcher[int(not int(events[i][2]))]][events[i][3]]['SF']))

    return stat_table


start()
