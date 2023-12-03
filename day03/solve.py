path = "."

import math
gears = {}

def validate(line, lower_band, size):
    found = False
    number = int("".join(m[line][lower_band:lower_band+size]))
    
    for j in range(lower_band -1, lower_band + size + 1):
        try:
            if not(m[line-1][j].isdigit()) and m[line-1][j] != ".":
                found = True
                if m[line-1][j] == "*":
                    if f'{line-1}-{j}' not in gears.keys(): #not(gears[f'{line-1}-{j}']):
                        gears.update({f'{line-1}-{j}':[number]})
                    else:
                        gears[f'{line-1}-{j}'].append(number)
        except IndexError:
            pass
    
    for j in range(lower_band -1, lower_band + size + 1):
        try:
            if not(m[line+1][j].isdigit()) and m[line+1][j] != ".":
                found = True
                if m[line+1][j] == "*":
                    if f'{line+1}-{j}' not in gears.keys(): #not(gears[f'{line+1}-{j}']):
                        gears.update({f'{line+1}-{j}':[number]})
                    else:
                        gears[f'{line+1}-{j}'].append(number)
        except IndexError:
            pass
    
    try:
        if not(m[line][lower_band-1].isdigit()) and m[line][lower_band-1] != ".":
            found = True
            if m[line][lower_band-1] == "*":
                if f'{line}-{lower_band-1}' not in gears.keys(): #not(gears[f'{line}-{lower_band-1}']):
                    gears.update({f'{line}-{lower_band-1}':[number]})
                else:
                    gears[f'{line}-{lower_band-1}'].append(number)
                
    except IndexError:
        pass
    
    try:
        if not(m[line][lower_band+size].isdigit()) and m[line][lower_band+size] != ".":
            found = True 
            if m[line][lower_band+size] == "*":
                if f'{line}-{lower_band+size}' not in gears.keys(): #not(gears[f'{line}-{lower_band+size}']):
                    gears.update({f'{line}-{lower_band+size}':[number]})
                else:
                    gears[f'{line}-{lower_band+size}'].append(number)

    except IndexError:
        pass

    if found:
        return number
    else: 
        return False
    

m =[]
parts = []
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

print(sum(parts))
s = 0
for key in gears.keys():
    if len(gears[key]) > 1:
        s += math.prod(gears[key])

print(s)