import re
import numpy as np

file = open ("input3.txt")

part1 = 0
part2 = 0
m = []
for line in enumerate(file):
    # if line[0]<6:    
        lineList = []
        for ch in line[1]:
            lineList.append(ch)
        m.append(lineList)

matrix = np.array(m, dtype='U1')
checknum1 = np.zeros((len(m), len(m[0])))

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        num1 = ""
        start1 = j
        while matrix[i][start1].isdigit() and checknum1[i][start1] != 1:
            num1 += matrix[i][start1]
            checknum1[i][start1] = 1
            if start1 < len(matrix[0]):
                start1 += 1;

        for ch in num1:
            for x in range (-1, 2):
                for y in range (-1, len(num1)+1):
                    if 0 <= (i+x) < len(matrix) and 0 <= (j+y) < len(matrix[0]):
                        # print ((matrix[i][j], matrix[i+x][j+y]), end = " |  ")
                        # print(part, end = " | ")
                        if re.match(r'([0-9])|\.|\n', matrix[i+x][j+y]) is None:
                            part1 += int(num1)
                            break
                else:
                    continue
                break
            else:
                continue
            break

checknum2 = np.zeros((len(m), len(m[0])))
part2 = 0

for k in range(len(matrix)):
    for l in range(len(matrix[0])):
        if re.match('\*', matrix[k][l]):
            nums = []
            for m in range (-1, 2):
                for n in range (-1, 2):
                    if 0 <= (k+m) < len(matrix) and 0 <= (l+n) < len(matrix[0]) and matrix[k+m][l+n].isdigit() and checknum2[k+m][l+n] != 1:
                        num2 = ""
                        start2 = l+n
                        while start2 > 0 and matrix[k+m][start2-1].isdigit():
                            start2 -=1
                        while start2 < len(matrix[0]) and matrix[k+m][start2].isdigit():
                            num2 += matrix[k+m][start2]
                            checknum2[k+m][start2] = 1
                            start2 += 1
                        if num2 != '':
                            nums.append(num2)
            if len(nums) == 2:
                part2 += int(nums[0])*int(nums[1])
                    
print (part1)
print (part2)
      