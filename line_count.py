def line_count():
  #We make a variable to count the lines and set it to 0 beacuse some files may have no lines of code
  counter = 0
  #Next I open the file and use r to read the file 
  file = open('file.txt', 'r')
  lines = file.readlines()
  #Now im telling it that for every line we add +1 to counter so we started at 0 now it will add 1 but the next line line counter will equal 1 beacuse we are just adding on 1 for everyline changing the variable
  for line in lines: 
      counter = counter + 1
      #Now we have to close the file and returm the counter
  file.close()
  return counter