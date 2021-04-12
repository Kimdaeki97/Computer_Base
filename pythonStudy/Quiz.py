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




