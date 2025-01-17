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
        # If we haven't checked this type of antenna yet, find all instances of it
        if col not in antennas_checked:
          antennas_checked.append(col)
          for i in range(2499-pos):
            pass

def encode(row, col):
  return row*50 + col

def decode(n):
  row = n // 50 
  col = n % 50
  return row, col

main()