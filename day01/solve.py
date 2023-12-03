path = "."
import re 

sum = 0
numbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

capture = r"^(zero|one|two|three|four|five|six|seven|eight|nine)"

def get_digit(match):
    return int(numbers.index(match.group(1)))

with open(f'{path}/puzzle') as fp:
    for line in fp.readlines():
        line = line.strip()
        line_len = len(line)
                
        stop_left = False
        stop_right = False
        
        for i in range(line_len):
            if not(stop_left):
                if ord(line[i]) < 58:
                    sum += (ord(line[i])-48) * 10
                    stop_left = True

            if not(stop_right):
                if ord(line[line_len-1-i]) < 58:
                    sum += (ord(line[line_len-1-i])-48) 
                    stop_right = True
print(f'Part 1: {sum}')

sum = 0
with open(f'{path}/puzzle') as fp:
    for line in fp.readlines():
        line = line.strip()
        line_len = len(line)
                
        stop_left = False
        stop_right = False
        
        for i in range(line_len):
            if not(stop_left):
                if m := re.match(capture, line[i:]):
                    sum += get_digit(m) * 10
                    stop_left = True

                elif ord(line[i]) < 58:
                    sum += (ord(line[i])-48) * 10
                    stop_left = True

            if not(stop_right):
                if m := re.match(capture, line[line_len-1-i:]):
                    sum += get_digit(m) 
                    stop_right = True

                elif ord(line[line_len-1-i]) < 58:
                    sum += (ord(line[line_len-1-i])-48) 
                    stop_right = True
print(f'Part 2: {sum}')