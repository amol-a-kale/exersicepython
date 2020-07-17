# Define a function that helps to calculate the area & perimeter of circle with any radius
# class circle:
#
#     def circle_area(radius):
#         PI = 3.14
#         circle_area = PI * radius * radius
#         print('The area of circle with radius {0} is {1}'.format(radius, circle_area))
#
#     def circle_perimeter(radius):
#         PI = 3.14
#         circle_perimeter = 2 * PI * radius
#         print('the perimeter of circle with radius {0} is {1}'.format(radius, circle_perimeter))
#
#
# cir = circle
# cir.circle_area(2)
# cir.circle_perimeter(2)

class circle:
    def __init__(self, radius):
        self.radius = radius
        PI = 3.14
        self.PI = PI

    def circle_area(self):
        circle_area = self.PI * self.radius * self.radius
        print('The area of circle with radius {0} is {1}'.format(self.radius, circle_area))

    def circle_perimeter(self):
        PI = 3.14
        circle_perimeter = 2 * self.PI * self.radius
        print('the perimeter of circle with radius {0} is {1}'.format(self.radius, circle_perimeter))


circle_measure = circle(4)
circle_measure.circle_area()
circle_measure.circle_perimeter()
