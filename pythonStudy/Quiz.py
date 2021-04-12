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
