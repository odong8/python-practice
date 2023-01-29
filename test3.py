# d1 = 123
# d2 = '123'
# d3 = [123]
# d4 = (123,)
# d5 = {'key' : 123}
# d6 = {123}
# d7 = True

# print(f'{d1}의 자료형: {type(d1)}')
# print(f'{d2}의 자료형: {type(d2)}')
# print(f'{d3}의 자료형: {type(d3)}')
# print(f'{d4}의 자료형: {type(d4)}')
# print(f'{d5}의 자료형: {type(d5)}')
# print(f'{d6}의 자료형: {type(d6)}')
# print(f'{d7}의 자료형: {type(d7)}')

# a = "사랑해요, 파이썬!"

# print(a[0],a[1],a[2])
# print(a[:6])

# a = '우리는 민족중흥의 역사적 사명을 띄고 이 땅에 태어났다.'
# print(a[3:12])



# name = '석진 남준 지민 정국'
# age = 29

# 문자열을 배열로 변경하는 방법
# name = name.split(" ")
# print(name)
# print(name[0])

# print(f'내 이름은 {name[:2]}이고 나이는 {age}세입니다.\n내 첫째 동생 이름은 {name[3:5]}이고 나이는 {age - 2}세입니다. \n내 둘째 동생 이름은 {name[6:8]}이고 나이는 {age - 3}세입니다. \n내 셋째 동생 이름은 {name[9:]}이고 나이는 {age - 5}세입니다.')


# name = ['석진','남준','지민','정국']
# age = 29

# print(f'내 이름은 {name[0]}이고 \n내 첫째 동생 이름은 {name[1]}')


# 세금 및 팁 적용하여 음식 계산하기
# meal = 4450
# tax = 6.75 / 100
# tip = 15 / 100

# meal = meal * tax + meal
# total = meal * tip + meal

# print(f'계산할 금액은 총 {round(total)}원입니다.')

# 급여 계산
# hours = 35
# rate = 2.75

# print(f'pay = {hours * rate}')


# 동전 개수 계산
# total = 4321

# 오백원 = total // 500
# total %= 500

# 백원 = total // 100
# total %= 100

# 오십원 = total // 50
# total %= 50

# 십원 = total // 10
# total %= 10

# 잔돈 = total // 1
# total %= 1


# print(f'500원짜리 동전: {오백원}개')
# print(f'100원짜리 동전: {백원}개')
# print(f' 50원짜리 동전: {오십원}개')
# print(f' 10원짜리 동전: {십원}개')
# print(f'\t잔돈: {잔돈}원 입니다.')

# # 더하기 함수 정의
# def add(a,b):
#     return a+b
# print(add(1,2))

# # 곱하기 함수 정의
# def multi(a,b):
#     return a * b
# print(multi(3,5))

# 짝수홀수1
# def is_odd(a):
#     if a % 2 == 0:
#         print(f'짝수입니다.')
#     else:
#         print(f'홀수입니다.')
# is_odd(30)


# 짝수홀수2
# a = 7

# def is_odd(a):
#     return a % 2

# if is_odd(a) == 0:
#     print("짝수")
    
# if is_odd(a) != 0:
#     print("홀수")
    
    
