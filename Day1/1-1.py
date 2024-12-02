def main():
  location_ids = []

  with open('input.txt') as file:
    for line in file:
      location_ids.append(line.strip().split())
  file.close()

  first_list = []
  second_list = []

  # Put the first item from each line in one list, and the second item in another list
  for line in location_ids:
    first_list.append(int(line[0]))
    second_list.append(int(line[1]))

  # Sort the two lists from smallest->largest
  first_list.sort()
  second_list.sort()

  total_distances = 0

  # Calculate the distance between each list pair and add it to the total
  for idx, item in enumerate(first_list):
    distance = abs(item - second_list[idx])
    total_distances += distance

  print("Total distance is: ", total_distances)
main()