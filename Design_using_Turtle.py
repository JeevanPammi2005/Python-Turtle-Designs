import turtle, colorsys
scr=turtle.getscreen()
scr.colormode(255)
scr.bgcolor('black')
turtle.title("Desgins Using Turtle Module")
turtle.hideturtle()
turtle.speed(0)
writer=turtle.Turtle()
writer.hideturtle()
writer.color('white')
writer.penup()
writer.goto(0,-250)
writer.write('Press 1,2,3,4 or 5 for different designs', font=('Comic Sans', 25, 'italic'), align='center')

def reset():
    turtle.clear()
    writer.clear()
    turtle.penup()
    turtle.goto(0,0)
    turtle.setheading(0)
    turtle.pensize(1)
    turtle.pendown()

def Rainbow_flower_concentric_petals():
    reset()
    writer.write('Pls wait...', font=('Comic Sans',25,'italic'), align='center')
    turtle.pensize(2)
    for i in range(200):                #Rainbow flower concenteric 5 petal design
        rgb_temp = colorsys.hsv_to_rgb(i / 230, 1, 1)
        rgb = [round(x * 255) for x in rgb_temp]
        turtle.pencolor(tuple(rgb))
        turtle.circle(i, 80)
        turtle.left(120)
        turtle.circle(i, 80)
        turtle.right(60)

    writer.clear()
    writer.write('Press 1,2,3,4 or 5 for different designs', font=('Comic Sans',25,'italic'), align='center')

def Rainbow_Sprial_Circles():
    reset()
    writer.write('Pls wait...', font=('Comic Sans',25,'italic'), align='center')
    for i in range(180):            #Rainbow Sprial Circles
        rgb_temp = colorsys.hsv_to_rgb(i/180, 1, 1)
        rgb=[round(x*255) for x in rgb_temp]
        turtle.pencolor(tuple(rgb))
        turtle.circle(100)
        turtle.left(2)
    writer.clear()
    writer.write('Press 1,2,3,4 or 5 for different designs', font=('Comic Sans',25,'italic'), align='center')

def Rainbow_Concentric_Circles():
    reset()
    writer.write('Pls wait...', font=('Comic Sans',25,'italic'), align='center')
    turtle.pensize(2)
    for i in range(0,200,5):        #Rainbow Concentric Circles
        turtle.fd(5)
        turtle.left(90)
        turtle.pendown()
        rgb_temp = colorsys.hsv_to_rgb(i / 100, 1, 1)
        rgb=[round(x*255) for x in rgb_temp]
        turtle.pencolor(tuple(rgb))
        turtle.circle(i)
        turtle.penup()
        turtle.right(90)
    writer.clear()
    writer.write('Press 1,2,3,4 or 5 for different designs', font=('Comic Sans',25,'italic'), align='center')

def Rainbow_Hexagon():
    reset()
    writer.write('Pls wait...', font=('Comic Sans',25,'italic'), align='center')
    colours=['red','orange','yellow','green','blue','purple']  #Rainbow Hexagon
    turtle.speed(0)
    turtle.pensize(2)
    turtle.penup()
    turtle.goto(0,-25)
    turtle.pendown()
    for i in range(200):
        turtle.pencolor(colours[i % 6])
        turtle.fd(50 + i)
        turtle.left(59)
    writer.clear()
    writer.write('Press 1,2,3,4 or 5 for different designs', font=('Comic Sans',25,'italic'), align='center')


def Rainbow_flower_15petals():
    reset()
    writer.write('Pls wait...', font=('Comic Sans',25,'italic'), align='center')
    for i in range(15):             #Rainbow flower design with 15 petals
        turtle.right(90)
        for j in range(18):
            rgb_temp = colorsys.hsv_to_rgb((i*18) / 270, 1, 1)
            rgb=[round(x*255) for x in rgb_temp]
            turtle.pencolor(tuple(rgb))
            turtle.circle(5 * j + 50, 90)
            turtle.left(90)
            turtle.circle(5 * j + 50, 90)
            turtle.left(90)
        turtle.left(90)
        turtle.penup()
        turtle.circle(30, 24)
        turtle.pendown()
    writer.clear()
    writer.write('Press 1,2,3,4 or 5 for different designs', font=('Comic Sans',25,'italic'), align='center')


scr.onkey(Rainbow_flower_concentric_petals,'1')
scr.onkey(Rainbow_Sprial_Circles,'2')
scr.onkey(Rainbow_Concentric_Circles,'3')
scr.onkey(Rainbow_Hexagon,'4')
scr.onkey(Rainbow_flower_15petals,'5')
turtle.listen()

turtle.exitonclick()