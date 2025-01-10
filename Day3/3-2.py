import re

def main():
  data = []
  multiplicands = []

  with open('input.txt') as file:
    data = file.readlines()
  file.close

  # First insert a 'do()' at the beginning since mul() instructions are enabled at start
  #print("data[0] is: ", data[0])
  data[0] = 'do()' + data[0]
  #print("data[0] is now: ", data[0])

  # Use regex to find all strings that look like 'mul(123,123)', and add them to a list
  for line in data:
    # Split each line where you see a "don't()"
    donts = re.split('don\'t\(\)', line)
    print("Donts for this line are.......")
    print()
    print()
    print(donts)
    # Then find the index where you start to see a 'do()'
    for dont in donts:
      do = dont.index('do()') if 'do()' in dont else -1
      # Only grab the multiplicands after the 'do()', if it exists
      if do != -1:
        mul = re.findall('mul\([0-9]+\,[0-9]+\)', line[do:])
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