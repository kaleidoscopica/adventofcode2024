def main():
  map = []

  with open('input.txt') as file:
    for line in file:
      map.append(line.strip())
  file.close()

  print(map)

  # First, find the location of the guard
  for idx1, row in enumerate(map):
    for idx2, col in enumerate(row):
      if col == '^':
        guard_loc = (idx1, idx2)

  # Then, go back and trace out her route through the map
  for idx1, row in enumerate(map):
    for idx2, col in enumerate(row):
      pass

  next = ''
  direction = 'up'
  while next != '#':
    #guard_loc = map[0][0]
    pass
  
  print(guard_loc)

main()