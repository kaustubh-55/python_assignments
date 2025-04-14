class Shape :
    def __init__(self,side1,side2):
        self.side1 = side1 
        self.side2 = side2
        self.multiply = side1*side2

    def area_of_square(self):
        s_area = self.multiply
        print("Area of square is : ", s_area)

    def area_of_rectangle(self):       
        r_area = self.multiply
        print("Area of rectangle is : ", r_area)

    def area_of_circle(self):
        c_area = 3.14 * (self.multiply)
        print("Area of circle is : " ,c_area)

square = Shape(10 , 10)
rectangle = Shape(20,30)
circle = Shape(20,20)

square.area_of_square()
rectangle.area_of_rectangle()
circle.area_of_circle()

        