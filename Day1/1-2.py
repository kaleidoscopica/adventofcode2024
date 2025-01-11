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

  similarity_score = 0

  # Calculate the similarity score by going through the first list and counting up the occurrences in the second list
  for item in first_list:
    count = second_list.count(item)
    similarity_score += item * count

  print("Similarity score is:", similarity_score)
main()