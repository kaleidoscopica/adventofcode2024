def main():
  rules = []
  updates = []

  with open('input.txt') as file:
    for line in file:
      if '|' in line:
        rules.append(line.strip().split('|'))
      elif ',' in line:
        updates.append(line.strip().split(','))
  file.close()

  total = 0

  for update in updates:
    # Assume each update is valid
    valid = True
    print("Before any changes.....", update)

    for idx, number in enumerate(update):
      # As long as we're not already at the last number, grab the next number to check
      if idx < len(update)-1:
        next_number = update[idx+1]
        print("Comparing {0} and {1}...".format(number, next_number))

        # Go through the rules, and find the one that applies
        for rule in rules:
          if number in rule and next_number in rule:
            print("Evaluating rule", rule)
            # If the rule has the numbers out-of-order, the update is not correctly-ordered
            if rule[0] == next_number and rule[1] == number:
              print("These numbers are out of order. Let's switch them around.")
              valid = False
              # Switch them around to put them in the right order
              update[idx], update[idx+1] = update[idx+1], update[idx]
            else:
              print("These numbers are already in the correct order!")

    print("After changes...", update)
    # If the update was incorrectly-ordered, add its middle page number to the total
    if valid == False:
      print("Adding middle number to total:", update[len(update)//2])
      total += int(update[len(update)//2])

  print("The total is:", total)

main()