import re

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
    valid = False
    page_rules = []
    for number in update:
      # Check where the rules containing that page number are
      for rule in rules:
        print(rule)
        if number in rule:
          page_rules.append(rule)
      print("For number...", number)
      #print("The applicable rules are:", page_rules)
  
    # If the update is correctly-ordered, add its middle page number to the total
    if valid == True:
      total += update[len(update)//2]

  print("The total is:", total)

main()