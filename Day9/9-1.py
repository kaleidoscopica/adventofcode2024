def main():

  blocks = []
  free_spaces = []
  representation = ''

  with open('input.txt') as file:
    #disk_map = file.readlines()
    for line in file:
      for idx, c in enumerate(line):
        if idx % 2 == 0:
          for i in range(int(c)):
            blocks.append(idx // 2)
          representation += (str(idx // 2) * int(c))
        else:
          for i in range(int(c)):
            blocks.append('')
          representation += ('.' * int(c))

  # Compact the files!
  compacted_list = [x for x in blocks]
  negative_idx = -1
  for idx, block in enumerate(compacted_list):
    if idx != negative_idx:
      if block == '':
        # Blank space - grab the last block, and move it here
        file_id = blocks[negative_idx]
        blocks[negative_idx] = ''
        negative_idx -= 1
        # If you got a blank, grab again
        while file_id == '':
          file_id = blocks[negative_idx]
          blocks[negative_idx] = ''
          negative_idx -= 1
        # If we "meet in the middle", break
        if last_ascending_seen == file_id:
          break_point = idx
          break
        # Otherwise, move the block to the first open space
        else:
          compacted_list[idx] = file_id
        print(f"Replaced block at idx {idx} with file ID {file_id}.")
      # Keep track of the IDs we see while ascending, to not overshoot
      else:
        last_ascending_seen = blocks[idx]

  # Clean up the remainder of the list
  while break_point < len(compacted_list):
    compacted_list[break_point] = ''
    break_point += 1

  # Calculate the checksum
  checksum = 0
  for idx, block in enumerate(compacted_list):
    if block != '':
      checksum += (idx * int(block))
  
  print("The checksum value is:", checksum)

main()