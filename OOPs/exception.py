a = 6
b = 2

try:

    print("resource open")
    print(a/b)
    k = int(input("enter the number"))
    print(k)

except ZeroDivisionError as e:
    print("hey, you cannot divide a number by zero", e)

except ValueError as e:
    print("ivalid input")

except Exception as e:
    print("something went wrong...")
   
finally:
    print("resource closed")