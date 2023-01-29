import turtle, random

t = turtle.Turtle()
t.pensize(5)
t.pensize(random.randint(1,3))
t.pensize(10)


def line(): # 한 변 그리기
    t.forward(100)
    t.right(72)

   

def line_5(): # 오각형 그리기
    r = random.random()
    g = random.random()
    b = random.random()
    t.color(r,g,b)
    for i in range(5):
        line()
        
def line_f(): # 오각형 꽃 그리기
    line_5()
    t.left(72)
    
for i in range(5):
    line_f()
    
turtle.exitonclick()



# t.pensize(10)


# def line(): # 한 변 그리기
#     t.forward(100)
#     t.right(72)

   

# def line_5(): # 오각형 그리기
#     for i in range(5):
#         line()
        
# def line_f(): # 오각형 꽃 그리기
#     line_5()
#     t.left(72)
    
# for i in range(5):
#     line_f()