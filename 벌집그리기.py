import turtle
t = turtle.Turtle()
t.pensize(5)
t.up()
t.goto(-30, 50)
t.down()

def f(): # 한 변 그리기
    t.forward(100)
    t.left(60)
    
def h(): # 육각형 그리기
    for i in range(6):
    # f(), f(), f(), f(), f(), f()
        f()
        
def g(): # 벌집 그리기
    h()
    t.forward(100)
    t.right(60)
    
    
for i in range(6):
    g()
turtle.exitonclick()
