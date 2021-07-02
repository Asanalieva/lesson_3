number = int(input('1st '))
number1 = int(input('2nd '))
operator = input('What to do? *, /, +, - ')
if operator == '*':
    print(number, '*', number1, '=', number * number)
if operator == '/':
    print(number, '/', number1, '=', number / number)
if operator == '+':
    print(number, '+', number1, '=', number + number)
if operator == '-':
    print(number, '-', number1, '=', number - number)

