#1

lst = [92, 91, 49, 87, 74, 20, 94, 12, 64, 36, 97, 2, 96, 40, 97, 36, 32, 22, 80, 83, 49, 52, 62, 31,
55, 86, 84, 1, 22, 15, 52, 18, 78, 92, 21, 9, 85, 89, 54, 99, 80, 7, 4, 31, 30, 28, 59, 35, 72, 33]

print({index+1:value for index,value in enumerate(lst)})


#2

import random
kol = 0 
print('Ваше имя?')
Your_name = input()
number = random.randint(1,20)
print('Привет, ' + Your_name + ', я загадала число от 1 до 20.')

while kol < 6:
    print('Попробуй угадать число.')
    guess = int(input())
    kol += 1
    if guess < number:
        print('Ваше число слишком маленькое.')  
    if guess > number:
        print('Ваше число слишком большое.')
    if guess == number:
        break

if guess == number:
    kol = str(kol)
    print('Отлично, ' + Your_name + '! Вы справились за' + kol + ' попытки!')

if guess != number:
    number = str(number)
    print('Увы. Я загадала ' + number + '.')  



#3
some_string = 'Adverts'
some_string[2:5]

#4

a = 'Adilet'
b = 'Aidana'
print(a[0],b[0], a[2],b[2], a[1],b[1], b[3],a[3], b[4],a[4], b[5],a[5]) 