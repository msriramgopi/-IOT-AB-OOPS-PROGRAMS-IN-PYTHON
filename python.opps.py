import math
class Circle:
    def __init__(self,ram):
        
      self.ram=ram
      
    def area(self):
        
        return(math.pi*self.ram**2)
    
    def peri(self):
        
        return 2*math.pi*self.ram
    
ram=float(input("Enter the radius: "))

sri=Circle(ram)

area=sri.area()

print("area of the circle is:",area)

peri=sri.peri()

print("perimiter ofthe circle",peri)





      
