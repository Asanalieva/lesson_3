posuda = 'Ok'
if posuda == 'Ok':
    print('Пойдешь гулять')
else:
    print("Don't Go")
name = input('Введите ваше имя ')
if name == 'Sultanmurat':
    age = int(input())
    if age > 16:
         hobby = input('Write your hobby ')
         if hobby =='book':
             print('Приветствую хозяин!')
         else:
             print('He loves book!')
    else:
        print('Sultanmurat is 17!')
else:
    print('Вы не хозяин')