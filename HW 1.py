def g(tom, jer, r):
    if tom > jer:
        fg = r / (tom - jer)
        print("Том догонит Джерри за", fg, "секунд")
    elif tom < jer:
       print("Тому Джерри не поймать")
print("Впишите скорость Тома")
tom = int(input())
print("Впишите скорость Джерри")
jer = int(input())
print("Впишите расстояние между ними")
r = int(input())
print(g(tom, jer, r))