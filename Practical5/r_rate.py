n = 84 # the initial amount of people that are infected.
r = 1.2 # rate, one infected person can infect r person(s) in one generation.
for i in range (1, 6): # n equals to the total number of infected people.
	n = n * r + n
print ('The r rate is' + str(r) + 'and the total number of individuals infected after 5 generations is' + str(n) + '.')

