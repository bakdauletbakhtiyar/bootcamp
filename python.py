# d = 0
# password = input("Write the password:")

# for i in password:
#     if(i.isdigit()):
#         d+=1
# if(len(password) > 6):
#     if d >= 5:
#       print("True")
#     else:
#         print("False")

# strs = ['ccc', 'aaaa', 'd', 'bb']
# print(sorted(strs, key=len)) ['d', 'bb', 'ccc', 'aaaa']

# def search_algo(num, items):
#     for item in items:
#         if item == num:
#             return True
#         else:
#             return False
# nums = [2, 4, 6, 8, 10]

# print(search_algo(2, nums))


# height = int(input("Enter your height: "))
# age = int(input("Enter your age: "))
# price = 0
# if height >= 120 and age >= 9:
#     if age >= 0 and age <= 9:
#         price += 10
#         print("You are welcome! " , "Pay:" , price)
#     elif age >= 9 and age <= 18:
#         price += 15
#         print("You are welcome! " , "Pay:" , price)
#     else:
#         price += 20
#         print("You are welcome! " , "Pay:" , price)
# else:
#     print("Vhoda net")
# take_photo = input("Do you want a photo? ")
# if take_photo == "Yes":
#     price += 5
#     print("Pay:",price, ".Have a great time! ")
# else:
#     print("Have a great time! ")
# from itertools import count
# from operator import contains
# from re import L
# first_name = input("Enter the first name: ").lower()
# second_name = input("Enter the second name: ").lower()
# t = first_name.count("t")
# r = first_name.count("r")
# u = first_name.count("u")
# e = first_name.count("e")
# l = second_name.count("l")
# o = second_name.count("o")
# v = second_name.count("v")
# e = second_name.count("e")
# print((t + r + u + e) * 10 + (l + o + v + e))

# print("Hello. Let's play labyrinth. You can Go to the Top(T),Go down(D), Turn Right(R) or Turn Left(L). Good luck:) ")
# print("'#' is the wall. '@' is the exit. 'Y' is you.")
# print("The map: ")
# print(" ##Y#########\n",
#     "##       ###\n",
#     "####### ####\n",
#     "####    ## #\n",
#     "###  ####  #\n",
#     "###       ##\n",
#     "#########@##\n"
#  )
# a = input("Your choice: ")
# if a.lower() == "d":
#     print(" ## #########\n",
#         "##Y      ###\n",
#         "####### ####\n",
#         "####    ## #\n",
#         "###  ####  #\n",
#         "###       ##\n",
#         "#########@##\n"
#     )
#     b = input("Your choice: ")
#     if b.lower() == "r":
#         print(" ## #########\n",
#             "## Y     ###\n",
#             "####### ####\n",
#             "####    ## #\n",
#             "###  ####  #\n",
#             "###       ##\n",
#             "#########@##\n"
#         )
#         c = input("Your choice: ")
#         if c.lower() == "r":
#             print(" ## #########\n",
#             "##  Y    ###\n",
#             "####### ####\n",
#             "####    ## #\n",
#             "###  ####  #\n",
#             "###       ##\n",
#             "#########@##\n"
#             )
#             d = input("Your choice: ")
#             if d.lower() == "r":
#                 print(" ## #########\n",
#                 "##   Y   ###\n",
#                 "####### ####\n",
#                 "####    ## #\n",
#                 "###  ####  #\n",
#                 "###       ##\n",
#                 "#########@##\n"
#                 )
#                 e = input("Your choice: ")
#                 if e.lower() == "r":
#                     print(" ## #########\n",
#                     "##     Y ###\n",
#                     "####### ####\n",
#                     "####    ## #\n",
#                     "###  ####  #\n",
#                     "###       ##\n",
#                     "#########@##\n"
#                     )
#                     f = input("Your choice: ")
#                     if f.lower() == "d":
#                         print(" ## #########\n",
#                         "##       ###\n",
#                         "#######Y####\n",
#                         "####    ## #\n",
#                         "###  ####  #\n",
#                         "###       ##\n",
#                         "#########@##\n"
#                         )
#                         g = input("Your choice: ")
#                         if g.lower() == "d":
#                             print(" ## #########\n",
#                             "##       ###\n",
#                             "####### ####\n",
#                             "####   Y## #\n",
#                             "###  ####  #\n",
#                             "###       ##\n",
#                             "#########@##\n"
#                             )
#                             h = input("Your choice: ")
#                             if h.lower() == "l":
#                                 print(" ## #########\n",
#                                 "##       ###\n",
#                                 "####### ####\n",
#                                 "####  Y ## #\n",
#                                 "###  ####  #\n",
#                                 "###       ##\n",
#                                 "#########@##\n"
#                                 )
#                                 i = input("Your choice: ")
#                                 if i.lower() == "l":
#                                     print(" ## #########\n",
#                                     "##       ###\n",
#                                     "####### ####\n",
#                                     "#### Y  ## #\n",
#                                     "###  ####  #\n",
#                                     "###       ##\n",
#                                     "#########@##\n"
#                                     )
#                                     j = input("Your choice: ")
#                                     if j.lower() == "l":
#                                         print(" ## #########\n",
#                                         "##       ###\n",
#                                         "####### ####\n",
#                                         "####Y   ## #\n",
#                                         "###  ####  #\n",
#                                         "###       ##\n",
#                                         "#########@##\n"
#                                         )
#                                         if input("Your choice: ") == "d":
#                                             print(" ## #########\n",
#                                             "##       ###\n",
#                                             "####### ####\n",
#                                             "####    ## #\n",
#                                             "### Y####  #\n",
#                                             "###       ##\n",
#                                             "#########@##\n"
#                                             )
#                                             if input("Your choice: ") == "d":
#                                                print(" ## #########\n",
#                                                 "##       ###\n",
#                                                 "####### ####\n",
#                                                 "####    ## #\n",
#                                                 "###  ####  #\n",
#                                                 "### Y     ##\n",
#                                                 "#########@##\n"
#                                                 )
#                                                if input("Your choice: ") == "r":
#                                                    print(" ## #########\n",
#                                                     "##       ###\n",
#                                                     "####### ####\n",
#                                                     "####    ## #\n",
#                                                     "###  ####  #\n",
#                                                     "###  Y    ##\n",
#                                                     "#########@##\n"
#                                                     )
#                                                    if input("Your choice: ") == "r":
#                                                         print(" ## #########\n",
#                                                         "##       ###\n",
#                                                         "####### ####\n",
#                                                         "####    ## #\n",
#                                                         "###  ####  #\n",
#                                                         "###   Y   ##\n",
#                                                         "#########@##\n"
#                                                         )
#                                                         if input("Your choice: ") == "r":
#                                                             print(" ## #########\n",
#                                                             "##       ###\n",
#                                                             "####### ####\n",
#                                                             "####    ## #\n",
#                                                             "###  ####  #\n",
#                                                             "###    Y  ##\n",
#                                                             "#########@##\n"
#                                                             )
#                                                             if input("Your choice: ") == "r":
#                                                                 print(" ## #########\n",
#                                                                 "##       ###\n",
#                                                                 "####### ####\n",
#                                                                 "####    ## #\n",
#                                                                 "###  ####  #\n",
#                                                                 "###     Y ##\n",
#                                                                 "#########@##\n"
#                                                                 )
#                                                                 if input("Your choice: ") == "r":
#                                                                     print(" ## #########\n",
#                                                                     "##       ###\n",
#                                                                     "####### ####\n",
#                                                                     "####    ## #\n",
#                                                                     "###  ####  #\n",
#                                                                     "###      Y##\n",
#                                                                     "#########@##\n"
#                                                                     )
#                                                                     if input("Your choice: ") == "d":
#                                                                         print("Congratulations. You won. You completed the game!")
#                                                                     else:
#                                                                         print("End of the game")

