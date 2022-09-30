num = 2
isPrime=True
for x in range(2, num):
	if num == 2:
		break
	if num%x == 0:
		print('not prime')
		isPrime=False
		break
	else:
		prime = num
	
if isPrime:
	print('prime')

	
