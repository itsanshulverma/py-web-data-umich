# Author: Anshul Verma

import re

#
#	Multi-line solution
#

#fhand = open("regex_sum_909721.txt")
#sum = 0
#for line in fhand:
#	line = line.strip()
#	nums = re.findall('([0-9]+)', line)
#	if nums:
#		for num in nums:
#			sum += int(num)
#print(n)			
#print(sum)


#
#	One-line solution
#

print(sum([ int(n) for n in re.findall('([0-9]+)', open('regex_sum_909721.txt').read()) ]))


# Output - 443003