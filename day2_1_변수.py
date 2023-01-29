# d1 = 123
# d2 = '123'
# d3 = [123]
# d4 = (123,)
# d5 = {'key' :123}
# d6 = {123}
# d7 = True

# # type()함수 : 변수의 자료형 확인할 때
# print(f'{d1}의 자료형: {type(d1)}')
# print(f'{d2}의 자료형: {type(d2)}')
# print(f'{d3}의 자료형: {type(d3)}')
# print(f'{d4}의 자료형: {type(d4)}')
# print(f'{d5}의 자료형: {type(d5)}')
# print(f'{d6}의 자료형: {type(d6)}')
# print(f'{d7}의 자료형: {type(d7)}')



# 인덱스 & 슬라이싱
# s = "hello world"
# print(s[4])

# # [시작인덱스:끝인덱스] 시작값 <= s < 끝값
# print(s[0:5]) # ----> s[0:5:1] 한칸씩 이동
# print(s[0:5:2]) # ----> 2칸씩 이동
# # print(s[6:]) # 공백으로 둔 자리는 전체를 의미
# # print(s[:4])
# # print(s[:]) # 처음부터 끝까지
# print(s[::])
# print(s[: :-1]) # 거꾸로 출력하기


# 문장에 변수 사용하여 대체할 때
# name = '김변수'
# print(f'안녕하세요. {name}님')
# print(f'{name}님이 방문하신 것을 환영합니다.')
# print(f'{name}님 즐거운 시간 되세요.')

# 대입연산자
# a = 100
# a += 3 # a = a + 3
# print(a)


# # 변수를 만드는 방법
# a = 'python'
# b = 'fun'
# a, b = ('python', 'fun') # 튜플 형태
# [a, b] = ['python', 'fun']
# a = b = 'python'

# # 변수 교차
# a = 5
# b = 3
# print(a,b)

# a, b = b, a
# print(a,b)


gift_cash = 1000
student_count = 10
teacher_count = 10
result = (( gift_cash * student_count ) / teacher_count )
print(result)



# 섭씨온도 화씨온도
