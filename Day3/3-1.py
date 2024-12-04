import re

def main():
  data = []
  multiplicands = []

  with open('input.txt') as file:
    data = file.readlines()
  file.close

  # Use regex to find all strings that look like 'mul(123,123)', and add them to a list
  for line in data:
    mul = re.findall('mul\([0-9]+\,[0-9]+\)', line)
    # Then parse each one to grab its pair of numbers that will be multiplied
    for item in mul:
      multiplicands.append(re.findall('[0-9]+', item))

  # Multiply each pair together and add it to a total
  total = 0
  for multiplicand in multiplicands:
    product = int(multiplicand[0]) * int(multiplicand[1])
    total += product
  
  print("The total is: ", total)

main()