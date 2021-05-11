# 05.07
with open("vocabulary.txt", "w") as f:
    while True: # While True는 무한반복. break문이 나올때까지 돈다.
        ENGLISH_WORD = input("영어 단어를 입력하세요: ")
        if ENGLISH_WORD == 'q':
            break

        KOREAN_WORD = input("한국어 뜻을 입력하세요: ")
        if KOREAN_WORD == 'q':
            break

        f.write("{}: {}\n".format(ENGLISH_WORD, KOREAN_WORD))

# 05.11
import random

# 사전 만들기
vocab = {}
with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, koren_word = data[0], data[1]
        vocab[english_word] = koren_word

# 목록 가져오기
keys = list(vocab.keys())

# 문제 내기
while True:
    # 랜덤한 문제 받아오기
    index = random.randint(0, len(keys) - 1)
    english_word = keys[index]
    koren_word = vocab[english_word]

    # 유저 입력값 받기
    guess = input("{}: ".format(koren_word))

    if guess == 'q':
        break

    if guess == english_word:
        print("정답입니다!\n")
    else:
        print("아쉽습니다. 정답은 {}입니다\n".format(english_word))
