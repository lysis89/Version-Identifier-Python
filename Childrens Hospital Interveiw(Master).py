## 1. You have a dataset of strings in a file. 
##    Each line represents a version number of software like this:
##    number.number...number.
##	  Example: 
##			1;
##			1.1;
##			0.1;
##			3.0.1
##			0;
##			01.02.03;
##			0.0.0...1;
##			3.0;
## 2. Write a program that reads the file and prints the latest software
##	  version(in the above example it is 3.0.1). Use a programming langauge
##    of your choice. Please use comments to explain what you are doing.
## Sample File Name: version_data.txt
## Convert each value in the string into seperate integers.
## Evaluate the newly created integer for the highest digitValues.
## Then Check the Second value for the highest digitValues.
## Check the third value for the highest digitValues.


def main(filename):
	f= open(filename, "r")
	lineCount = sum(1 for line in open(filename))
	values = []
	digitValues = []
	
	for x in range(0, lineCount):
		line = f.readline()
		values.append(line)
		digitValues.append(values[x])
		digitValues[x] = ''.join(i for i in digitValues[x] if i.isdigit())
		digitValues[x] = ''.join(('.', digitValues[x]))
	positionHighestValue = digitValues.index(max(digitValues))
	return values[positionHighestValue].replace('\n', '')
