import turtle
t = turtle.Turtle()
t.pensize(5)
# t.up()
# t.goto(-30, 50)
# t.down()


def f(): # 한 변 그리기
    t.forward(100)
    t.right(90)
    
def h(): # 사각형 그리기
    for i in range(4):
        f()
        
def w(): # 창틀 그리기
    h()
    t.left(90)


for i in range(4):
    w()
turtle.exitonclick()