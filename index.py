import turtle

bob = turtle.Turtle()

# cria poligono
def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

print(polygon(bob, n=7, length=70))

turtle.mainloop()
