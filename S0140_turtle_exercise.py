"""
Opgave "Tom the Turtle":

Som altid skal du læse hele øpgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Funktionen "demo" introducerer dig til alle de kommandoer, du skal bruge for at interagere med Tom i de følgende øvelser.

Kun hvis du er nysgerrig og elsker detaljer:
    Her er den fulde dokumentation for turtle graphics:
    https://docs.python.org/3.3/library/turtle.html

Del 1:
    Skriv en funktion "square", som accepterer en parameter "length".
    Hvis denne funktion kaldes, får skildpadden til at tegne en firkant med en sidelængde på "længde" pixels.

Del 2:
     Færdiggør funktionen "visible", som skal returnere en boolsk værdi,
     der angiver, om skildpadden befinder sig i det synlige område af skærmen.
     Brug denne funktion i de følgende dele af denne øvelse
     til at få skildpadden tilbage til skærmen, når den er vandret væk.

Del 3:
    Skriv en funktion "many_squares" med en for-loop, som kalder square gentagne gange.
    Brug denne funktion til at tegne flere firkanter af forskellig størrelse i forskellige positioner.
    Funktionen skal have nogle parametre. F.eks:
        antal: hvor mange firkanter skal der tegnes?
        størrelse: hvor store er firkanterne?
        afstand: hvor langt væk fra den sidste firkant er den næste firkant placeret?

Del 4:
    Skriv en funktion, der producerer mønstre, der ligner dette:
    https://pixabay.com/vectors/spiral-square-pattern-black-white-154465/

Del 5:
    Skriv en funktion, der producerer mønstre svarende til dette:
    https://www.101computing.net/2d-shapes-using-python-turtle/star-polygons/
    Funktionen skal have en parameter, som påvirker mønsterets form.

Del 6:
    Opret din egen funktion, der producerer et sejt mønster.
    Senere, hvis du har lyst, kan du præsentere dit mønster på storskærmen for de andre.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""

import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.


def visible(turtle_name):  # returns true if both the x- and y-value of the turtle's position are between -480 and 480
    # you will need this: x-value: turtle_name.position()[0]
    # and this:           y-value: turtle_name.position()[1]
    if -380 <= turtle_name.position()[0] <= 380 and -380 <= turtle_name.position()[1] <= 380:
        return True
    else:
        print("False returning home")
        make_visible(turtle_name)


def make_visible(turtle_name):
    while True:
        if turtle_name.position()[0] > 380:
            turtle_name.left(180)
        elif turtle_name.position()[0] < -380:
            turtle_name.right(180)
        elif turtle_name.position()[1] > 380:
            turtle_name.left(180)
        elif turtle_name.position()[1] < -380:
            turtle_name.right(180)
        else:
            break
        turtle_name.home()


def demo():  # demonstration of basic turtle commands
    tom = turtle.Turtle()  # create an object named tom of type Turtle
    print(type(tom))
    tom.speed(1)  # fastest: 10, slowest: 1
    for x in range(8):  # do the following for x = 0, 1, 2, 3, 4, 5, 6, 7
        tom.forward(50)  # move 50 pixels
        tom.left(45)  # turn 45 degrees left
        print(f'Tom is now at {tom.position()}, x-value: {tom.position()[0]=:.2f}, y-value: {tom.position()[1]=:.2f}')
    tom.penup()  # do not draw while moving from now on
    tom.forward(100)
    tom.pendown()  # draw while moving from now on
    tom.pencolor("red")  # draw in red
    tom.right(90)  # turn 90 degrees right
    tom.forward(120)
    tom.right(-90)  # turning -90 degrees right is the same as turning +90 degrees left
    tom.forward(120)
    tom.home()  # return to the original position in the middle of the window
    turtle.done()  # keeps the turtle window open after the program is done


def square(length):  # laver en firkant
    for x in range(4):
        tom.forward(length)
        tom.left(90)
        print(visible(tom))
    # tom.forward(400)
    # print(visible(tom))


def many_squares(amount, size, distance):
    for i in range(amount):
        square(size)
        if i != amount - 1:
            tom.penup()
            tom.forward(size)
            tom.forward(distance)
            tom.pendown()


def spiral():
    tom.pencolor("blue")
    x = 3
    tom.speed(10)
    tom.right(90)
    tom.forward(x)
    for i in range(200):
        tom.left(90)
        x = x + 3
        if x % 2 != 0:
            tom.pencolor("yellow")
        else:
            tom.pencolor("blue")
        tom.forward(x)


def star_polygon(number):
    tom.speed(10)
    tom.pencolor("gold")
    if number == 1:
        tom.left(36)
        tom.forward(75)
        for i in range(4):
            tom.left(144)
            tom.forward(75)
    if number == 2:
        tom.left(54)
        tom.forward(75)
        for i in range(6):
            tom.left(154)
            tom.forward(75)
    if number == 3:
        tom.right(50)
        tom.forward(75)
        for i in range(10):
            tom.left(131)
            tom.forward(75)
    turtle.done()


def brand():
    tom.bgcolor("black")
    tom.speed(1)
    tom.pencolor("darkred")
    tom.width(10)
    tom.right(90)
    tom.forward(150)
    tom.right(135)
    tom.forward(105)
    tom.right(90)
    tom.forward(210)
    tom.left(90)
    tom.forward(50)
    tom.penup()
    tom.home()
    tom.pendown()
    tom.right(90)
    tom.forward(150)
    tom.left(135)
    tom.forward(105)
    tom.left(90)
    tom.forward(210)
    tom.right(90)
    tom.forward(50)
    tom.penup()
    tom.home()
    tom.pendown()
    tom.left(90)
    tom.forward(105)
    tom.width(7)
    tom.forward(25)
    tom.backward(25)
    tom.left(45)
    tom.forward(20)
    tom.backward(20)
    tom.right(90)
    tom.forward(20)
    turtle.done()


tom = turtle.Turtle()
tom.speed(1)
# many_squares(3, 100, 20)
brand()