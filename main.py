truck = Actor('truck')
truck.pos = 100, 56

WIDTH = 500
HEIGHT = truck.height + 20

def draw():
    screen.clear()
    truck.draw()