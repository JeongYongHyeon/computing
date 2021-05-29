import turtle

t = turtle.Turtle()
t.shape("turtle")
radius = 50
for i in range(1,5):
    t.circle(radius)
    t.fd(30)
    radius += 30