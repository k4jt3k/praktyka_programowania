class Figure():
    def __init__(self,color):
        self.color=color 

class Red():
    def name(self): return("czerwony")

class Blue():
    def name(self): return("niebieski")
    
class Circle(Figure):
    def draw(self):
        print (f"Kolor koła {self.color.name()}")

class Square(Figure):
    def draw(self):
        print (f"Kolor kwadratu {self.color.name()}") 

red = Red()
blue = Blue()

circle = Circle(red)
square = Square(blue)

circle.draw()
square.draw()