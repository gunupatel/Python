#class Computer:
#    def config(self):
#        print("i5, 16gb, 1tb")
#com1 = Computer()
#Computer.config(com1)
#com1.config()



class Car:
    wheels = 3
    def __init__(self):
        self.mil = 10
        self.com = "BMW"
c1 = Car()
c2 = Car()
c1.mil = 12
Car.wheels =4
print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)
