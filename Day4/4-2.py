def main():
  wordsearch = []

  with open('input.txt') as file:
    for line in file:
      wordsearch.append(line.strip())
    file.close()

  count = 0

  for idx1, line in enumerate(wordsearch):
    for idx2, ltr in enumerate(line):
      found1 = False
      found2 = False
      if ltr == 'A' and idx1 >= 1 and idx2 >= 1 and idx1 <= 138 and idx2 <= 138:
        ## Check the first diagonal
        if wordsearch[idx1-1][idx2-1] == 'M' and wordsearch[idx1+1][idx2+1] == 'S':
          found1 = True
        elif wordsearch[idx1-1][idx2-1] == 'S' and wordsearch[idx1+1][idx2+1] == 'M':
          found1 = True
        ## Check the second diagonal
        if wordsearch[idx1-1][idx2+1] == 'M' and wordsearch[idx1+1][idx2-1] == 'S':
          found2 = True
        elif wordsearch[idx1-1][idx2+1] == 'S' and wordsearch[idx1+1][idx2-1] == 'M':
          found2 = True
        
        if found1 == True and found2 == True:
          count += 1
  
  print("The total number of 'X-MAS' found is: ", count)

main()