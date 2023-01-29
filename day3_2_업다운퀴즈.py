# 업&다운 퀴즈 맞추기 프로그램
import random

a = random.randint(1, 50)   # 1~50 사이의 임의의 정수

print('업&다운 퀴즈 시작~!')
print('-' * 50)
print('1~50 중 한개의 비밀의 수가 정해졌습니다.')

trycnt = 0

while True:     # 무한반복
    guess = int(input('당신이 생각하는 비밀의 수는?: '))
    trycnt = trycnt + 1     # trycnt += 1
    if guess == a:
        print('정답입니다.')
        break
    # 방법1
    elif guess > a:     # 그렇지 않고 만약에
        print('작아')
    elif guess < a:
        print('커')
   
        
print(f'비밀의 숫자는 {a}입니다.')
print(f'당신이 시도한 횟수는 {trycnt}입니다.')


# 방법2
# else:     # 그렇지 않다면
#     if guess > a:
#         print('작아')
#     elif guess < a:
#         print('커')


# 방법3
#  elif guess < a:
#         print('비밀의 수보다 더 커요..')
        
#     else:
#         print('비밀의 수보다 더 작아요..')