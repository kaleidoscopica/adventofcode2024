from itertools import combinations_with_replacement, zip_longest

def main():
  values = []
  equations = []
  operators = []

  with open('input.txt') as file:
    for line in file:
      values.append(int(line.split(':')[0]))
      equations.append([int(x) for x in line.split(':')[1].split()])
  file.close()

  total = 0

  for idx, equation in enumerate(equations):
    # For each equation, generate a combination of + and * operators to try
    num_operators = len(equation)-1
    ops_list = [list(x) for x in combinations_with_replacement('+*', num_operators)]
    # Lookup dictionary for operators
    op = {'+': lambda x, y: x + y, '*': lambda x, y: x * y}
    # Then try each list of operators zipped against the equation, and see if it matches the given value
    for operators in ops_list:
      eq = [x for y in zip_longest(equation, operators) for x in y]
      print(eq)

main()