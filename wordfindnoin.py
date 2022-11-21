phrase = 'There is a cat over there'
character = 'c'
length = len(phrase)
inWord = True
i = 0

while i < length:
	if phrase[i] == character:
		print(character + ' is in the sentance: ' + phrase)
		inWord = True
		break
	else:
		i += 1
		inWord = False

if inWord == False:
	print(character + ' is not in the sentance: ' + phrase)