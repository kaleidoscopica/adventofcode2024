from itertools import combinations_with_replacement, zip_longest

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
    print("Evaluating equation", equation)
    print("Test value here is", values[idx])
    # found flag, for when operators have more than one possible configuration
    found = False
    # For each equation, generate a combination of + and * operators to try
    num_operators = len(equation)-1
    ops_list = [list(x) for x in combinations_with_replacement('+*', num_operators)]
    # Lookup dictionary for operators
    op = {'+': lambda x, y: x + y, '*': lambda x, y: x * y}
    # Then try each list of operators zipped against the equation, and see if evaluating it matches the given value
    for operators in ops_list:
      #print("Evaluating operators", operators)
      if found == False:
        # zip_longest allows us to zip even though one list is one item longer than the other
        eq = [x for y in zip_longest(equation, operators) for x in y]
        # Since the shorter list left a NoneType at the end when zipping, remove it
        del eq[-1]
        # Now join all the items in the list into one big concatenated equation and evaluate it
        if eval(''.join(eq)) == values[idx]:
          print("Equation:", ''.join(eq))
          print("Evaluation:", eval(''.join(eq)))
          print("This equation is possible. Values being added to total:", values[idx])
          found = True
          total += values[idx]
          print("Running total:", total)

  print("The total value of all possible true equations is:", total)

main()