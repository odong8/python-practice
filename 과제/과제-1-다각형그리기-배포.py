#------------------------------------
# 과제-1-다각형그리기.py
#------------------------------------
import turtle
import random

t = turtle.Pen()
t.color('black')

# 함수: 다각형 그리기 함수 정의하기 
def _drawPolygon(n):      
        
    # 도형의 변의 길이 임의로 지정하기: 10 ~100사이의 값 사용 
    length = random.randint(10, 100)
    
    # 임의의 위치(x, y)로 이동하기: (x:-200~200, y:-200~200)
    t.up()  
    t.goto(random.randint(-200, 200),random.randint(-200, 200))
    t.down()

  
    # 임의의 색상 지정하기
    colors = ['violet','misty rose','green','light blue','yellow','pink','hotpink','limegreen', 'purple', 'orange']  # 색상 리스트
    t.color(random.choice(colors))        # 도형 그리기 색상 지정하기
    t.fillcolor(random.choice(colors))    # 도형 칠하기 색상 지정하기
    t.begin_fill()                        # 도형 칠하기 시작
    for _ in range(n):
        t.forward(length)
        t.left(360/n)                     # N각형 도형 그리기
    t.end_fill()                          # 도형 칠하기 종료
        
    
#--------------
# 시작
#--------------
# 화면 초기화
turtle.clear()  # 화면 지우기
t.up()          # 펜 올리기
t.goto(0,0)     # 커서 홈으로 이동하기(0, 0)

# 사용자로부터 숫자 입력 받기
# '몇각형 도형을 그릴까요?(3~10): '
n =  int(input('몇각형 도형을 그릴까?(3~10)'))

for _ in range(n):   # n번 반복하기    
    _drawPolygon(n)  # 다각형 그리기 함수 호출하기


# 화면을 마우스로 클릭하면 닫힌다.
turtle.exitonclick() 
 


