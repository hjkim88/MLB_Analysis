###
#   File name  : WS_Prob.py
#   Author     : Hyunjin Kim
#   Date       : July 30, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : You have one chance to watch a World Series game and hope it would be the last one
#                of the series. Which one would be the last game with the highest possibility?
#                Four wins out of seven games will decide the champion of the series. If four wins
#                are achieved, there will be no other games for the series.
#
#   Instruction
#               1. import WS_Prob.py
#               2. Run the function WS_Prob.start()
#               3. The results will be generated in the console
###

### import modules
import timeit
import numpy

### a function starting this script
def start():
    print("WS_Prob.py")

    start_time = timeit.default_timer()
    ws_simulation("NYY", "LAD", 0.55, 7, 10000)
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function to simulate world series with a probability
### team1 = a string of the first team's name
### team2 = a string of the second team's name
### prob = a probability that the first team is going to win the second team in one game
### iteration = the number of iterations to repeat the world series for testing
def ws_simulation(team1, team2, prob, max_game_num, iteration):
    print(team1, " vs ", team2)

    win_cut_off = max_game_num // 2 + 1
    unique_nums = list(range(win_cut_off, max_game_num + 1))
    stats = [0] * (len(unique_nums) * 2)

    for i in range(iteration):
        team1_win = 0
        team2_win = 0
        for j in range(max_game_num):
            if team1_win == win_cut_off:
                stats[j-win_cut_off] += 1
                break
            elif team2_win == win_cut_off:
                stats[j] += 1
                break
            else:
                win = numpy.random.choice([team1, team2], size=1, p=[prob, 1 - prob])[0]
                if win == team1:
                    team1_win += 1
                elif win == team2:
                    team2_win += 1
                else:
                    raise ValueError("ERROR: Unspecified team appeared.")
        if team1_win + team2_win == max_game_num:
            if team1_win > team2_win:
                stats[win_cut_off-1] += 1
            else:
                stats[2*win_cut_off-1] += 1

    for i in range(len(stats)):
        if i < len(unique_nums):
            print(team1, " wins in ", unique_nums[i % len(unique_nums)], "th game: ", stats[i])
        else:
            print(team2, " wins in ", unique_nums[i % len(unique_nums)], "th game: ", stats[i])
    print("")
    for i in range(len(unique_nums)):
        print("World Series ended in ", unique_nums[i], "th game: ", stats[i] + stats[i+win_cut_off])


start()
