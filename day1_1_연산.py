# a = 10
# b = 5
#print()문장에서 formatting방법
# print("%.2f + %.2f = %.2f" % (a, b, a + b)) #소숫점 두자리 실수 나타낼때.2f
# %d -> decimal 정수
# print("%d - %d = %d" % (a, b, a - b))
# print("%d * %d = %d" % (a, b, a * b))
# print("%d / %d = %d" % (a, b, a / b))
# print("%d // %d = %d" % (a, b, a // b))
# print("%d %% %d = %d" % (a, b, a % b))
# print("%d ** %d = %d" % (a, b, a ** b))


# f'' f스트링방법
# print( f' 덧셈 : {a} + {b} = {a+b}')
# print( f' 뺄셈 : {a} - {b} = {a-b}')


# ------------------------
# 숫자관련 함수 사용하기
# ------------------------

import math

# print(math.pi)

반지름 = 4
print(f'원의 둘레: {2 * math.pi * 반지름}')
# print(f'절대값: {abs(-10)}')
# print(f'반올림: {round(1.7777,2)}')
# print(f'올림: {math.ceil(1.7)}')
# print(f'내림: {math.floor(1.7)}')
# print(f'제곱승: {math.pow(2,10)}')
# print(f'제곱근: {math.sqrt(4)}')
# print(f'로그: {math.log(10)}')
# 반지름*반지름*원주율
print(4**2*3.14)
print(f'원의 넓이: {math.pow(반지름,2) * math.pi}')
print(f'반올림: {round(3.14*2/7)}')
print(f'원의 둘레: {2 * math.pi * 반지름}')



# print(f'문제1: {math.pi*(r**2)}')
# print(f'문제2: {round(3.14*2/7)}')
# print(f'문제3: {2*3.14*r}')