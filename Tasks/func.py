'''
Найдите три ключа с самыми высокими значениями в словаре
'''
max_3=[]
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
for i in my_dict.values():
    max_3.append(i)
print(sorted(max_3)[-3:])