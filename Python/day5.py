# For Loop
#     print(fruit + "  == 반복문
# *** 디버깅 모드 확인방법
# python3 -m pdb 파일명
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)pie")
#     print(fruits) # for 들여쓰기 포함되므로 apple, banana, cherry 각각 한 번씩 출력됨
# print(fruits) # for 들여쓰기 포함되지 않으므로 한 번만 출력됨

scores = [90, 34, 78, 99, 57, 100]
# print(sum(scores))

# sum_score = 0
# for score in scores:
#     sum_score += score
# print(sum_score)

# # print(max(scores))
# max_score = 0
# for score in scores:
#     if score > max_score:
#         max_score = score
# print(max_score)

# range() == 범위
# for number in range(1,10, 4): # (a, b) a부터 b-1까지 출력됨 # (a, b, c) a부터 b-1까지 c 간격으로 출력됨
#     print(number)

# Gauss challenge == 1 ~ 100까지의 합 구하기
# sum_num = 0
# for number in range(1, 101):
#     sum_num += number
# print(sum_num)

# for number in range (1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# final project == password generator
import random
Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",("S"),("T"),("U"),("V"),("W"),("X"),("Y"),("Z")]
Symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
Numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? \n"))
nr_symbols = int(input("How many symbols would you like? \n"))
nr_numbers = int(input("How many numbers would you like? \n"))

# Easy Level
# password = ""
# for char in range(0, nr_letters):
#     password += random.choice(Letters)
# for char in range(0, nr_symbols):
#     password += random.choice(Symbols)
# for char in range(0, nr_numbers):
#     password += random.choice(Numbers)
# print(f"your password is: {password}")

# Hard Level
password_List = []
for char in range (0, nr_letters) :
    password_List.append(random.choice(Letters))
for char in range (0, nr_symbols) :
    password_List.append(random.choice(Symbols))
for char in range (0, nr_numbers) :
    password_List.append(random.choice(Numbers))
print(password_List)

# random.shuffle(password_List)
# password = ""
# for char in password_List:
#     password += char
# print(f"your password is: {password}") 