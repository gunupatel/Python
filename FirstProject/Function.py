
# def greet():
#     print("Hllo")
#     print("GM")
#
# greet()

#function argument
# def update(x):
#     x=8
#     print("x",x)
#
# a=10
# update(a)
# print("a",a)

#types of argument
#formal agr
# def add(a,b):
#     c=a+b
#     print(c)
#
# add(5,6) #actual arg

#position arg
# def emp(id,name):
#     print(id)
#     print(name)
#
# emp(name='ram',id=11)

# scope
# a=10
# def something():
#     global a
#     a=15
#     print("in fun",a)
#
# something()
#
# print("outside",a)

#Lambda Function
#
# def square(a):
#     return a*a
# result = square(5)
# print(result)
#
# f=lambda a,b : a+b
# result=f(5,6)
# print(result)

# using filter()
# def is_even(n):
#     return n%3==0
nums =[2,3,4,5,6,7]
evens=list(filter(lambda  n: n%2==0,nums))

print(evens)