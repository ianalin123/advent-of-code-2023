import re

def convert_to_number(number):
    # Dictionary to pair strings to numbers
    word_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
                 'nine': '9'}
    if number in word_dict.keys():
        real_number = word_dict.get(number)
        return real_number
    else:
        return str(number)


# Part 2
def extract_word_calib_values(line):
    numbers = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine',line)
    for item in numbers:
        # Addresses strings tied together
        num = convert_to_number(item)
        new_sub = item[0] + num + item[-1]
        line = re.sub(item,new_sub,line)
    numbers = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
    if len(numbers) == 1:
        number = convert_to_number(numbers[0])
        value = int(number + number)
        return value
    else:
        front = convert_to_number(numbers[0])
        back = convert_to_number(numbers[-1])
        value = int(front + back)
        return value
    

if __name__ == '__main__':
    second_total = 0
    input_text = "input.txt"
    with open('input.txt','r') as f:
        for line in f:
            second_total += extract_word_calib_values(line)
    print(second_total)