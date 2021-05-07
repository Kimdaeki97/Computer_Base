# 05.04
import random
ANSWER = random.randint(1, 20)
NUM_TRIES = 4

guess = -1
tries = 0
"""
게임이 계속되어야하는 조건 두가지
1. 아직 사용자가 정답을 맞히지 못했다. = guess != ANSWER
2. 아직 사용자에게 기회가 남았다. = tries가 4가 되지 않았다.
"""
while guess != ANSWER and tries < NUM_TRIES:
    guess = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요.".format(NUM_TRIES - tries)))
    print(guess)
    tries += 1

    if guess < ANSWER:
        print("UP")
    elif guess > ANSWER:
        print("DOWN")

if guess == ANSWER:
    print("축하합니다 {}번 만에 숫자를 맞히셨습니다.".format(tries))
else:
    print("아쉽습니다. 정답은 {}였습니다.".format(ANSWER))

print("-------------------------------")

# 05.06
'''
with open("data/chicken.txt", "r") as f:
    total_revenue = 0
    total_days = 0

    for line in f:
        data = line.strip().split(": ")
        revenue = int(data[1])
        
        total_revenue += revenue
        total_days += 1
        
    print(total_revenue / total_days)
'''