print('Welcome to the easiest game of your life')
playing = input('Are you ready to play? ')

score = 0

if playing.lower() != 'yes':
    quit()

print("Okay let's play!!!!!!!!")

answer = input("What does CPU stand for? ")
if answer.lower() == 'central processing unit':
    print('Correct!')
    score = score+1
else:
    print("Incorrect!")
    score = score-1

answer = input("what does GPU stand for? ")
if answer.lower() == 'graphics processing unit':
    print('Correct!')
    score = score+1
else:
    print("Incorrect!")
    score = score-1

answer = input("what does RAM stand for? ")
if answer.lower() == 'random access memory':
    print('Correct!')
    score=score+1
else:
    print("Incorrect!")
    score=score-1


print("Your total score is: ", score)
print("You've got", (score/3) *100, '% questions correct!')
if score == 3:
    print("Congrats! you have won the game!")
else:
    print("Try Again!")