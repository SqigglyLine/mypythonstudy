#find average of first 100 even numbers
number = 0
avg = 0
length = 0
while number <= 100:
	if number%2 == 0:
		avg += number
		length += 1
	number += 1
avg = avg / length
print(avg)