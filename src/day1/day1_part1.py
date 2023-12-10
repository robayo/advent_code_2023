import re


with open('src/day1/input.txt', 'r') as file:
    input_lines = [line.strip() for line in file]
suma = sum([ int(re.search('\d', i)[0] +re.search('\d', i[::-1])[0])  for i in input_lines] 
            )
print(suma)
