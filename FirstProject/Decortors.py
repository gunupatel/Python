def divide(x,y):
    print(x/y)
def outer_div(func):
    def inner(x,y):
        if(x<y):
            x,y = y,x
           return func(x,y)
     return inner
divide1 = outer_div(divide)
divide1(2,4)  