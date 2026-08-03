#Datatype
# 1. string(문자열)
# print("Hello"[4])

#print(len("123"))
#text = "korea"
#print(type(text))
#print(type(468))
#print(type(5.92))
#print(type(False))

#print("Number of leters in your name: " + str(len(input("Enter your name: "))))

#print("Number of letters in your name: " + len(input("Enter your name: ")))

#user_name = input("Enter your name: ")
#length_of_name = len(user_name)

#print(type ("Number of letters in your name: ")) #str
#print(type (length_of_name)) #int

#print("Number of letters in your name: " + str(length_of_name))

# PEMDAS 연산순서를 나타내며, 동등한 순서일경우 왼쪽에서 오른쪽 순으로 계산
# () 괄호
# ** 지수
#  *  곱셈 or / 나눗셈
# + 덧셈 or - 뺄셈
#print(3*3+3/3-3)

bmi = 84 / 1.65 ** 2
#print(bmi)
#print(int(bmi)) # 정수로 표현, 나머지 버림
#print(round(bmi)) # 반올림

score = 0
# user scores a point
score += 3
#print(score)

# f-String
#print(f"your score is {score}") # TypeError: can only concatenate str (not "int") to str
# 이전에는 str()로 변형을 해서 했음
#print("your score is " + str(score))
# f-String을 사용하면 str()로 변형하지 않아도 됨
#print(f"your score is {score}")

#score = 0
#height = 1.78
#is_winning = False

#print(f"your score is {score} , your height is {height} and your winning is {is_winning}")

# final test
print("Welcome to tip calculator!")
bill = float(input("what was the total bill? $"))
tip = int(input("what percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("how many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill /people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: $){final_amount}")