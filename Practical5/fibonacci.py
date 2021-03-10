a = 0 # This is the 0th number of the sequence.
b = 1 # This is the 1st number of the sequence.
print b # output the 1st number.
for i in range (1, 13): # the upper fence is final number what we need.
	c = a + b   # a and b move forward one space in each loop. c is always at the first place.
	a = b
	b = c
	print c       # I print each of c after each loop
