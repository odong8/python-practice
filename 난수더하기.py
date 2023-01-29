import random

a = random.randint(1, 50)
c_num = 0

print(f'1~50까지의 숫자 중에 비밀의 숫자가 지정되었습니다.')
print(f'게임을 시작합니다!')

while True:
    f_num = int(input("당신이 생각하는 숫자를 입력하세요."))
    c_num = c_num + 1
    if f_num == a:
        print('정답입니다!')
        break
        
    elif f_num > a:
        print('비밀의 수는 더 작은 수입니다.')
        
    else:
        print('비밀의 수는 더 큰 수 입니다.')
        
print(f'{"-" * 50}')
print(f'비밀의 숫자: {a}')
print(f'당신의 입력 횟수: {c_num}')