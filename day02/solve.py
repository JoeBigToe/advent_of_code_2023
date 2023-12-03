path = "."

from itertools import chain 
import re
import math

limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

game = 0
sum = 0

with open(f'{path}/puzzle') as fp:
    for line in fp.readlines():
        possible = True
        game += 1
        plays = list(chain.from_iterable([play.split(', ') for play in line.strip().split(': ')[1].split('; ')]))
        for play in plays:
            m = re.match(r"(\d+) (red|blue|green)", play)
            if int(m.groups(1)[0]) > limits[m.groups(1)[1]]:
                # print(game)
                possible = False
                continue
        if possible:
            sum += game

print(sum)

sum = 0
with open(f'{path}/puzzle') as fp:
    for line in fp.readlines():
        limits = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        plays = list(chain.from_iterable([play.split(', ') for play in line.strip().split(': ')[1].split('; ')]))
        for play in plays:
            m = re.match(r"(\d+) (red|blue|green)", play)
            if int(m.groups(1)[0]) > limits[m.groups(1)[1]]:
                limits[m.groups(1)[1]] = int(m.groups(1)[0])
        sum += math.prod(limits.values())

print(sum)