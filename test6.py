# score = int(input("숫자입력: "))


# if score >= 60:
#     message = "success"
# else:
#     message = "failure"
    
    
# message = "success" if score >= 60 else "failure"

# print(message)


# 난수값 더하기
# import random
# a = random.randint(1, 10)
# b = random.randint(1, 10)

# print(f'{a} + {b} = {a+b} 입니다.')


# 1 ~ 100까지 숫자 출력

# 방법1
# a =  list(range(101))
# print(a)


# 방법2
# for a in range(1,10):
#     print(a)

# 방법3
# a = 1
# while a <= 10:
#     print(a)
#     a += 1

# 방법4
# a = 0
# s = []
# while a < 100:
#     a += 1
#     s.append(a)
# print(s)


treeHit = 0

# while treeHit < 10:
#     treeHit += 1  
#     print(f'나무를 {treeHit}번 찍었습니다.')
  
#     if treeHit == 10:
#         print(f'나무 넘어갑니다.')
        
for treeHit in range(1, 11):
    print(f'나무를 {treeHit}번 찍었습니다.')
    
    if treeHit == 10:
        print(f'나무 넘어갑니다.')