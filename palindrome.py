#this program finds if a string is palindrome
word = 'nook'

i = 1
reversed_word = ''
length = len(word) 
while i <= length:
	reversed_word = reversed_word + word[length-i]
	i += 1

if word == reversed_word:
	print(word + ' is a palindrome')
else:
	print(word + ' is not a palindrome')

