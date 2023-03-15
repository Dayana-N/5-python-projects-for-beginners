print('Welcome To Car Brand Anagram Quiz')

playing = input('Do you want to play? ')
if playing.lower() != 'yes':
    quit()

print('Okay, Lets Play! ')
score = 0

answer = input('What model is YTOOAT ')
if answer.lower() == 'toyota':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('What model is YUNDHAI ')
if answer.lower() == 'hyundai':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('What model is OFDR ')
if answer.lower() == 'ford':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('What model is GRONIMLABIH ')
if answer.lower() == 'lamborghini':
    print('Correct!')
    score += 1
else: 
    print('Incorrect')

print('You got ' + str(score) + ' questions correct!')
print('You got ' + str((score / 4) * 100) + ' % correct')
