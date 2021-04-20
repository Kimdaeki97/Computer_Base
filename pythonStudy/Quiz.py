# # 04.12
#
# INTEREST_RATE = 0.12
# ARPARRTMENT_PRICE = 1100000000
#
# year = 1988
# bank_balance = 50000000
#
# while year < 2016:
#     bank_balance = bank_balance * (1 + INTEREST_RATE)
#     year += 1
#
# print(bank_balance)
#
# if bank_balance > ARPARRTMENT_PRICE:
#     print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(int(bank_balance - ARPARRTMENT_PRICE)))
# else:
#     print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(int(ARPARRTMENT_PRICE - bank_balance)))
#
# print("-------------------------------")
#
# i = 1
# previous = 0
# current = 1
#
# while i <= 50:
#     print(current)
#
#     # # 1번 방법
#     # temp = previous # previous를 임시 저장소인 temp에 저장
#     # previous = current
#     # current = current + temp # temp에는 기존 previous 값이 저장되어있음
#
#     # 2번 방법
#     previous, current = current, current + previous
#
#     i += 1
#

# print("-------------------------------")

#
# # 구구단 (중첩 while 문)
# dan = 1
# while dan <= 9:
#     hang = 1
#     while hang <= 9:
#         print("{} * {} = {}".format(dan, hang, dan * hang))
#         hang += 1
#     dan += 1
#

# print("-------------------------------")


# # 04.14
# # 리스트 원소를 모두 출력하기
# greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]
#
# i = 0
# while i <= len(greetings):
#     print(greetings[i])
#     i += 1
#

# print("-------------------------------")


# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(F):
    return (F - 32)*5 / 9

temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

i = 0
while i < len(temperature_list):
    temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]), 1)
    i += 1

# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드를 입력하세요.
print("섭씨 온도 리스트: {} ".format(temperature_list))  # 섭씨 온도 출력


print("-------------------------------")


# 04.15
# 원화(￦)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    return krw / 1000

# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    return usd * 125

# 원화(￦)으로 각각 얼마인가요?
prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: {} ".format(prices) )

# amounts를 원화(￦)에서 달러($)로 변환하기
i = 0
while i < len(prices):
    prices[i] = int(krw_to_usd(prices[i]))
    i += 1

# 달러($)로 각각 얼마인가요?
print("미국 화폐: " + str(prices))

# amounts를 달러($)에서 엔화(￥)으로 변환하기
i = 0
while i < len(prices):
    prices[i] = round(usd_to_jpy(prices[i]), 1)
    i += 1

# 엔화(￥)으로 각각 얼마인가요?
print("일본 화폐: " + str(prices))


print("-------------------------------")


# 빈 리스트 만들기
numbers = []
print(numbers)

# numbers에 값들 추가
numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)
print(numbers)

# numbers에서 홀수 제거
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 1:
        del numbers[i]
    else:   # <- 핵심
        i += 1
print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
numbers.insert(0, 20)
print(numbers)

# numbers를 정렬해서 출력
numbers.sort()
print(numbers)

# 04.16
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# 인덱스와 원소 출력
for i in range(len(numbers)):
    print(i, numbers[i])

# 2의 제곱 출력
for i in range(11):
    print("{}^{} = {}".format(2, i, 2 ** i))

# 구구단 출력, 반복문 사용
for i in range(1,10):
    for j in range(1,10):
        print("{} * {} = {}".format(i, j, i*j))


print("-------------------------------")


# 04. 19
#a + b + c = 1000을 만족하는 피타고라스 삼조 구하기

for a in range(1, 1000):
    for b in range(1, 1000):
        c = 1000 - a - b
        if a * a + b * b == c * c and a < b < c:
            print(a * b * c)

print("-------------------------------")

# 04. 20

# for문을 이용해서 리스트 뒤집기
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
for left in range(len(numbers) // 2):
    # 인덱스 left와 대칭인 인덱스 right 계산
    right = len(numbers) - left - 1

    # 위치 바꾸기
    numbers[right], numbers[left] = numbers[left], numbers[right]

print("뒤집어진 리스트: " + str(numbers))

