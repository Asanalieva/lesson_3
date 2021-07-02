name = input()
age = int(input())
hobby = input()
if name == 'Aman' and age >=16 and hobby == 'swim':
    print('Hi owner!')
    login = input()
    password = input()
    if login == "soulunthesoil" and password == 'rysyk12':
        print('Aman log ined')
    else:
        print('Incorrect login ot password')
else:
    print('You are not owner!')

if name == 'Aman' and age >=16 and hobby == 'swim':
    print('You are or Aman or you are over 16,or your hobby is swim')
else:
    print('You are not fit!')


