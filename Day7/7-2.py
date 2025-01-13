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
    #print("Evaluating numbers...", equation)
    #print("Test value here is", values[idx])
    found = False
    # For each equation, generate a list of all possible combinations of + and * operators to try
    num_operators = len(equation)-1
    ops_list = [list(x) for x in product('+*|', repeat=num_operators)]
    #print(ops_list)

    # Then try each list of operators zipped against the equation, and see if evaluating it matches the given value
    for operators in ops_list:
      if found == False:
        # zip_longest allows us to zip even though one list is one item longer than the other
        eq = [x for y in zip_longest(equation, operators) for x in y]
        # Since the shorter list left a NoneType at the end when zipping, remove it
        del eq[-1]
        # Whenever you see a '|', just remove it from the list
        while '|' in eq:
            eq.remove('|')
        # Add closing parentheses after every digit except the first one
        paren_count = 0
        for index, i in enumerate(eq):
          if i.isdigit() and index > 1:
            if index < len(eq)-1:
              if eq[index+1].isdigit():
                pass
            else:
              eq.insert(index+1, ')')
              paren_count += 1
        # Add that amount of opening parentheses at the beginning (len(equation)-1)
        for i in range(paren_count):
          eq.insert(0, '(')
        # Now join all the items in the list into one big concatenated equation and evaluate it
        evaluation = eval(''.join(eq))
        #print("Evaluation:", evaluation)
        if evaluation == values[idx]:
          #print("{0} is possible. Values being added to total: {1}".format(''.join(eq), values[idx]))
          found = True
          total += values[idx]
          #print("Running total:", total)

  print("The total value of all possible true equations is:", total)

main()