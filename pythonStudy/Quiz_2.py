# 05.04
import random
ANSWER = random.randint(1, 20)
NUM_TRIES = 4

guess = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요.".format(NUM_TRIES)))


if tryy == ANSWER:
    print("축하합니다. {}번만에 숫자를 맞히셨습니다.".format(NUM_TRIES))
else:
    NUM_TRIES - 1
    print(tryy)
