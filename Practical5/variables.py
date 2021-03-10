a = 200902
b = 190784
c = 100321
d = a - c
e = a - b
compare = d > e
print ("d > e ?", compare)
X = 1
Y = 0
Z = (X and not Y) or (Y and not X)
print Z
W = X != Y
import random
for i in range (1, 11):
	X = random.randint(0, 1)
	Y = random.randint(0, 1)
	print ("X = ", X, "Y = ", Y, "Z == W ?", Z == W)

