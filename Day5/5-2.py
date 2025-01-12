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
  out_of_order = []

  for update in updates:
    # Assume each update is valid
    valid = True

    for idx, number in enumerate(update):
      # As long as we're not already at the last number, grab the next number to check
      if idx < len(update)-1:
        next_number = update[idx+1]
        # Go through the rules, and find the one that applies
        for rule in rules:
          if number in rule and next_number in rule:
            # If the rule has the numbers out-of-order, the update is not correctly-ordered
            if rule[0] == next_number and rule[1] == number:
              valid = False

    # Keep only the out-of-order updates in a separate list for further processing
    if valid == False:
      out_of_order.append(update)

  # Now loop through the out-of-order updates and get them in order
  for update in out_of_order:
    # We know each update is not yet valid, at least at the start
    valid = False

    # While it's not yet valid, keep making changes
    while valid == False:
      changes = 0
      for idx, number in enumerate(update):
      # As long as we're not already at the last number, grab the next number to check
        if idx < len(update)-1:
          next_number = update[idx+1]
          # Go through the rules, and find the one that applies
          for rule in rules:
            if number in rule and next_number in rule:
              # If the rule has the numbers out-of-order, the update is not correctly-ordered
              if rule[0] == next_number and rule[1] == number:
                # Switch them around to put them in the right order
                update[idx], update[idx+1] = update[idx+1], update[idx]
                changes += 1
      
      # If no changes were made, it can become valid, stopping the while loop
      if changes != 0:
        valid = False
      else:
        valid = True

  # For each originally out-of-order update, add its middle page number to the total
  for update in out_of_order:
    total += int(update[len(update)//2])

  print("The total is:", total)

main()