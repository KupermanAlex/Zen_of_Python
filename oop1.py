# """Створити батьківський клас Figure з методами __init__: ініціалізується колір, 
#                                                                                          get_color: повертає колір фігури,
#                                                                                           info: надає інформацію про фігуру та колір,  
# від якого наслідуються такі класи як Rectangle, Square, які мають інформацію про ширину, висоту фігури, метод square, який знаходить площу фігури."""
# class Figure ():
#     def __init__(self, color):
#        self.color = color
        
#     def get_color(self):
#         return self.color

#     def info (self):
#         print ("Enter color: ", self.color)
# Circle = Figure("red")
# Circle.info()


# class Polygon:
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]

#     def inputSides(self):
#         self.sides = [float(input("Enter side" + str(i+1)+" : ")) for i in range(self.n)]

#     def dispSides(self):
#         for i in range(self.n):
#             print("Side",i+1,"is",self.sides[i])
# class Square(Polygon):
#     def __init__(self,):
#         Polygon.__init__(self, 1)

#     def findArea(self) :
#         a = self.sides
#         area = a * a
#         print  ("The area of the square is:", area )
        ##################################################################
# class Figure:
#     def __init__(self, color):
#         self.color = color
      
#     def get_color(self):
#         return self.color

#     def info(self):
#         print("Figure")
#         print("Color: " + self.color)

# class Rectangle(Figure):
#     def __init__(self, color, width=100, height=100):
#         super().__init__(color)
#         self.width = width
#         self.height = height

#     def square(self):
#         return self.width * self.height

#     def info(self):
#         print("Rectangle")
#         print("Color: " + self.color)
#         print("Width: " + str(self.width))
#         print("Height: " + str(self.height))
#         print("Square: " + str(self.square()))

# fig1 = Figure("green")
# fig1.info()
# fig2=Rectangle("red",10,20)
# fig2.info()







