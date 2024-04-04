import re
file = open ("input.txt")

dictionary = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    }

sum1 = 0
sum2 =0
for line in file:
    digits = re.findall(r'(\d)', line)
    sum1 += int(digits[0]+digits[len(digits)-1])

    toConvert = re.findall(r'one|two|three|four|five|six|seven|eight|nine', line)
    for x in toConvert:
        line = re.sub(x, dictionary[x], line, count =1)
    digits = re.findall(r'\d', line)
    sum2 += int(digits[0]+digits[-1])
print(sum1)
print(sum2)