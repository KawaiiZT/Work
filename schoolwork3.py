f='Lip'
print(f.strip())
print(f.lstrip())
print(f.rstrip())

print('I make innovation' .isalnum())
print('Lipda pola'.isalpha())
print('2022'.isnumeric())
print('i make innovation'.islower())
print('I MAKE INNOVATION'.isupper())

lang=['C','Java','python','vb']
print(','.join(lang))
lang2='C Java Python vb'
print(lang2.split(' '))

classitem=['Pencil','eraser','ruler']
classitem.append('board')
print(classitem)
classitem.insert(1,'pen')
print(classitem)
classitem.remove('ruler')
print(classitem)
print(classitem.count('eraser'))
classitem.sort()
print(classitem)

menu_a=['salad','fruit','broccoli']
menu_b=['meat','fish','pork']
print('Choose menu a or b')
select=input()
if select == 'a':
    print('menu a:',menu_a)
if select == 'b':
    print('menu b:',menu_b)
else:
    print('no this menu is not in the menu list')

print('Choose BTS STATION from 1 - 10:')
select=int(input())
if select==0:
    if select==1:
        print('15 baht')
    elif select==2:
        print('20 baht')
    elif select>=3 and select <=4:
        print('30 baht')
    elif select>=5 and select <=6:
        print('40 baht')
    elif select>= 7:
        print('50 baht')
    else:
        print('error')

print(abs(-10))
print(bin(7))
print(hex(100))
print(ord('a'))
print(pow(3,4))
x=range(1,100,2)
for n in x:
    print(n)
num=[12,100,5,97]
print(max(num))
print(min(num))
print(oct(15))
a=12.567
print(round(a,2))
print(sum(num))

from turtle import *
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)

from turtle import*
color=['red','purple','blue','green','yellow','orange']
for x in range(360):
    pencolor(color[x%6])
    width(x/100+1)
    forward(x)
    left(59)

def message(a,b):
    print('Name:',a)
    print('surname:',b)
message('Trisit','Charoenparipat')

def volume(width,height,depth):
    v=widthheightdepth
    print('volume:',v)
    return v
volume (20,20,20)