from itertools import product, zip_longest

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
    ops_list = [list(x) for x in product('+*|', repeat=num_operators)]

    # Then try each list of operators zipped against the equation, and see if evaluating it matches the given value
    for operators in ops_list:
      if found == False:
        # zip_longest allows us to zip even though one list is one item longer than the other
        eq = [x for y in zip_longest(equation, operators) for x in y]
        # Since the shorter list left a NoneType at the end when zipping, remove it
        del eq[-1]
        # Now, go through each operation and evaluate them left-to-right
        for i in range(len(eq)//2):
          if eq[1] == '|':
            res = eval(''.join(eq[x] for x in [0, 2]))
          elif eq[1] == '+' or eq[1] == '*':
            res = eval(''.join(eq[0:3]))
          del eq[0], eq[0], eq[0]
          eq.insert(0, str(res))

        if int(res) == values[idx]:
          found = True
          total += values[idx]

  print("The total value of all possible true equations is:", total)

main()