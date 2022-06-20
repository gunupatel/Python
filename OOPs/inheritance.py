class A:
   def feature1(self):
       print("feature1 is working")
   def feature2(self):
       print("feature2 is working")
# --------------------------------------------child/sub class
class B(A):         #------------------this is called single level inheritance
# class B:
   def feature3(self):
       print("feature3 is working")
   def feature4(self):
       print("feature4 is working")
# --------------------------------------------another child class  -> we will use in multi level inhertance
class C(B):
# class C(A,B):         #----------------- this is called multiple inheritance
   def feature5(self):
       print("feature5 is working")
a1 = A()
a1.feature1()
a1.feature2()
b1 = B()
b1.feature3()
b1.feature4()
c1 = C()
c1.feature5()
