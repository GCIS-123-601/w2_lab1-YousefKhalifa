import turtle

def test_drive():
    turtle.forward(100)
    turtle.left(87)
    turtle.setheading(127)
    turtle.up()
    turtle.goto(50,50)
    turtle.down()
    turtle.home()
    turtle.circle(50)
test_drive()

def turtle_state():
    v2=turtle.isdown()
    v3=turtle.heading()
    vx=turtle.xcor()
    vy=turtle.ycor()
    print("turtle is down? " , v2)
    print("current angle: " ,v3)
    print("xor: ", vx, "ycor: ", vy)
    def main():
        turtle_state()
        test_drive()
        input("press enter to continue..")
        turtle_state()
    main()