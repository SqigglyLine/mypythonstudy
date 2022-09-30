isPrime=True
y = 3
print(2)
while y <= 100:
		
	for x in range(2, y):
		if y%x == 0:
			isPrime=False
			break
		else:
			isPrime = True
			
	if isPrime:
		print(y)
	y+=1
	
	