#                                                                 else:
#                                                                     print("End of the game")
#                                                             else:
#                                                                 print("End of the game")
#                                                         else:
#                                                             print("End of the game")
#                                                    else:
#                                                         print("End of the game")
#                                                else:
#                                                     print("End of the game") 
#                                             else:
#                                                 print("End of the game") 
#                                         else:
#                                             print("End of the game")
#                                     else:
#                                         print("End of the game")
#                                 else:
#                                     print("End of the game")
#                             else:
#                                 print("End of the game")
#                         else:
#                             print("End of the game")
#                     else:
#                         print("End of the game")
#                 else:
#                     print("End of the game")
#             else:
#                 print("End of the game")
#         else:
#             print("End of the game")
#     else:
#         print("End of the game")
# else:
#     print("End of the game")

# min_s = s[: len(s)//2]
# # print(s[::3]) 
# string = input("Write your sentence: ")
# half = len(string) // 2
# s_first_half = string[: half]
# s_second_half = string[half + 1 : len(string)]
# print(s_first_half.upper(), " + " , s_second_half.lower())

# string = input("Write your word: ")
# print("Your word contains", len(string), "elements.")
# print("Here we have", string.count("a"), "a characters and", string.count("b"), "b characters.")


# password = input("Write your password: ")
# if password.isDigit():
#     print("Wrong password")
# elif password.isalpha():
#     print("Wrong password.")
# else:
#     print("You are welcome.")



# write_word = input("Write your text here: ")
# print(write_word.lower())
# print(write_word.title())



# print_word = input("Write your text: ")
# print("Palindrome of this word is ", print_word[::-1])
# from curses.ascii import isdigit


# first = ('apple', 1, 12)
# second = (2.23, 123.23)
# third = (1, 34)
# fourth = (True, False)
# fifth = (5)
# list = [first, second, third, fourth]
# list.append(fifth)
# print(list)
# print(first[0], first[1], first[2])

# list = []
# list1 = [1]
# list2 = [2]
# list3 = [3]
# list4 = [4]
# list5 = [5]
# # list.extend([list1, list2, list3, list4, list5])
# [list1].join([list])

# # print(list)
# names = ['b', 'a', 'c' , 'k']
# string = ''
# print(string.join(names))

# list_one = [1,2,3]
# list_two = [4,5,6]
# print(list_one + list_two)

