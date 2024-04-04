import re

file = open ("input2.txt")

def set_to_dict (setName, color):
    colorset = re.findall('\d*(?= ' + color +')', setName)
    
    if not colorset:
        return 0
    else:
        return int(colorset[0])
part1 = 0
part2 = 0
for x in enumerate(file):
    possible = True
    mins = {"red" : 0, "green": 0, "blue": 0}


    games = re.sub(r'(Game \d*: )|(?<=;)(\s)|\n', '', x[1])
    games = re.split(r';', games)   

    for set in games:
        digits = {"red" : 0, "green": 0, "blue": 0}
        digits = {key:set_to_dict(set, key) for key in digits.keys()}
        if digits["red"] > 12 or digits["green"] > 13 or digits["blue"] > 14:
            possible = False
        mins = {key:(digits[key] if digits[key] > mins[key] else mins[key]) for key in mins.keys()}
    if possible:
        part1 += x[0]+1
    part2 += mins["red"]*mins["green"]*mins["blue"]

print(part1) 
print(part2)          

