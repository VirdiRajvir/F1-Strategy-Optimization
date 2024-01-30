import find_total_time as ftt


def pit(strat, laps_rem, _t):
    p1 = strat[0]  # retrieve the first pit compound
    p2 = strat[1]  # retrieve the second pit compound
    if p1 == 's':  # if pit 1 compound is s
        for i in range(1, 28):  # find the total time for softs
            time = ftt.find_total_time('softs', i)
            if p2 == 's':
                for j in range(1, 28):
                    if j + i == laps_rem:
                        time += ftt.find_total_time('softs', j)
                        print(f'2pitsofts+softs: {i}.{j}: {time + _t + 40}')
            elif p2 == 'm':  # find the total time for mediums
                for j in range(1, 36):
                    if j + i == laps_rem:
                        time += ftt.find_total_time('meds', j)
                        print(f'2pitsofts+meds: {i}.{j}: {time + _t + 40}')
            else:  # find the total time for hards
                for j in range(1, 45):
                    if j + i == laps_rem:
                        time += ftt.find_total_time('hards', j)
                        print(f'2pitsofts+hards: {i}.{j}: {time + _t + 40}')
    elif p1 == 'm': # if pit 1 compound is med
        for i in range(1, 36):  # repeat the process for med
            time = ftt.find_total_time('meds', i)
            if p2 == 's':
                for j in range(1, 28):
                    if j + i == laps_rem:
                        time += ftt.find_total_time('softs', j)
                        print(f'2pitmeds+softs: {i}.{j}: {time + _t + 40}')
            else:
                for j in range(1, 45):
                    if j + i == laps_rem:
                        time += ftt.find_total_time('hards', j)
                        print(f'2pitmeds+softs: {i}.{j}: {time + _t + 40}')
    elif p1 == 'h': # if pit 1 compound is hard
        for i in range(1, 46): # repeat
            time = ftt.find_total_time('hards', i)
            if p2 == 's':
                for j in range(1, 28):
                    if j + i == laps_rem:
                        time += ftt.find_total_time('softs', j)
                        print(f'2pitshards+softs: {i}.{j}: {time + _t + 40}')
            elif p2 == 'm':
                for j in range(1, 36):
                    if j + i == laps_rem:
                        time += ftt.find_total_time('meds', j)
                        print(f'2pitshards+meds: {i}.{j}: {time + _t + 40}')
            elif p2 == 'h':
                for j in range(1, 45):
                    if j + i == laps_rem:
                        time += ftt.find_total_time('hards', j)
                        print(f'2pitshards+hards: {i}.{j}: {time + _t + 40}')
            elif p2 == 'n':
                print(f'2pitshards+only: {i}: {time + _t + 40}')
