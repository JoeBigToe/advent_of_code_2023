path = "."

import math

gears = {}
m =[]
parts = []

def symbol_lookup(line, j, number, found):   
    try:
        if not(m[line][j].isdigit()) and m[line][j] != ".":
            found = True
            if m[line][j] == "*":
                if f'{line}-{j}' not in gears.keys():
                    gears.update({f'{line}-{j}':[number]})
                else:
                    gears[f'{line}-{j}'].append(number)
    except IndexError:
        pass

    return found

def validate(line, lower_band, size):
    found = False
    number = int("".join(m[line][lower_band:lower_band+size]))
    
    for j in range(lower_band -1, lower_band + size + 1):
        found = symbol_lookup(line-1, j, number, found)
        found = symbol_lookup(line+1, j, number, found)
    found = symbol_lookup(line, lower_band-1, number, found)
    found = symbol_lookup(line, lower_band+size, number, found)

    if found:
        return number
    else: 
        return False
    

with open(f'{path}/puzzle') as fp:
    for line in fp.readlines():
        m.append([c for c in line.strip()])

    for line in range(len(m)):
        is_number = False
        lower_band = 0
        size = 0
        for i in range(len(m[line])):
            if m[line][i].isdigit():
                size += 1
                if not(is_number):
                    lower_band = i
                    is_number = True
            elif is_number:
                if n := validate(line, lower_band, size):
                    parts.append(n)
                is_number = False
                size = 0
            else:
                size = 0

        if is_number:
            if n := validate(line, lower_band, size):
                parts.append(n)
            is_number = False
            size = 0

print(f'Part1: {sum(parts)}')

sum = 0
for key in gears.keys():
    if len(gears[key]) > 1:
        sum += math.prod(gears[key])

print(f'Part2: {sum}')