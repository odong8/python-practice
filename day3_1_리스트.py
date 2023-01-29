#-------------------------
# 배열(리스트)
#-------------------------

# 리스트 정의하기
# a = []      # 빈 리스트 정의하기
# a = list()  # 빈 리스트 정의하기
# odd = [2, 4, 6, 8, 10]
# print(a, type(a))
# print(odd, type(odd))


# 리스트 인덱싱&슬라이싱
n = [80, 20, 70, 75]
print(n)
print(n[1])

# 리스트 요소의 값을 변경
n[1] = 40
n[3] = 'first'
print(n)

# 리스트의 요소를 연산하여 변경하기
n[0] = n[1] + n[2]
n[3] = n[1] * n[2]
print(n)

# 리스트 안에 리스트의 접근 방법_데이터 분석할 때 많이 사용
a = [1, 2, 3, ['a', 'b', 'c', [10,20,30,40], 'd']]
print(a[3])         # ['a', 'b', 'c']
print(a[3][1])      # b
print(a[3][1:])     # ['b', 'c']
print(a[3][3][1])   # 20

print('-' * 30)

# 리스트에서 사용하는 여러가지 함수
# 1. range() : 정수를 순차적으로 만들어주는 함수
range(5) # --> range(0, 5, 1) : 0부터 시작해서 5미만까지 1씩 증가해
         # 화면에 출력하려면 list 형태에 넣어 출력
         
a = list(range(5)) # 0~5미만까지의 정수
a = list(range(0, 5, 1)) # range(시작값, 종료값(미만), 증가분)
a = list(range(1, 11)) # 1~10까지
print(a)   # [0, 1, 2, 3, 4]

print('-' * 30)

# 퀴즈: [2,4,6,8,10]
a = list(range(2,11,2))
print(a)

print('-' * 30)

# 2. len() : 길이를 확인하는 함수
a = [3, 4, 40, 10]
print(len(a)) # a 리스트의 길이 출력

# 3. 리스트.append() : 리스트의 마지막에 요소를 추가하는 기능
a.append(10)
print(a)

# 4. 리스트.insert() : 리스트의 특정 위치에 추가하는 기능
a.insert(2, 100) #index 2번 자리에 100을 추가하세요.
print(a)

# 5. 리스트.remove(데이터) : 리스트의 요소 삭제(중복 값이 있을 경우 처음에 있는 데이터 삭제)
a.remove(10)
print(a)

# 6. 리스트.sort() : 정렬기능 (기본: 오름차순 정렬)
a.sort()
print(a)
# a.sort(reverse=True) #내림차순 정렬
# print(a)

# 7. 리스트.reverse() : 내림차순 정렬
a.reverse()
print(a)

b = [1,3,5,4,2]
b.reverse()
# a.sort(reverse=True)
print(b)



# 실습문제2: join함수(선생님 버전)
a = ['Life', 'is', 'good']
# print(a[0], a[1], a[2])

print(' '.join(a))


# join함수
a = ['Life', 'is', 'good']

res1 = " ".join(a)
print(res1)

# 실습문제 3: 리스트에서 중복 제거 - 집합 함수(set()) 사용
a = [1,1,1,2,2,3,3,3,4,4,5]
print(list(set(a)))
