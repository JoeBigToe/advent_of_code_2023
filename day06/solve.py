path = '.'

from math import sqrt, floor, ceil
import re

with open(f'{path}/puzzle') as fp:
    for line in fp.readlines():
        if m := re.match(r'Time:\s+([0-9\s]+)', line.strip()):
            # print(m.groups(1)[0])
            times = [int(x) for x in filter(lambda a: a != '', m.groups(1)[0].split(' '))]
            time_part2 = int(m.groups(1)[0].replace(' ', ''))
            

        if m := re.match(r'Distance:\s+([0-9\s]+)', line.strip()):
            # print(m.groups(1)[0])
            distances = [int(x) for x in filter(lambda a: a != '', m.groups(1)[0].split(' '))]
            distance_part2 = int(m.groups(1)[0].replace(' ', ''))
            
sum = 1
for t,d in zip(times, distances):
    sum *= floor(-(-t - sqrt(t*t-4*(d+1))) / 2 ) - ceil(-(-t + sqrt(t*t-4*(d+1))) / 2 ) + 1
print(f"Part 1: {sum}")


t = time_part2
d = distance_part2
print(f"Part 2: {floor(-(-t - sqrt(t*t-4*(d+1))) / 2 ) - ceil(-(-t + sqrt(t*t-4*(d+1))) / 2 ) + 1}")