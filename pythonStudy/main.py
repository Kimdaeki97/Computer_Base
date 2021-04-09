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