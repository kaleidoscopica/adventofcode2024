def main():
  reports = []

  with open('input.txt') as file:
    for report in file:
      reports.append(report.strip().split())
  file.close()

  # Analyze each report to see if it is safe
  safe_count = 0
  for report in reports:
    # Each report starts off safe
    safe = True
    increasing_or_decreasing = []
    report_length = len(report)

    # Check the levels in each report for safety
    for idx in range(report_length-1):
      # Make sure any two adjacent levels differ by at least one and at most three
      distance = abs(int(report[idx]) - int(report[idx+1]))
      # If they stay the same or differ too much, mark the report unsafe
      if distance < 1 or distance > 3:
        safe = False
      
      # Next check, did it always increase or always decrease?
      if int(report[idx]) > int(report[idx+1]):
        increasing_or_decreasing.append(1)
      elif int(report[idx]) < int(report[idx+1]):
        increasing_or_decreasing.append(0)

    # If you see both 0 and 1, it sometimes increased and sometimes decreased, so mark it unsafe
    if 0 in increasing_or_decreasing and 1 in increasing_or_decreasing:
      safe = False

    # If it's still safe, add it to the safe count
    if safe:
      safe_count += 1
    
    if not safe:
      # What if it can be made safe by removing a bad level? Check what happens when we pop out levels
      for x in range(report_length):
        # Copy the report to a new list, removing the level at index 'x' each iteration
        tmp_report = report[:x] + report[x+1:]
        safe = True
        increasing_or_decreasing = []

        for idx in range(report_length-2):
          # Make sure any two adjacent levels differ by at least one and at most three
          distance = abs(int(tmp_report[idx]) - int(tmp_report[idx+1]))
          # If they stay the same or differ too much, mark the report unsafe
          if distance < 1 or distance > 3:
            safe = False
          
          # Next check, did it always increase or always decrease?
          if int(tmp_report[idx]) > int(tmp_report[idx+1]):
            increasing_or_decreasing.append(1)
          elif int(tmp_report[idx]) < int(tmp_report[idx+1]):
            increasing_or_decreasing.append(0)

        # If it only increases once and decreases the rest of the time, or vice versa, it can still be safe
        if 0 in increasing_or_decreasing and 1 in increasing_or_decreasing:
          safe = False

        # If it's still safe, add it to the safe count
        if safe:
          safe_count += 1
    
  print("The number of safe reports is: ", safe_count)

main()