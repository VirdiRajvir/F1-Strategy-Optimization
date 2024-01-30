
def find_total_time(compound, laps):
    total_time = 0
    if compound == "hards":  # function for hards as found by regression model
        for i in range(0, laps): # every possible stint time
            total_time += max(-0.0001212*i.__pow__(3) + 0.002951*i.__pow__(2) + 0.05224*i + 76.76, 0.0242407*i.__pow__(3)-2.03173*i.__pow__(2)+56.7639*i-449.613-0.5)
    elif compound == "softs": # function for softs as found by regression model
        for i in range(0, laps): # every possible stint time
            total_time += 0.0007749 * (i).__pow__(4) - 0.02119 * (i).__pow__(3) + 0.1849 * (i).__pow__(2) - 0.4158 * (
                i) + 76.73
    else:   # function for meds as found by regression model
        for i in range(0, laps): # every possible stint time
            total_time += 0.0001064*i.__pow__(4)- 0.005232*i.__pow__(3) + 0.08294*i.__pow__(2) - 0.4283*i + 77.77
    return float(f'{total_time:.4}')  # return total time spent on stint