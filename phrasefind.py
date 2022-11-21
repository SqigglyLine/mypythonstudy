phrase = 'There is a cat over there'
character = 'cat'
consecutive = ' '
length = len(phrase)
word = len(character)
inWord = True
flag = True
i = 0
j = 0

while j < word:
	if consecutive == ' ':
		while i < length:
			if phrase[i] == character[j]:
				inWord = True
				break
			else:
				i += 1
				inWord = False
		if inWord:
			j += 1
			consecutive = phrase[i]
		else: 
			print(character + ' is not in the sentance')
			flag = False
			break

	if flag == False:
		break

		flag = True
		
		
	if consecutive == phrase[i]:
		while i < length:
			if phrase[i] == character[j]:
				inWord = True
				break
			else:
				i += 1
				inWord = False
		if inWord:
			j += 1
		else: 
			print(character + ' is not in the sentance')
			flag = False
			break
			
	if flag == False:
		break
#break			


if inWord:
	print(character + ' is in the sentance')