word = 'Santhosh'



def reverse():	 
	i = 1
	reversed_word = ''
	length = len(word) 
	while i <= length:
		reversed_word = reversed_word + word[length-i]
		i += 1
	print(reversed_word)
reverse()

