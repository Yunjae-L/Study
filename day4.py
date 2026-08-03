# Random moudule
# ref: https://docs.python.org/3/library/random.html

# import random
# random_integer = random.randint(1,10) # 1<= x <=10 사이 숫자 랜덤
# print(random_integer)

# import는 불러오는 내용이며 day3 파일에서 my_favorite_num을 정의했을 시 그 값을 불러옴
# import random
# import day3
# print(day3.my_favorite_num)

# 임시 부동소수점 
# import random
# random_num_0_to_1 = random.random() * 3
# print(random_num_0_to_1)

# 반올림에 따라 뒤의 숫자가 포함될 수 있음
# import random
# random_flaot = random.uniform(1,7)
# print(random_flaot)

# 임의 대로 동전 앞 뒤 나오게 하기
# import random
# random_head_or_tail = random.randint(0,1)
# if random_head_or_tail == 0:
#     print("head")
# else:
#     print("tail")

# 과제 - 임의 계산자 구하기
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# 1st-option
# import random
# print(random.choice(friends))

#2nd-option 인덱싱을 활용한 방법
# friends_index = random.randint(0,4)
# print(friends[friends_index])

# 중첩 리스트
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [[fruits], [vegetables]]
# print(dirty_dozen)

#final Project - 가위바위보

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [Rock, Paper, Scissors]

import random # 컴퓨터가 무작위 선택을 하기 위해 불러옴
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")) # input 함수는 문자열로 반환됨
print("your_choice:")
print(game_images[your_choice]) # 리스트 인덱싱을 통해 입력한 숫자에 맞는 그림 출력

computer_choice = random.randint(0,2)
print("computer_choice:")
print(game_images[computer_choice]) # 컴퓨터가 선택한 그림 출력

if your_choice >= 3 or your_choice < 0: # 맨 처음 조건문을 통해 0,1,2가 아닌 숫자를 입력했을 때의 예외처리 
    print("You type an invalid number!, you lose!") 
elif your_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and your_choice == 2:
    print("You lose!")
elif your_choice < computer_choice:
    print("You lose!")
elif your_choice > computer_choice:
    print("You win!")
# elif your_choice == computer_choice: # (optional) draw 조건문을 elif로 처리
#     print("It's a draw!")
else:   #draw 조건문을 else로 처리리 (optional)
    print("It's a draw!")
