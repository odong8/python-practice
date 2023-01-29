# --------------------
# 문자열
# --------------------


# 문자열 지정 방법
# - 따옴표를 사용한다.
# print('Hello')
# print("Hello")
# print("Hello 'world")
# print('Hello "world')

# print("\"No, I'm not\"")
# print('"Yes, I can"')
# print("'Yes, I can'")

# 문자열에서 + 연산자 사용 : 붙여쓰기
print('Hello'+'world')
print('Hello','world')
print('Hello','world','!')
a = "Python"
b = " is very fun!"
print(a+b)
# 문자열 연산함수 : evel() - 문자열을 숫자처럼 계산해주는 함수
print(eval('a+b'))


# 문자열에서 * 연산자 사용 : 반복
print('Hello'*3)
print('-' * 30)

# 문자열의 인덱싱(indexing)
print("Hello"[0])
print("Hello"[1])
print("Hello"[-4])

# 문자열의 슬라이싱(slicing)
print('Hello'[2:4])

# 이스케이프 문자(Escape Character)
print('Hello\t\t\tworld')

# 데이터타입 확인 함수 : type()
print( type(10+5))
print( type('10'+'5'))

# 서로 다른 타입의 연산은 오류 발생
# print(10 + "5")


print('문제1: ',"Mary\'s cosmetics")
print('문제2: ','박씨가 소리질렀다."도둑이야".')

print('문제3: ','C:\\Windows')
print('문제4: ')
print("안녕하세요.\n오늘날씨가\t\t좋습니다.")
print() # == \n
print()
print('-' * 50)

# 따옴표 세개 사용 - 여러줄의 문장을 쓸 때
a = '''박씨가 소리를 질렀다.
도둑이야!'''

# 따옴표 세개 사용 - 여러줄의 문장을 쓸 때
a = '''OOO카페 메뉴판
- 아메리카노:     3000원
- 카페라떼:       5000원
- 카라멜마키아또 : 6000원
'''
print(a)