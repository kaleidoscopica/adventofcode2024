import re

def main():
  data = []
  multiplicands = []

  with open('input.txt') as file:
    # Join all the lines together, into a single line
    data = " ".join(line.strip() for line in file)

  # First insert a 'do()' at the beginning since mul() instructions are enabled at start
  data = 'do()' + data

  # Use regex to find all strings that look like 'mul(123,123)', and add them to a list
  # Split everywhere you see a "do()"
  dos = re.split('do\(\)', data)

  # Then find the index where you start to see a 'don't()'
  for do in dos:
    dont = do.index("don't()") if "don't()" in do else -1
    # Only grab the multiplicands before the 'don't()', if it exists
    if dont == -1:
      mul = re.findall('mul\([0-9]+\,[0-9]+\)', do)
    else:
      mul = re.findall('mul\([0-9]+\,[0-9]+\)', do[:dont])
    # Then parse each one to grab its pair of numbers that will be multiplied
    for item in mul:
      multiplicands.append(re.findall('[0-9]+', item))

  # Multiply each pair together and add it to a total
  total = 0
  for multiplicand in multiplicands:
    product = int(multiplicand[0]) * int(multiplicand[1])
    total += product
  
  print("The total is:", total)

main()