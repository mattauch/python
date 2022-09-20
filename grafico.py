import turtle

p=turtle.Pen()
p.speed(0)
turtle.bgcolor("black")

#        0       1         2       3
cores=["red", "yellow", "blue", "green"]
for x in range(600): 
    resto= x%4 #resto da divisão de x / 4 => 0, 1, 2, 3
    cor= cores[resto]
    p.pencolor(cor)
    p.forward(x * 2) #linas
    #p.circle(x * 5) #5 = pixels
    p.left(89) #left = grau
