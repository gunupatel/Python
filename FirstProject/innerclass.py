class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

        #inner class

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu='i5'
            self.ram=8
        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=Student("X",1)
s2=Student("Y",2)

#s1.show()

lap1= Student.Laptop()