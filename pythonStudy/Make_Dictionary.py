# 05.07
with open("vocabulary.txt", "w") as f:
    while True: # While True는 무한반복. break문이 나올때까지 돈다.
        ENGLISH_WORD = input("영어 단어를 입력하세요: ")
        if ENGLISH_WORD == 'q':
            break

        KOREAN_WORD = input("한국어 뜻을 입력하세요: ")
        if KOREAN_WORD ==\
                'q':
            break

        f.write("{}: {}\n".format(ENGLISH_WORD, KOREAN_WORD))