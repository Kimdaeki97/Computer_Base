# 04.12

INTEREST_RATE = 0.12
ARPARRTMENT_PRICE = 1100000000

year = 1988
bank_balance = 50000000

while year < 2016:
    bank_balance = bank_balance * (1 + INTEREST_RATE)
    year += 1

print(bank_balance)

if bank_balance > ARPARRTMENT_PRICE:
    print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(int(bank_balance - ARPARRTMENT_PRICE)))
else:
    print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(int(ARPARRTMENT_PRICE - bank_balance)))

print("-------------------------------")

i = 1
previous = 0
current = 1

while i <= 50:
    print(current)

    # # 1번 방법
    # temp = previous # previous를 임시 저장소인 temp에 저장
    # previous = current
    # current = current + temp # temp에는 기존 previous 값이 저장되어있음

    # 2번 방법
    previous, current = current, current + previous

    i += 1

print("-------------------------------")

# 구구단 (중첩 while 문)
dan = 1
while dan <= 9:
    hang = 1
    while hang <= 9:
        print("{} * {} = {}".format(dan, hang, dan * hang))
        hang += 1
    dan += 1

print("-------------------------------")
# 04.14
# 리스트 원소를 모두 출력하기
greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]

i = 0
while i <= len(greetings):
    print(greetings[i])
    i += 1

print("-------------------------------")
# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(F):
    C = ((F - 32)*5) / 9
    return C

temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드를 입력하세요.
print("섭씨 온도 리스트: " + str(temperature_list))  # 섭씨 온도 출력








