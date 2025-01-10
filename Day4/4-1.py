def main():
  wordsearch = []

  with open('input.txt') as file:
    for line in file:
      wordsearch.append(line.strip())
    file.close()

  count = 0

  for idx1, line in enumerate(wordsearch):
    for idx2, ltr in enumerate(line):
      if ltr == 'X':

        ## Left-to-right checks
        if idx2 <= 136:
          # Check the row for 'XMAS' going left-to-right
          if wordsearch[idx1][idx2+1] == 'M' and wordsearch[idx1][idx2+2] == 'A' and wordsearch[idx1][idx2+3] == 'S':
            count += 1
          # Check the diagonal for 'XMAS' going to the top-right
          if idx1 >= 3:
            if wordsearch[idx1-1][idx2+1] == 'M' and wordsearch[idx1-2][idx2+2] == 'A' and wordsearch[idx1-3][idx2+3] == 'S':
              count += 1
          # Check the diagonal for 'XMAS' going to the bottom-right
          if idx1 <= 136:
            if wordsearch[idx1+1][idx2+1] == 'M' and wordsearch[idx1+2][idx2+2] == 'A' and wordsearch[idx1+3][idx2+3] == 'S':
              count += 1

        ## Right-to-left checks
        if idx2 >= 3:
          # Check the row for 'XMAS' going right-to-left
          if wordsearch[idx1][idx2-1] == 'M' and wordsearch[idx1][idx2-2] == 'A' and wordsearch[idx1][idx2-3] == 'S':
            count += 1
          # Check the diagonal for 'XMAS' going to the top-left
          if idx1 >= 3:
            if wordsearch[idx1-1][idx2-1] == 'M' and wordsearch[idx1-2][idx2-2] == 'A' and wordsearch[idx1-3][idx2-3] == 'S':
              count += 1
          # Check the diagonal for 'XMAS' going to the bottom-left
          if idx1 <= 136:
            if wordsearch[idx1+1][idx2-1] == 'M' and wordsearch[idx1+2][idx2-2] == 'A' and wordsearch[idx1+3][idx2-3] == 'S':
              count += 1

        ## Vertical checks
        if idx1 <= 136:
          # Check the column for 'XMAS' going down
          if wordsearch[idx1+1][idx2] == 'M' and wordsearch[idx1+2][idx2] == 'A' and wordsearch[idx1+3][idx2] == 'S':
            count += 1
        if idx1 >= 3:
          # Check the column for 'XMAS' going up
          if wordsearch[idx1-1][idx2] == 'M' and wordsearch[idx1-2][idx2] == 'A' and wordsearch[idx1-3][idx2] == 'S':
            count += 1
  
  print(count)

main()