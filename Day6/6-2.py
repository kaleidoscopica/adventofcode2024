def main():
  map = []

  with open('input.txt') as file:
    for line in file:
      map.append(line.strip())

  # First, find the location of the guard
  for idx1, row in enumerate(map):
    for idx2, col in enumerate(row):
      if col == '^':
        guard_loc = (idx1, idx2)
        # Mark where the guard is now as an 'X', before she starts to move
        updated_row = map[idx1][:idx2] + 'X' + map[idx1][idx2+1:]
        map[idx1] = updated_row
  
  # Her first direction is going up
  direction = 'up'
  idx1, idx2 = guard_loc
  left_map = False

  # While the guard hasn't left the map yet, follow her path
  while left_map == False:
    next = ''
    while next != '#' and direction == 'up' and left_map == False:
      if idx1 > 0:
        # Grab the next position - is there an obstacle?
        next = map[idx1-1][idx2]
        # If there's an obstacle, turn 90 degrees to the right
        if next == '#':
          direction = 'right'
        # Otherwise, take a step forward (and mark it)
        else:
          idx1 -= 1
          updated_row = map[idx1][:idx2] + 'X' + map[idx1][idx2+1:]
          map[idx1] = updated_row
      # If she's at idx1 == 0, then a move will result in her going off the map
      else:
        left_map = True

    next = ''
    while next != '#' and direction == 'right' and left_map == False:
      if idx2 < 129:
        # Grab the next position - is there an obstacle?
        next = map[idx1][idx2+1]
        # If there's an obstacle, turn 90 degrees to the right
        if next == '#':
          direction = 'down'
        # Otherwise, take a step forward (and mark it)
        else:
          idx2 += 1
          updated_row = map[idx1][:idx2] + 'X' + map[idx1][idx2+1:]
          map[idx1] = updated_row
      # If she's at idx2 == 129, then a move will result in her going off the map
      else:
        left_map = True

    next = ''
    while next != '#' and direction == 'down' and left_map == False:
      if idx1 < 129:
        # Grab the next position - is there an obstacle?
        next = map[idx1+1][idx2]
        # If there's an obstacle, turn 90 degrees to the right
        if next == '#':
          direction = 'left'
        # Otherwise, take a step forward (and mark it)
        else:
          idx1 += 1
          updated_row = map[idx1][:idx2] + 'X' + map[idx1][idx2+1:]
          map[idx1] = updated_row
      # If she's at idx1 == 129, then a move will result in her going off the map
      else:
        left_map = True
    
    next = ''
    while next != '#' and direction == 'left' and left_map == False:
      if idx2 > 0:
        # Grab the next position - is there an obstacle?
        next = map[idx1][idx2-1]
        # If there's an obstacle, turn 90 degrees to the right
        if next == '#':
          direction = 'up'
        # Otherwise, take a step forward (and mark it)
        else:
          idx2 -= 1
          updated_row = map[idx1][:idx2] + 'X' + map[idx1][idx2+1:]
          map[idx1] = updated_row
      # If she's at idx2 == 0, then a move will result in her going off the map
      else:
        left_map = True
    
    # Count up the number of 'X'
    count = 0
    if left_map == True:
      for idx1, row in enumerate(map):
        for idx2, col in enumerate(row):
          if col == 'X':
            count += 1
    
  for row in map:
    print(row)
  print("The total number of locations visited by the guard is:", count)

main()