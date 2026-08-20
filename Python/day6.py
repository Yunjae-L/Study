# 파이썬 함수
print("Welcom to Python")
char = len("Welcome to Python")
print(char)

# 함수 정의
def my_function():
    print("Test Function")

my_function()

# 허들넘기1

# 강의버전
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# for step in range(6):
#     jump()

# 내가 짠 버전
# def turn_right():
#     for right in range(3):
#         turn_left()

# for step in range(6):
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# 최종
# def turn_right():
#     for right in range(3):
#         turn_left()

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# for step in range(6):
#     jump()

# 들여쓰기 : 오른쪽으로 4칸 (space 4칸), tab과 혼용하면 안됨 (tab을 4칸 공백으로 설정 후 사용가능)
# IndentationError: 들여쓰기 오류

# While 반복문
# while sometiong_is_true:
#     do_something() repeatedly

# 허들넘기2
# 허들넘기1 과정은 동일하나, 깃발의 위치가 임의대로 변경이 되므로, while문법을 써, 참일경우 jump()를 실행하고, 거짓인 경우 실행하지 않음

# while at_goal() != True:
#    jump()

# while not at_goal():
#     jump()

# 허들넘기3
# The functions move() and turn_left().
# The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
# How to use a while loop and an if statement.
# Your program should also be valid for worlds Hurdles 1 and Hurdles 2.

# 여기서 중요포인트!!
    # 기존에 jump() 정의할떄 맨 처음 move()가 포함되어 있지만,
    # 벽이 있는 경우, jump()를 실행하므로, move()는 지워야함
    # def jump():
    #     turn_left()
    #     move()
    #     turn_right()
    #     move()
    #     turn_right()
    #     move()
    #     turn_left()

# while not at_goal():
#    if wall_in_front():
#        jump()
#    else:
#        move()

# 허들넘기4
# def turn_right():
#     for right in range(3):
#         turn_left()


# jump()의 정의를 수정
# def jump():
#     turn_left()
#     while wall_on_right(): # 조건이 참일경우, move() / 거짓일 경우 실행하지 않고 그 이후 명령어 실행
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear(): # 조건이 참일경우, move() / 거짓일 경우 실행하지 않고 그 이후 명령어 실행
#         move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

# final PJT
# 미로찾기 무한루프 예외가 존재함.
# 초급단계는 15일 강의 후 다시 도전해볼것 권장!
# 우선 넘어가고 이후에 다시 재도전 예정 