# x = 2 # 글로벌 변수
#
# def my_function():
#     x = 3  # 로컬 변수
#     print(x)
#
# my_function()
# print(x)
#
# # 상수는 일반 변수와 구분 짓기 위해 대문자로 표기한다.
# # 실수를 방지하기 위해서이기도 함
# # 상수는 절대 바꾸지 않겠다는 의지(?)를 표현
#
# PI = 3 # 상수
# def calculate_area(r):
#     return PI * r * r

# 04.09 - 거스름돈 계산 프로그램
def calculate_change(payment, cost):
    left = payment - cost

    fifty = left // 50000
    ten = (left % 50000) // 10000
    five = (left % 10000) // 5000
    one = (left % 5000) // 1000

    print("50000원 지폐: {}장".format(fifty))
    print("10000원 지폐: {}장".format(ten))
    print("5000원 지폐: {}장".format(five))
    print("1000원 지폐: {}장".format(one))


calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)

# 04.10
# while문을 사용하여, 100 이상의 자연수 중 가장 작은 23의 배수를 출력하기
i = 100

while i % 23 != 0:
    i += 1

print(i)

# while 반복문을 사용하여 1이상 100이하 짝수를 모두 출력하기
# i = 1
# while i <= 50:
#     print(i * 2)
#     i += 1

print("-------------------------------")
# 04.11
temperature = 11
if temperature <= 10:
    print("자켓을 입는다.")
else:
    print("자켓을 입지 않는다.")

print("-------------------------------")
# 학점 계산기
def print_grade(midterm_score, final_score):
    total = midterm_score + final_score

    if total >= 90:
        print("A")
    elif 90 > total >= 80:
        print("B")
    elif 80 > total >= 70:
        print("C")
    elif 70 > total >= 60:
        print("D")
    else:
        print("F")

print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)

print("-------------------------------")
# 100이하 자연수 중 8의 배수이지만, 12의 배수는 아닌 것은
i = 1
while i <= 100:
    if (i % 8 == 0) and (i % 12 != 0) :
        print(i)
    i += 1

print("-------------------------------")
# 1,000보다 작은 자연수 중 2 또는 3의 배수의 합은?
i = 1
total = 0

while i < 1000:
    if (i % 2 == 0) or (i % 3 == 0):
        total += i
    i += 1

print(total)

print("-------------------------------")
# 정수 120의 약수를 모두 출력하고, 총 몇개의 약수가 있는지 출력하는 프로그램
i = 1
count = 0

while i <= 120:
    if 120 % i == 0:
        print(i)
        count += 1
    i += 1

print("120의 약수는 총 {}개 입니다.".format(count))

print("-------------------------------")





