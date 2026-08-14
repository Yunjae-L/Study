# if/else 
# if condition:
#    do this
# else:
#    do this else

#water_level = int(input("Enter the water level: "))
#if water_level >100:
#    print("Drain water")
#else:
#    print("Continue filling water")


#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm? "))
#if height >= 120:
#    print("Congratulations! You can ride the rollercoaster!")
#else:
#    print("Sorry, you have to grow taller before you can ride.")

# 연산자
# > , < ~보다 크다,작다
# >= , <= ~보다 크거나 같다, 작거나 같다
# == , != 같다, 같지않다
# 등호 개념
# = 변수에 값을 할당할때 사용 , == 비교할때 사용 (같다)

# modulus 연산자
# % 나머지 값을 반환함

#num = int(input("Enter a number: "))

# 홀수,짝수 확인
#if num % 2 == 0:
#    print("The number is even")
#else:
#    print("The number is odd")

# 중첩 if문 
# 처음에는 키를 확인하였고, 키가 120 이상일때 나이확인

#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm? "))
#if height >= 120:
#    print("Congratulations! You can ride the rollercoaster!")
#    age = int(input("What is your age? "))
#    if age < 12:
#        print(("Child tickets are $5."))
#    else:
#        print("Adult tickets are $12.")
#else:
#    print("Sorry, you have to grow taller before you can ride.")

# 중첩에서 elif 사용 (조건이 여러개일때 사용)
#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm? "))
#if height >= 120:
#    print("Congratulations! You can ride the rollercoaster!")
#    age = int(input("What is your age? "))
#    if age < 12:
#        print(("Child tickets are $5."))
#    elif age <= 18:
#        print("Youth tickets are $7.")
#    else:
#        print("Adult tickets are $12.")
#else:
#    print("Sorry, you have to grow taller before you can ride.")

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
# if height >= 120:
#    print("Congratulations! You can ride the rollercoaster!")
#    age = int(input("What is your age? "))
#    if age < 12:
#        bill += 5
#        print((f"child tickets are ${bill}."))
#    elif age <= 18:
#        bill += 7
#        print(f"Youth tickets are ${bill}.")
#    else:
#        bill += 12
#        print(f"Adult tickets are ${bill}.")
# else:
#    print("Sorry, you have to grow taller before you can ride.")


# multiple if 
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# if height >= 120:
#     print("Congratulations! You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print(("Child tickets are $5."))
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")

#     want_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
#     if want_photo == "y":
#         # Add $3 to their bill
#         bill += 3 # bill = bill + 3 
#     print(f"Your final bill is ${bill}")
# else:
#       print("Sorry, you have to grow taller before you can ride.")

# 피자 주문하기 
# Info.
# small pizza: $15
# Medium pizza: $20
# large pizza: $25
# Add pepperoni for Small pizza(Y or N): $+2
# Add pepperoni for Medium or Large pizza(Y or N): $+3
# Add extra cheese for anysize pizza(Y or N): $+1


# print("Welcome to python pizza Deliveries!")
# size = input("What size pizza do you wants? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# bill = 0
# if size == "S":
#     bill+= 15
# elif size == "M":
#     bill+= 20
# elif size == "L":
#     bill+= 25
# else:
#     print("you don't want to pizza")

# if pepperoni == "Y":
#     if size == "S":
#         bill+= 2
#     else:
#         bill+= 3

# if extra_cheese == "Y":
#     bill+= 1

# print(f"You final bill is: ${bill}. ")    

# logic operators
# and - 조건이 모두 참 이여아만 참, 하나라도 거짓이면 거짓
# or - 조건 중 하나만 참이여도 참, 모두 거짓인 경우에만 거짓
# Not - 참 -> 거짓, 거짓-> 참으로 뒤집음.

#Not 예시 >> 중년의 위기를 겪는 모든사람들에게 입장권 free (중년의 위기: 45~55)
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
# if height >= 120:
#     print("Congratulations! You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill += 5
#         print((f"Child tickets are ${bill}."))
#     elif age <= 18:
#         bill += 7
#         print(f"Youth tickets are ${bill}.")
#     elif 45 <= age <= 55:
#         print("your age tickets are free")
#     else:
#         bill += 12
#         print(f"Adult tickets are ${bill}.")

#     want_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
#     if want_photo == "y":
#         # Add $3 to their bill
#         bill += 3 # bill = bill + 3 
#     print(f"Your final bill is ${bill}")
# else:
#       print("Sorry, you have to grow taller before you can ride.")

# 3 Days project

# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/[TomekK]
# *******************************************************************************)
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")

# choice1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' \n").lower()

# if choice1 == "left":
#     choice2 = input("You've come to a lake. There is an island in the middle of the lake. " \
#     "Type 'wait' to wait for a boat. " \
#     "Type 'swim' to swim across. \n").lower()
    
#     if choice2 == "wait":
#         choice3 = input("You arrive at the island unharmed. " \
#         "There is a house with 3 doors. One red, one yellow and one blue. " \
#         "Which colour do you choose? \n").lower()
        
#         if choice3 == "yellow":
#             print("You found the treasure! You Win!")
#         elif choice3 == "red":
#             print("It's a room full of fire. Game Over.")
#         elif choice3 == "blue":
#             print("You enter a room of beasts. Game Over.")
#         else:
#             print("You chose a door that doesn't exist. Game Over.")
            
#     else:
#         print("You get attacked by an angry trout. Game Over.")
# else:
#     print("You fell into a hole. Game Over.")

my_favorite_num = 66
