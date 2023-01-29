# -----------------
# 변수 활용
# -----------------


# name, age = '석진 남준 지민 정국', 29

# print(f'내 이름은 {name[:2]}이고 나이는 {age}세 입니다.')
# print(f'내 첫째 동생 이름은 {name[3:5]}이고, 나이는 {age - 2}세 입니다.')
# print(f'내 둘째 동생 이름은 {name[6:8]}이고, 나이는 {age - 3}세 입니다.')
# print(f'내 셋째 동생 이름은 {name[9:]}이고, 나이는 {age - 5}세 입니다.')



# name = '석진 남준 지민 정국'
# age = 29
# print(f'내 이름은 {name[:2]}이고 나이는 {age}세 입니다.')
# age -= 2  # age = age -2
# print(f'내 첫째 동생 이름은 {name[3:5]}이고, 나이는 {age}세 입니다.')
# age -= 1  # age = age -1
# print(f'내 둘째 동생 이름은 {name[6:8]}이고, 나이는 {age}세 입니다.')
# age -= 2  # age = age -2
# print(f'내 셋째 동생 이름은 {name[9:]}이고, 나이는 {age}세 입니다.')



# 문제1. 세금 및 팁 적용하여 음식 계산하기
# meal = 4450        # 1. 음식가격
# tax = 6.75 / 100   # 2.세금
# tip = 15 / 100     # 3. 팁

# meal = meal * tax + meal   # 4. 세금이 포함된 음식 가격
# total = meal * tip + meal  # 5. 팁이 포함된 토탈 가격
# print(f'음식 가격(세금포함): {round(meal)}')
# print(f'계산할 금액은 총 {round(total)}원입니다.')


# 문제2. 급여 계산
# '''
# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25
# '''
# hours = 35
# rate = 2.75
# pay = hours * rate
# print(f'pay = {pay}')



# hours = int(input('근로시간: '))
# rate = float(input('시간당 임금: '))
# pay = hours * rate
# print(f'pay = {pay}')



# 문제3. 섭씨온도 vs 화씨온도
# c_temp = input()
# print(c_temp, type(c_temp))


# c_temp = input()     # 키보드로부터 입력을 받는 함수: input()
# c_temp = int(c_temp)    # 정수로 변환: int()
# print(c_temp, type(c_temp))

# c_temp = int(input('섭씨온도를 입력하세요:'))
# f_temp = (9/5) * c_temp + 32
# print(f'섭씨온도: {c_temp}는 화씨온도로: {f_temp}이다.')




# 강사님의 동전교환기 만들기
# money = 4321
print('---동전교환기 프로그램을 작동합니다.---')
# print(f'금액을 입력하세요: {money}')
money = int(input("금액을 입력하세요:"))
print('동전으로 교환하겠습니다.---------')

print(f'500원짜리 동전: {money//500} 개')
# money = money % 500
money %= 500
print(f'100원짜리 동전: {money//100} 개')
money = money % 100
print(f'50원짜리 동전: {money//50} 개')
money = money % 50
print(f'10원짜리 동전: {money//10} 개')
money = money % 10
print(f'잔돈:  {money} 원')


# 동전 개수 계산
# money = 4321

# 오백원 = money // 500
# money = money % 500

# 백원 = money // 100
# money = money % 100

# 오십원 = money // 50
# money = money % 50

# 십원 = money // 10
# money = money % 10

# 잔돈 = money // 1
# money = money % 1

# print(f'500원짜리 동전: {오백원}개')
# print(f'100원짜리 동전: {백원}개')
# print(f' 50원짜리 동전: {오십원}개')
# print(f' 10원짜리 동전: {십원}개')
# print(f'\t  잔돈: {잔돈}원 입니다.')