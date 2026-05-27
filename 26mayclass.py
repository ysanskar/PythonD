# n=7
# for i in range (n):
#     for i in range(n):
#         if j==0 or j==n-1 or i==n//2:
#             print("*",end=" ")
#         else:
#             print


# n=7
# for i in range (n):
#     for j in range(n):
#         print("In")

#     print("exit")


# n=7
# for i in range (n):
#     for j in range(n):
#         print("In" , end=" ")

#     print("exit")


n=7
for i in range (n):
    for j in range(n):
        if j==0 or j==n-2 or i==n//2:
            print("*" , end=" ")
        else:
            print(" " ,end=" ")
    print( )