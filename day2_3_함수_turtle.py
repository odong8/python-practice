import turtle

# turtle.shape('turtle')
t = turtle.Pen()
t.pensize(5)
t.pencolor('pink')

# t.forward(100)
# t.left(225)
# t.forward(100)
# t.left(225)
# t.forward(100)
# t.left(225)
# t.forward(100)
# t.left(225)
# t.forward(100)
# t.left(225)
# t.forward(100)
# t.left(225)
# t.forward(100)
# t.left(225)
# t.forward(100)
# t.left(225)



# def draw():
#     t.forward(100)
#     t.left(225)
    
# draw()
# draw()
# draw()
# draw()
# draw()
# draw()
# draw()
# draw()

# 별그리기
# def draw_star(): #함수 정의하기
#     t.fd(100)
#     t.left(225)
   
# for i in range(8): #8번 반복하기
#     draw_star()     # 함수 호출하기
    

# # 원그리기
# t.color(0.6, 1, 0.4) # R, G, B  빛의 3요소
# t.begin_fill() # 색칠하기 시작
# t.circle(30) # 반지름이 30인 원 그리기
# t.end_fill() # 색칠하기 끝
# t.up()         # t.penup 펜 올리기
# t.fd(100)       # 앞으로 100만큼 이동
# t.down()        # t.pendown 펜 내리기
# t.color(1, 0.3, 1)
# t.begin_fill()
# t.circle(50)
# t.end_fill()
# t.up()
# t.fd(150)
# t.down()
# t.color(0, 1, 1)
# t.begin_fill()
# t.circle(70)
# t.end_fill()

# def f_circle(r,g,b,radius):
#     t.color(r,g,b)
#     t.begin_fill()
#     t.circle(radius)
#     t.end_fill()

# f_circle(0.6, 1, 0.4, 30)
# t.up()
# t.fd(100)
# t.down()
# f_circle(1, 0.3, 1, 50)
# t.up()
# t.fd(150)
# t.down()
# f_circle(0, 1, 1, 70)


# 원 그리기 함수
def f_circle(r, g, b, 원크기): 
    t.color(r, g, b) # R,G,B
    t.begin_fill()  # 색칠하기 시작
    t.circle(원크기) # 반지름이 '원크기'인 원 그리기
    t.end_fill()    # 색칠 종료
    
f_circle(0.6, 1, 0.4, 30)   # 원 그리기 함수 호출하기 
t.up()                      # t.penup 펜 올리기
t.forward(100)              # 앞으로 100만큼 이동
t.down()                    # t.penup 펜 내리기
f_circle(1, 0.3, 1, 50)    
t.up()
t.forward(150)
t.down()
f_circle(0, 1, 1, 70)  

turtle.exitonclick() 



# 이주희 선생님 버전_x좌표 -100부터 시작하게
# turtle.setx(-100)
# turtle.sety(0)
# t=turtle.Pen()

# t.pensize(10)
# t.color(0.6,1,0.4)
# turtle.position()
# (-100.00,0.00)
# turtle.heading()
# -100.0
# t.begin_fill()
# t.circle(30)
# t.end_fill()
# t.up()
# t.forward(100)
# t.down()
# t.color(1,0.3,1)
# t.begin_fill()
# t.circle(50)
# t.end_fill()
# t.up()
# t.forward(150)
# t.down()
# t.color(0,1,1)
# t.begin_fill()
# t.circle(70)
# t.end_fill()
# turtle.exitonclick()