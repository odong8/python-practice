#------------------
# 난수: random number
#------------------

# 난수 모듈 가져오기
import random

# # 임의의 정수 발생: 
# a = random.randint(10, 20) # 10~20 사이의 정수 발생 
# print(a)

# b = random.randrange(10, 20, 2) # start <= N < end
# print(b)


# # 임의의 실수 발생:
# c = random.random() # 0~1 사이의 임의의 실수 1개 발생
# print(c)

# d = random.uniform(10, 20) # start <= N <= end 1개 발생
# print(d)


# 문제:1~10 사이의 임의의 수 5개를 리스트로 만들어라.

b = list()
# b.append(random.randint(1,10))
# b.append(random.randint(1,10))
# b.append(random.randint(1,10))
# b.append(random.randint(1,10))
# b.append(random.randint(1,10))

for _ in range(5):
    b.append(random.randint(1,10))
    
print(b)

# 리스트(순서가 있는 데이터) 섞기 : 순서가 바뀐다.
x = [1, 3, 5, 4, 2]
print(f'섞기전:{x}')
random.shuffle(x)
print(f'섞은 후:{x}')

# 리스트에서 임의로 한 개 추출
a = random.choice(x)
print(a)
print(random.choice(x)) #Numpy라는 패키지에도 같은 기능

# 리스트에서 임의로 몇 개 추출
print(random.sample(x,2))


# 로또번호 추출
print('로또번호 추출: ',random.sample(range(1,46), 6))



# 실습문제1 : 난수값 더하기
import random
a = random.randint(1, 10)
b = random.randint(1, 10)

print(f'{a} + {b} = {a+b} 입니다.')