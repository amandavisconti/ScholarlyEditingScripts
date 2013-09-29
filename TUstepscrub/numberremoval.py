# Copied whole from http://goo.gl/tePnrO. Need to adapt this to write to file instead of printing into the terminal when I have the time!

import sys
import re

def remove_line_numbers(line):
  components = re.split("\s+",line)
  if(re.search("\d+:?",components[0])):
    return " ".join(components[1:])
  else:
    return line

if __name__ == "__main__":
	file = sys.argv[1]
	fhnd = open(file,"r")
	for line in fhnd:
	  line = remove_line_numbers(line)
	  print line
	fhnd.close()