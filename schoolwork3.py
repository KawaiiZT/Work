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