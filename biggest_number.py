a = -23
b = -18
c = -45
d = -5

sequence = [a,b,c,d]
biggestNum = sequence[1]
length = len(sequence)
i = 1

while i < length:
	print('Times')
	if sequence[i] > biggestNum:
		biggestNum = sequence[i]
	i += 1
print(biggestNum)