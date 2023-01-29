


import turtle

t = turtle.Pen()
t.pensize(5)
t.up()
t.goto(-30,50)
t.down()

# for i in range(6):
#     for i in range(6):
#         t.forward(50)
#         t.left(60)
#     t.forward(50)    
#     t.right(60)

# def line():  # 선 그리기
#     t.forward(50)
#     t.right(60)
    
# def line_6(): # 육각형 그리기
#     line()
#     line()
#     line()
#     line()
#     line()
#     line()

# def fig_6(): # 도형 6개 그리기
#     line_6()
#     t.forward(50)
#     t.left(60)
    
# for i in range(6):
#     fig_6()
        



def line(): # 한 변 그리기
    t.forward(100)
    t.right(72)
   

def line_5(): # 오각형 그리기
    for i in range(5):
        line()
        
def line_f(): # 오각형 꽃 그리기
    line_5()
    t.left(72)
    
for i in range(5):
    line_f()

turtle.exitonclick()