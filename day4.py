import re

file = open("input4.txt")

sum1 = 0

for line in enumerate (file):
    # if line[0]<5:
        winning = re.findall('\d+', re.split ('\|', line[1])[0])
        winning = winning[1:]
        actual = re.findall('\d+', re.split ('\|', line[1])[1])
        num = 0
        for x in winning:
            if x in actual:
                num += 1
        if num != 0:
            sum1 += pow (2, num-1)
print(sum1)