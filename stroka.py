print('введите любое слово или число')
s=input()
str="Это строка в которую новую строку"
position=21
new_str=str[:position-1]+' '+s+' '+str[position:]
print(new_str)
zamena='замена в строке'
new_str=str[:position-1]+' '+zamena+' '+str[position:]
print(new_str)


print(len(new_str))

proverka='строка'
if proverka not in str:
    print('Нет')
else:
    print("Да")