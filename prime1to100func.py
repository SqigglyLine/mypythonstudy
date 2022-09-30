
def primefind(num):
	if num == 0:
		return 
	if num == 2 or num == 1:
		print(str(num) + " is a prime number")
		return 
		
	isPrime=True
	for x in range(2, num):
		if num%x == 0:
			isPrime=False
			break
		else:
			isPrime = True
			
	if isPrime:
		print(str(num) + " is a prime number")
		
y = 0
while y <= 100:
	primefind(y)
	y+=1