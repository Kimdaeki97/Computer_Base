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

# 04.13
# # 리스트
# numbers = [2, 3, 5, 7, 11, 13]
# names = ["윤수", "혜린", "태호", "영훈"]
#
# # 인덱싱 (indexing)
# num_1 = numbers[1]
# num_3 = numbers[3]
#
# # 리스트 슬라이싱 (list slicing)
# print(numbers[0:4])

print("-------------------------------")
numbers = []
numbers.append(5)
numbers.append(8)
print(numbers)

print("-------------------------------")
numbers = [2, 3, 5, 7, 11, 13, 17, 19]
del numbers[3]

numbers.insert(4, 37)
print(numbers)

print("-------------------------------")
numbers = [19, 13, 2, 5, 3, 11, 7, 17]

sorted(numbers, reverse=True) # -> 기존 리스트는 건드리지 않고, 정렬된 새로운 리스트를 리턴
print(numbers)

print("-------------------------------")
numbers.sort(reverse=True) #-> 아무것도 리턴하지 않고, 기존 리스트를 정렬
print(numbers)


print("-------------------------------")

# 04.15
# 리스트에 값이 있는지 확인하기
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 in primes)
print(12 in primes)

print(7 not in primes)
print(12 not in primes)

# 04.21
# 딕셔너리
my_dictionary = {5: 25, 2: 4, 3: 9, 9: 81}
print(my_dictionary)

for key,value in my_dictionary.items():
    print(key, value)


print("-------------------------------")


# 05.03
import os
print(os.getlogin())
print(os.getcwd())

import random
print(random.random())
print(random.uniform(0,2))

'''
[random 모듈]
스탠다드 라이브러리에 있는 random 모듈은 랜덤한 숫자를 생성하기 위한 다양한 함수들을 제공한다.
- randit 함수
randit은 두 수 사이 어떤 랜덤한 정수를 리턴하는 함수이다.
randit(a, b) 하면 a<= N <=b 사이 랜덤한 수를 리턴한다.

- uniform 함수
uniform 함수는 두 수 사이 랜덤한 소수를 리턴하는 함수이다.
'''

print("-------------------------------")

import datetime
pi_day = datetime.datetime(2021, 5, 3, 13, 6, 5)
print(pi_day)
print(type(pi_day))

today = datetime.datetime.now()
print(today)
print(today.day)
print(today.minute)

# 포맷 코드
print(today.strftime("%A, %B %dth %Y"))

'''
[datetime 모듈]
날짜와 시간을 다루기 위한 다양한 클래스를 갖추고 있다.
'''

# 05.05
full_name = "  Kim, Yuna"
# strip
# 맨 앞,뒤 공백들 제거
print(full_name.split())
# split
print(full_name.split(", "))

# 05.07
with open("new_file", "a") as f:
    f.write("Hello World\n")
    f.write("My name is DAEKI\n")





