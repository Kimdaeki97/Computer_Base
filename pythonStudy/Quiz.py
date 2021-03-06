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

print("-------------------------------")

# 04.21
# 딕셔너리
# 1. 단어장 만들기
vocab = {
    "sanitizer": "살균제",
    "ambition": "야망",
    "conscience": "양심",
    "civilization": "문명"
}
print(vocab)

# 2. 새로운 단어들 추가
vocab["privilege"] = "특권"
vocab["principle"] = "원칙"
print(vocab)

print("-------------------------------")

# 언어 사전의 단어와 뜻을 서로 바꿔주는 함수
def reverse_dict(dict):
    new_dict = {}  # 새로운 사전

    # dict의 key와 value를 뒤집어서 new_dict에 저장
    for key, value in dict.items():
        new_dict[value] = key

    return new_dict  # 변환한 새로운 사전 리턴

# 영-한 단어장
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
}

# 기존 단어장 출력
print("영-한 단어장\n{}\n".format(vocab))

# 변환된 단어장 출력
reversed_vocab = reverse_dict(vocab)
print("한-영 단어장\n{}".format(reversed_vocab))

print("-------------------------------")

# 투표 결과 리스트
votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', \
'최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', \
'강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']

# 후보별 득표수 사전
vote_counter = {}

# 리스트 votes를 이용해서 사전 vote_counter를 정리하기
for name in votes:
    # 코드를 작성하세요.
    if name not in vote_counter:
        vote_counter[name] = 1
    else:
        vote_counter[name] += 1

# 후보별 득표수 출력
print(vote_counter)

print("-------------------------------")

# 04.26
# 파이썬 데이터의 비밀 Aliasing
x = [2, 3, 5, 7, 11]
y = x  # 변수 y는 x의 가명(alias)
y[2] = 4
print(x)
print(y)
# x, y 결과 값은 같게 나옴

print("-------------------------------")

# y 결과 값이 바뀌게 하려면?
x = [2, 3, 5, 7, 11]
y = list(x)  # y는 x 리스트의 복사본을 가리킴
y[2] = 4
print(x)
print(y)

print("-------------------------------")

# 04.27
# 자리수 합 리턴
def sum_digit(num):
    total = 0
    str_num = str(num)

    for i in str_num:
        total += int(i)
    return total

# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
sum = 0
for num in range(0,1001):
    sum = sum + sum_digit(num)

print(sum)

print("-------------------------------")

def mask_security_number(security_number):
    # 코드를 입력하세요.
    return security_number[0:-4] + str('****')

# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))

print("-------------------------------")

# 04.28
def is_palindrome(word):
    for left in range(len(word) // 2):
        # 한 쌍이라도 일치하지 않으면 바로 False를 리턴하고 함수를 끝낸다.
        right = len(word) - 1 - left
        if word[right] != word[left]:
            return False
    # for문에서 나왔다면 모든 쌍이 일치
    return True


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))

# 05.03











