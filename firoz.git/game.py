import random
defult_value=20
score=0

print('enter a number your scrore is '+ str(score))
for lotary in range(0,int(defult_value)):
    secretNumber=random.randint(1,6)
    print('take a number between 1 to 6')
    number=int(input())

    if number==secretNumber:
        print('you are win and got  1+ bonus life and your score is added')
        defult_value= int(defult_value)+1
        score=int(score)+secretNumber
        print('score is',score)
        print('life:',defult_value)
        print('the number was',secretNumber)

    else:
        print('you lost')
        defult_value=int(defult_value)-1
        score = int(score)-secretNumber
        print('score is', score)
        print('life:',defult_value)
        print('the number was',secretNumber)
    
