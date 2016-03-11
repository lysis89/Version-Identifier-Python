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

	## loop for walking through the lists
	for x in range(0, lineCount):
		## Read each line of the file and place each line in a list.
		line = f.readline()
		values.append(line)
		## Make a copy of the list to be modified for the number conversion.
		digitValues.append(values[x])
		## Check if each charater is a digit, if it isn't it will remove it. 
		## After it performs the check it will replace the orgianl value in the position with the newly formatted version.
		## Example; for 3.0.1 it removes the not numeric charater . and stores the value as 301
		## Next it will append a . at the front of the value. The new value will be .301
		digitValues[x] = ''.join(i for i in digitValues[x] if i.isdigit())
		digitValues[x] = ''.join(('.', digitValues[x]))
	## After converting all of the values to values which can be compared it will then find the highest value and return the position in the array.	
	positionHighestValue = digitValues.index(max(digitValues))
	## After finding the position of the highest value that position is applied to the orignal list and returns that value and removes the '\n' attached.
	return values[positionHighestValue].replace('\n', '')
