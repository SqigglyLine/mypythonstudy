a = 1
b = 2
c = 3
d = 6

sequence = [a,b,c,d]
smallestNum = sequence[0]
biggestNum = sequence[0]
length = len(sequence)
i = 0
number = 0
#while i < length:
	#if sequence[i] < smallestNum:
		#smallestNum = sequence[i]
	#i += 1
#print('The smallest number is ' + str(smallestNum))
#i = 0
#while i < length:
	#if sequence[i] > biggestNum:
		#biggestNum = sequence[i]
	#i += 1
#print('The biggest number is ' + str(biggestNum))

while i < length:
	number += sequence[i]
	i += 1
number = number / length
print(number)


