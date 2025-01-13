from itertools import product, zip_longest
import re

def main():
  values = []
  equations = []
  operators = []

  with open('input.txt') as file:
    for line in file:
      values.append(int(line.split(':')[0]))
      equations.append([x for x in line.split(':')[1].split()])
  file.close()

  total = 0

  for idx, equation in enumerate(equations):
    found = False
    # For each equation, generate a list of all possible combinations of + and * operators to try
    num_operators = len(equation)-1
    ops_list = [list(x) for x in product('+*', repeat=num_operators)]
    # Then try each list of operators zipped against the equation, and see if evaluating it matches the given value
    for operators in ops_list:
      if found == False:
        # zip_longest allows us to zip even though one list is one item longer than the other
        eq = [x for y in zip_longest(equation, operators) for x in y]
        # Since the shorter list left a NoneType at the end when zipping, remove it
        del eq[-1]
        # Add closing parentheses after every digit except the first one
        for index, i in enumerate(eq):
          if i.isdigit() and index > 1:
            eq.insert(index+1, ')')
        # Add that amount of opening parentheses at the beginning (len(equation)-1)
        for i in range(len(equation)-1):
          eq.insert(0, '(')
        # Now join all the items in the list into one big concatenated equation and evaluate it
        evaluation = eval(''.join(eq))
        if evaluation == values[idx]:
          found = True
          total += values[idx]

  print("The total value of all possible true equations is:", total)

main()