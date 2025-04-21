def main():
  map = []

  with open('input.txt') as file:
    map = file.read().splitlines()
  file.close()

  antinodes = []
  antennas_checked = []

  for idx1, row in enumerate(map):
    for idx2, col in enumerate(row):
      pos = encode(idx1, idx2)
      if col != '.':
        print("Evaluating antenna", col)
        # If we haven't checked this type of antenna yet, find all instances of it
        if col not in antennas_checked:
          print("Evaluating antenna {0} at position {1}".format(col, pos))
          print(map[idx1])
          antennas_checked.append(col)
          for i in range(2499-pos):
            r, c = decode(i)
<<<<<<< HEAD
            if map[r][c] == col:
              print("Founding matching antenna at position", i)
=======
            if map[r][c] == col and i != pos:
              print("Antenna found at position", i)
              #print(map[r-1])
              print(map[r])
              #print(map[r+1])

  print(antennas_checked)
>>>>>>> 0244861 (File close not needed with 'with')

def encode(row, col):
  return row*50 + col

def decode(n):
  row = n // 50 
  col = n % 50
  return row, col


main()