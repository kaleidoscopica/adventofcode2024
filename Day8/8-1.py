def main():
  map = []

  with open('input.txt') as file:
    map = file.read().splitlines()
  file.close()

  print(len(map[0]))

  for idx1, row in enumerate(map):
    for idx2, col in enumerate(row):
      pos = encode(idx1, idx2)
      if col != '.':
        for i in range(2500-pos):
          

def encode(row, col):
  return row*50 + col + 1

def decode(n):
  row = n // 50 
  col = n % 50
  return row, col

main()