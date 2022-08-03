x = "mom"
w = ""
for i in x:
    w = i + w
if (x == w):
    print("Yes")
else:
    print("No")



# dict1 = {'year': None, 'month': None, 'Day': None}
# d = input("Write date: ")
# a = d.split()
# dict1['year'] = a[0]
# dict1['month'] = a[1]
# dict1['Day'] = a[2]
# print(dict1)


# num = "4729461084"
# b = 0
# for i in range(len(num)):
# 	a = int(num[i])
# 	b = a + b
# print(b)
# 
# a = [1, 1, 2, 3, 13, 13, 13, 13, 13, 13, 13, 13, 13, 5, 8, 13, 21, 34,1,55, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 1313, 13, 13, 13, 13, 13, 89]
# a.append(13)
# b = a.count(13)
# len(a)
# c = b*100/len(a)
# if c <70 :
#     print("НЕУЖЕЛИ")
# if c>70 :
#     print("Я ТАК И ЗНАЛ")
# if c ==70 :
#     print("СОВПАДЕНИЕ, НЕ ДУМАЮ")

# Задача 3

# username = input("Please create your username: ")
# password = input("Please create the password: ")
# users = [username, password]
# print("Great! The user is logged in succesfully.")
# username_ = input("Please enter your username: ")
# password_ = input("Please enter your password: ")
# if username_ == users[0]:
#     if password_ == users[1]:
#         print("Добро пожаловать.")
#     else:
#         print("Неправильный логин или пароль")
# else:
#     print("Неправильный логин или пароль")

# a = ['Bish', 'osh', 'batken','karakol', 'kant', 'naryn', 'talas']
# while True:
#     command = input('''Выберите действие: 
#     > Добавить 
#     > Отобразить
#     > Заменить 
#     > Удалить 
#     > Выход
#     > ''')
#     if command == 'добавить':
#         add = input('Добавьте новый город: ')
#         if add not in a:
#             a.append(add)
#             print('Город успешно добавлен')
#         else:
#             print('Такой город уже есть')
#     elif command == 'отобразить':
#         print(', '.join(a))
#     elif command == 'удалить':
#         print(', '.join(a))
#         rem = input('Выберите город для удаления:')
#         if rem not in a:
            
#             print('Такого города нет')
#         else:
#             a.remove(rem)
#             print('Город успешно удален')
#     elif command == 'выход':
#         break

#     elif command == 'заменить':
#         print(', '.join(a))
#         replace = input('Выберите город для замены: ')
#         replace2 = input('Введите название города: ')
#         if replace  in a:
#             a.remove(replace)
#             a.append(replace2)
#         else:
#             print('Такого города нет')h,