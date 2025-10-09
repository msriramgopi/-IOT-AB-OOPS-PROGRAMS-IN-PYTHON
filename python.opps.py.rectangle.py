# area & perimeter of the rectangle by python(oops)
import math
class rectangle:
    def __init__(self,ram,gopi):
        
      self.ram=ram
      self.gopi=gopi
      
    def area(self):
        
        return ram*gopi
    def peri(self):
       return 2*(gopi*ram)
    
    
#driver code   
ram=float(input("Enter the length: "))

gopi=float(input("Enter the width: "))

sri=rectangle(ram,gopi)

area=sri.area()

print("area of the rectangle is:",area)

peri=sri.peri()

print("perimeter of the rectangle is:",peri)





      

