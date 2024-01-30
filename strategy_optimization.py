import find_total_time as ftt
import pit as pit

def strategy_optimization():
    for i in range(1, 36):  # iteration for every possible pit for Medium Compound
        time = ftt.find_total_time('meds', i)   # find the total time spent on that compound
        rem_laps = 66 - i  # remaining laps after medium stint
        for strat in ['sm','ms','mh','hm','sh','hs','hh','ss']:
            pit.pit(strat, rem_laps, time)  # function call for rest of the 8 strats


strategy_optimization()