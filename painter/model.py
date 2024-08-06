# TODO: Add code here

import matplotlib.pyplot as plt
import pickle


class Point:
    def _init_(self, x:float, y:float) -> None:
        self.x= x
        self.y= y
        

class Circle:
    def _init_(self, center:Point, radius:float) -> None:
        self.center= center
        self.radius= radius
        
def area(self)->float:
    return 3.1416 * (self.radius **2)

def draw(self) ->None:
    circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
    plt.gca().add_patch(circle)
    plt.axis("scaled")
    plt.show()
    
    
def __str__(self)->str:
    return f"Circle with center at ({self.center.x}, {self.center.y}) and radius {self.radius}"

    
    
        
                
        