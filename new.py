import re
# pls download the txt from the link 
fhand = open('regex_sum_1278144.txt')
tosum = 0

for line in fhand:
	numlist = re.findall('[0-9]+',line)
	if len(numlist) > 0:
		for item in numlist:
			tosum = tosum + int(item)
print(tosum)
	
