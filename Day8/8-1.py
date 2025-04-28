def main():
  map = []

  with open('input.txt') as file:
    map = file.read().splitlines()

  antenna_dict = {}   # dictionary of which antennae (keys) are found at which positions (values)
  antinode_dict = {}

  # Iterate through the map, looking for antennas
  for idx1, row in enumerate(map):
    for idx2, col in enumerate(row):
      pos = encode(idx1, idx2)   # Encode the position as a digit between 1-2500
      if col != '.' and col not in antenna_dict:
        # If we haven't checked this type of antenna yet, find all instances of it
        for i in range(2500):
          r, c = decode(i)
          if map[r][c] == col:
            # Add each new position to the antenna dictionary
            if col in antenna_dict:
              antenna_dict[col].append(i)
            else:
              antenna_dict[col] = [i]

  #print(antenna_dict)

  # Now, find all the antinodes
  for key in antenna_dict:
    num_antennae = len(antenna_dict[key])
    outer_count = 0
    # 01 02 03 12 13 23
    while (outer_count < num_antennae-1):
      inner_count = outer_count
      while (inner_count < num_antennae-1):
        pos_1 = antenna_dict[key][outer_count]
        r_1, c_1 = decode(pos_1)
        pos_2 = antenna_dict[key][inner_count+1]
        r_2, c_2 = decode(pos_2)
        # Make sure they have enough space between them
        row_distance = abs(r_1 - r_2)
        col_distance = abs(c_1 - c_2)
        pos_distance = pos_2 - pos_1
        if (col_distance >= 2) or (row_distance >= 2) or (row_distance >= 1 and col_distance >= 1):
          # Then calculate and add the antinodes to the antinode_dict, if they are within the bounds
          if (c_1 - col_distance >= 0) and (r_1 - row_distance >= 0):
            anti_1 = pos_1 - pos_distance
            r_3, c_3 = decode(anti_1)
            # Another check to make sure they're in bounds
            if r_3 >= 0 and r_3 <= 49 and c_3 >= 0 and c_3 <= 49:
              if key in antinode_dict:
                antinode_dict[key].append(anti_1)
              else:
                antinode_dict[key] = [anti_1]
          if (c_2 + col_distance <= 49) and (r_2 + row_distance <= 49):
            anti_2 = pos_2 + pos_distance
            r_4, c_4 = decode(anti_2)
            if r_4 >= 0 and r_4 <= 49 and c_4 >= 0 and c_4 <= 49:
              if key in antinode_dict:
                antinode_dict[key].append(anti_2)
              else:
                antinode_dict[key] = [anti_2]
        inner_count += 1
      outer_count += 1
  
  antinode_list = []
  # Now count unique antinodes
  for key in antinode_dict:
    for value in antinode_dict[key]:
      antinode_list.append(value)
  antinode_set = set(antinode_list)

  #print("Antinode list contains:")
  #print(antinode_list)
  #print("Antinode set contains:")
  #print(antinode_set)
  print(antenna_dict)
  print(antinode_dict)

  print("The number of unique locations containing an antinode is:", len(antinode_set))
  # 417 is too high
  # 379 is too high

def encode(row, col):
  return row*50 + col + 1   # Encode between 1-2500

def decode(n):
  row = (n-1) // 50 
  col = (n-1) % 50
  return row, col

main()