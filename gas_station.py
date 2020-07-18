'''
	There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
	You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
	Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.
'''
def gas_station(gas, cost):
    marker = 0
    diff =0
    l = len(gas)
    sum=0
    total_sum=0
    for i in range(l):
        diff = gas[i]-cost[i]
        sum+=diff
        total_sum+=diff
        if sum<0:
            sum = 0
            marker+=(i+1)
    if total_sum>=0:
        return marker
    return -1   
