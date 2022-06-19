# x=int(input("how many candid u want"))
# av =5
# i=1
# while i <= x:
#
#     if i>av:
#         print("out of stock")
#         break
#     print("candy")
#     i=i+1

for i in range(1,101):
    if i%3==0:
        continue

    print(i)