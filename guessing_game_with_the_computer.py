import random 
# this is guessing game
def guess_(x):
    a=1
    b=x

    guess=random.randint(1, x)
    print(guess)
    user=0
    while user!=guess:
        user = int(input(f'enter a guess '))
        if user>guess:
            print('guess again ur guess is high')
        elif user<guess:
            print('guess again its low')
    return print(f'u guessed the right number{guess}')
#guess_(10)

def computer_guess(x):
    l=1
    h=x
    feedback=''

    while feedback!='c':
        if l!=h:
            pc_guess = random.randint(1, x)
        else:
            pc_guess=l
        pc_guess=random.randint(1,x)
        feedback=str(input(f'is  {pc_guess} is to low (l),pc guess if high(h),correct(c)'.lower()))
        if feedback=='l':
              h=pc_guess+1
        elif feedback=='h':
              l=pc_guess-1

    print(f'u guessed the right number{pc_guess}')
computer_guess(10)


