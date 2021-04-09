x = 2 # 글로벌 변수

def my_function():
    x = 3  # 로컬 변수
    print(x)

my_function()
print(x)

# 상수는 일반 변수와 구분 짓기 위해 대문자로 표기한다.
# 실수를 방지하기 위해서이기도 함
# 상수는 절대 바꾸지 않겠다는 의지(?)를 표현

PI = 3 # 상수
def calculate_area(r):
    return PI * r * r