###
#   File name  : MakePBTable.py
#   Author     : Hyunjin Kim
#   Date       : August 15, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Make a matrix (table) of Pitcher - Hitter based on Batting Average
#                The rows are pitchers and the columns are hitters
#                With given year, only collect data since that year
#
#   Instruction
#               1. import MakePBTable.py
#               2. Run the function MakePBTable.start()
#               3. The results will be generated in the output path
###

### import modules
import timeit
import csv

### a function starting this script
def start():
    print("MakePBTable.py")

    start_time = timeit.default_timer()

    print("Execution Time: ", timeit.default_timer() - start_time)


### a function to get player IDs based on ROS files
def load_all_players(dataPath, start_year, end_year):
    for year in range(start_year, end_year+1):
        with open(dataPath, 'r') as f:
            teams = list(csv.reader(f))

