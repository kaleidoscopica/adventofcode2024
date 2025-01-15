def main():
  map = []

  with open('input.txt') as file:
    map = file.read().splitlines()
  file.close()

  print(map)

main()