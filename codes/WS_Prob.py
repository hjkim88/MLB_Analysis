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

### a function starting this script
def start():
    print("WS_Prob.py")

    start_time = timeit.default_timer()
    print("")
    print("Execution Time: ", timeit.default_timer() - start_time)


start()