# list_names = ['Bakdaulet', 'Jack' ,'Oskar', 'Baksa', 'Jack', 'Oskar']
# print(list_names.count('Jack'))

# for i in list_names:
#     if i == 'Oskar':
#         list_names.remove('Oskar')
# print(list_names)

# list_myself = []
# list_myself.append("Bakdaulet")
# list_myself.append(2003)
# list_myself.append('Python')
# list_myself.append('loop')
# print(list_myself)
# list_myself.pop(list_myself.index('loop'))
# print(list_myself)

# google_collab = [1,2,3,4,5]
# print(google_collab[0] * google_collab[1] * google_collab[2] * google_collab[3] * google_collab[4])



# list_1 = [1, 'a', 2, 'b', 3, 'c', 4]
# letters = []
# numbers = []
# x = len(list_1)
# for i in range(x):
#     if type(list_1[i]) is int:
#         numbers.append(list_1[i])
#     else:
#         letters.append(list_1[i])
# print(letters)
# print(numbers)

# print(list_1[1 : 4])

# city = {
#     'Nur-Sultan': 403433,
#     'Almaty': 321432,
#     'Shymkent': 777777
# }
# print(city)

# dates_of_birth = {1,2,3,4,5,9}
# nums = {4,5,6,7,8}
# dates_of_birth.remove(7)
# print(dates_of_birth)
# dates_of_birth.add(7)
# dates_of_birth.pop()
# print(dates_of_birth)
# c = dates_of_birth.intersection(nums)
# print(c)

# dates_of_birth.difference(nums)
# nums.discard(dates_of_birth)
# print(nums)

# dict1 = {'Nur-Sultan': 1, 'Almaty': 2, 'Shymkent': 17}
# dict2 = {'Alamty-obl': 5, 'Taraz': 8}
# dict1.update(dict2)
# print(set(dict1))

# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica")

# c = a.zip()

# print(c)

# #while
# x = 5
# while x < 3:
#     print(x)
#     x+=1
# password = input("Please enter your password: ")
# num = 0
# while password != "qwerty":
#     password = input("Error. Please enter correct password.")
#     num += 1
#     if num > 3:
#         print("You tried 5 times. Later...")
#         break
# if num < 4:
#     print("Correct password! Congratulations.")



# a = 'sdsfgrtJAfsdISdfsdmf'
# i = 0
# while len(a)>0:
#     bukva = a[i]
#     i+=1
#     if bukva.islower():
#         print(bukva,"is small")
#     elif bukva.isupper():
#         print(bukva,"is big")



# a = '*'
# num = int(input("Write your number: "))
# for i in range(num):
#     print(a*i)
# for j in range(num,0,-1):
#     print(a*j)



# import random
# import string
# alphabets = list(string.ascii_letters)
# digits = list(string.digits)
# special_characters = list("!@#$%^&*")
# alphabets_count = int(input("How many letters must be in password: "))
# digits_count = int(input("How many digitts must be in password: "))
# characters_count = int(input("How many special characters must be in password: "))
# password = []
# for i in range(alphabets_count):
#     password.append(random.choice(alphabets))
# for i in range(digits_count):
#     password.append(random.choice(digits))
# for i in range(characters_count):
#     password.append(random.choice(special_characters))
# random.shuffle(password)
# print("".join(password))




# n = int(input())
# arr = map(int, input().split())
# print(sorted(list(set(arr)))[-2])
# names = []
# scores = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     names.append(name)
#     scores.append(score)
# x = min(scores)
# scores.remove(x)
# y = min(scores)
# print(x,y)




# b = 0
# for i in range(100):
#     if i % 2 == 0:
#         b = b + i
# print(b)

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
#             print('Такого города нет')


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


# print("Нажмите на кнопку ноль чтобы закончить процесс"
#       "\nзавершит работу программы")
# while True:
#     s = input("Выберите знак (+,-,*,/): ")
#     if s == '0':
#         break
#     if s in ('+', '-', '*', '/'):
#         x = float(input("1 значение = "))
#         y = float(input("2 значение = "))
#         if s == '+':
#             print("%.2f" % (x+y))
#         elif s == '-':
#             print("%.2f" % (x-y))
#         elif s == '*':
#             print("%.2f" % (x*y))
#         elif s == '/':
#             if y != 0:
#                 print("%.2f" % (x/y))
#             else:
#                 print("Деление на ноль!")
#     else:
#         print("Неверный знак операции!")
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
# a = int(input())
# b = 0
# for i in range(a):
#     if i%3==0 or i%5==0:
#        b = b + i
# print(b)
# dict1 = {'a': 5, 'b': 3, 'c': 8, 'd': 14}
# if dict1['b']%3==0:
#    print("hi")
# if dict1['a']%5==0:
#     print("Bye")



#task 2 zadacha 2

# a = int(input("The number of languages: "))
# languages = []
# for i in range(a):
#     languages.append(input())
# for i in range(a):
#     print(i, end = " ")
#     print(languages[i])
    

# num = "4729461084"
# b = 0
# for i in range(len(num)):
# 	a = num[i]
# 	b = a + b
# print(a)
# print(4+7+2+9+4+6+1+0+8+4)
