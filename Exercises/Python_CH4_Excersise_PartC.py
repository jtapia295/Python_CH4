wordlength = input()

print('Enter a word: ', wordlength)

print('The word ', wordlength, ' contains ', str(len(wordlength)) , " letters")

rec_length = input()
rec_width = input()

print("Rectangle Length: " + str(rec_length) + '''\n''' + 'Rectangle Width: ' + rec_width)
print('The rectangle has an area of ' + str(int(rec_length) * int(rec_width)) + '.')


miles_driven = input()
gallons_used = input()

print("How many miles did you drive? ", str(miles_driven), '''\n''', 'How many gallons did you use?  : ', gallons_used)
print('Your car got ', str(int(miles_driven) // int(gallons_used)), ' miles per gallon.')
