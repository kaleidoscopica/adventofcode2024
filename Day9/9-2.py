def main():

  blocks = []
  free_spaces = []

  with open('input.txt') as file:
    for line in file:
      for idx, c in enumerate(line):
        if idx % 2 == 0:
          for i in range(int(c)):
            blocks.append(idx // 2)
        else:
          for i in range(int(c)):
            blocks.append('')

  # Compact the files!
  negative_idx = -1
  for idx, block in enumerate(blocks):
    if idx != negative_idx:
      if block == '':
        # Find out how many empty blocks there are
        block_size = calculate_space(blocks, idx)
        # Blank space - grab the last block, and move it here
        file_id = blocks[negative_idx]
        negative_idx -= 1
        # If you got a blank, grab again
        while file_id == '':
          blocks[negative_idx+1] = ''
          file_id = blocks[negative_idx]
          negative_idx -= 1
        # If we "meet in the middle", break
        if last_ascending_seen == file_id:
          break
        # Otherwise, move the block to the first open space
        else:
          blocks[negative_idx+1] = ''
          blocks[idx] = file_id
        print(f"Replaced block at idx {idx} with file ID {file_id}.")
      # Keep track of the IDs we see while ascending, to not overshoot when we reach the end
      else:
        last_ascending_seen = blocks[idx]

  # Calculate the checksum
  checksum = 0
  for idx, block in enumerate(blocks):
    if block != '':
      checksum += (idx * int(block))
  
  print("The checksum value is:", checksum)

main()

def calculate_space(blocks, idx):
  block_size = 1
  while idx+1 < len(blocks):
    if blocks[idx+1] == '':
      block_size += 1
    else:
      break
  return block_size