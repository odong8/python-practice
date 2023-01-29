# -------------------
# 함수
# -------------------


# 문제1. 곱하기 함수 만들기

# 함수 정의하기
# def 곱하기(a, b):
#     # result = a * b
#     # return result
#     return a * b

# 함수 호출하기
# print(곱하기(10, 5))




# 짝수홀수1
# def is_odd(a):
#     if a % 2 == 0:
#         print(f'짝수입니다.')
#     else:
#         print(f'홀수입니다.')
# is_odd(30)


# 짝수홀수2
# a = int(input("판별할 숫자를 입력하세요."))

# def is_odd(a):
#     return a % 2

# if is_odd(a) == 0:
#     print("짝수")
    
# if is_odd(a) != 0:
#     print("홀수")
    
    
#문제2: 짝수, 홀수 판별함수(강사님버전)
# def is_odd(a):
#     if a % 2 == 0: 
#         return '짝수'
#     else:
#         return '홀수'
    
# a = 18988
# print( is_odd(a) )


input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print(f"두 수의 합은 {total}입니다.")
# print("두 수의 합은 %s 입니다" % total)
# print("두 수(%d, %d)의 합은 %s 입니다" % (input1, input2, total))


a = 20
b = 30
# print(a + b)

def 곱하기():
    global c
    c=a*b
    print(c)

def 더하기():
    print(c+a)
    
곱하기()
더하기()
    