def main():
  map = []

  with open('input.txt') as file:
    map = file.read().splitlines()

  antenna_dict = {}
  antinode_dict = {}

  # Iterate through the map, looking for antennas
  for idx1, row in enumerate(map):
    for idx2, col in enumerate(row):
      # Encode the position as a digit between 1-2500
      pos = encode(idx1, idx2)
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

  # Now, find all the antinodes
  for key in antenna_dict:
    num_antennae = len(antenna_dict[key])
    outer_count = 0
    while (outer_count < num_antennae-1):
      inner_count = outer_count
      while (inner_count < num_antennae-1):
        pos_1 = antenna_dict[key][outer_count]
        r_1, c_1 = decode(pos_1)
        pos_2 = antenna_dict[key][inner_count+1]
        r_2, c_2 = decode(pos_2)
        row_distance = r_2 - r_1
        col_distance = c_2 - c_1

        # Make sure they have enough space between them to create an antinode pair
        if (abs(col_distance) >= 2) or (abs(row_distance) >= 2) or (abs(row_distance) >= 1 and abs(col_distance) >= 1):

          # Then calculate and add the antinodes to the antinode_dict, if they are within the bounds
          # And now we must place antinodes on the original resonant antennae, too
          r_3 = r_1
          c_3 = c_1
          anti_1 = encode(r_3, c_3)
          # Check to make sure it's in bounds
          while r_3 >= 0 and r_3 <= 49 and c_3 >= 0 and c_3 <= 49:
            if key in antinode_dict:
              antinode_dict[key].append(anti_1)
            else:
              antinode_dict[key] = [anti_1]
            # Now keep placing antinodes at each point until we go out of bounds
            r_3 = r_3 - row_distance
            c_3 = c_3 - col_distance
            anti_1 = encode(r_3, c_3)

          r_4 = r_2
          c_4 = c_2
          anti_2 = encode(r_4, c_4)
          # Check to make sure it's in bounds
          while r_4 >= 0 and r_4 <= 49 and c_4 >= 0 and c_4 <= 49:
            if key in antinode_dict:
              antinode_dict[key].append(anti_2)
            else:
              antinode_dict[key] = [anti_2]
            # Now keep placing antinodes at each point until we go out of bounds
            r_4 = r_4 + row_distance
            c_4 = c_4 + col_distance
            anti_2 = encode(r_4, c_4)

        inner_count += 1
      outer_count += 1
  
  antinode_list = []
  # Now count unique antinodes
  for key in antinode_dict:
    for value in antinode_dict[key]:
      antinode_list.append(value)
  antinode_set = set(antinode_list)

  print("The number of unique locations containing an antinode is:", len(antinode_set))

def encode(row, col):
  return row*50 + col + 1   # Encode between 1-2500

def decode(n):
  row = (n-1) // 50 
  col = (n-1) % 50
  return row, col

main()