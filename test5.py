# n1 = [1,2,3,4]
# a = [3,4,'toy', 3.14]
# score = [90, 89, 77, 95, 67]
# fruit =['apple', 'banana', 'orange']

# print(a[0])
# print(a[::-1])
# print(a[0:2])

# n = [80, 20, 70, 75]
# # print(n)
# # print(n[1])
# n[1] = 40
# n[3] = 'first'
# # print(n)
# n[0] = n[1] + n[2]
# n[3] = n[1] * n[2]
# print(n)

# a = [1, 2, 3, 4, 5]
# b = "12345"
# print(a[0:2])
# print(b[0:2])

# 내림차순 내장함수
# a = [1, 3, 5, 4, 2]
# b = sorted(a)
# # print(a)

# print(f"{a} -> 역순 출력 -> {b}")

# join함수
# a = ['Life', 'is', 'good']

# res1 = ".".join(a)
# print(res1)

# a = [1,1,1,2,2,3,3,3,4,4,5]

# # 리스트 중복제거 set(리스트)함수
# result1 = list(set(a))
# # result2 = sorted(result1)
# # print(result2)
# print(f'{a} -> 중복제거 -> {result1}')


# 난수값 더하기
import random
# a = random.randint(1, 10)
# b = random.randint(1, 10)

# print(f'{a} + {b} = {a+b} 입니다.')

# 난수 퀴즈
# a = random.randint(1,50)
# c_num = 0

# while True:
#     f_num = int(input('너가 생각하는 숫자를 입력해봐:'))
#     c_num = c_num + 1
#     if f_num  == a:
#         print('정답이야!')
#         break
        
#     elif f_num > a:
#         print('비밀의 수는 더 작은 수야')
        
        
#     else:
#         print('비밀의 수는 더 큰 수야.')
    
# print(f'비밀의 숫자: {a}')
# print(f'당신의 입력 횟수: {c_num}회')


# x = 10
# if x % 2 == 0:
#     print(f'입력된 수: {x} ==> 짝수')
# else:
#     print(f'입력된 수: {x} ==> 홀수')


# age = int(input('나이 : '))

# if age > 7:
#     if age <= 13:
#         print('초등학생입니다.')
#     else:
#         if age <= 16:
#             print('중학생입니다.')
#         else:
#             if age <= 19:
#                 print('고등학생입니다.')
#             else:
#                 print('일반성인 혹은 대학생입니다.')
# else:
#     print('미취학 아동입니다.')


# if score >= 60
#     message = "success"
# else:
#     message = "failure"
    
    
# message = "success" if score >= 60 else "failure"

print(f'{"-" * 50}')
print('''상황 : 어느날 다음과 같은 문자가 왔다. 
      \'친구 나아파가 크게 다쳐서 현재 아파병원 응급실에서
      치료를 받고 있습니다.\' 문자를 확인하고 당신은 어떤
      반응을 보일 것인가?
      ''')

ans_num = int(input('''
반응 ① 진짜 치료 중인지 확인부터 해야겠어.
     ② 빨리 다른 친구들에게 알려야겠다.
     ③ 아마 큰일은 아닐거야. 괜찮겠지.
'''))

if ans_num == 1:
    message = "당신은 배려심 많고 섬세한 사람이군요.낯가림이 다소 있어 처음에는 말수가 적지만, 친해지면 말도 많고 유머러스한 성격입니다."
elif ans_num == 2:
    message = "당신은 남들의 말은 크게 신경 안 쓰는 마이웨이 타입이에요! 처음 보는 사람이나 자주 보는 사람이나 한결같이 잘 챙겨주는 성격입니다."
else:
    message = "당신은 밝고 자유분방한 성격이군요. 대체로 자신감이 강하고, 행동과 말이 자유롭기 때문에 자유로운 영혼처럼 보일 수 있어요!"
    
print(message)