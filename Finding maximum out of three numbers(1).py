# def maximum(num1, num2, num3):
#     if(num1>num2):
#         if(num1>num3):
#             return num1
#         else:
#             return num3
#
#     else:
#         if(num2>num3):
#             return num2
#         else:
#             return num3
# m=maximum(23,43,56)
# print("The maximum value is: " ,str(m))
print("Enter 1st number :")
n1=int(input())
print("Enter 2nd number :")
n2=int(input())
print("Enter 3rd number :")
n3=int(input())
if(n1>=n2 or n1>=n3):
    print("Largest number is : ",n1)
elif(n2>=n3 or n2>=n1)   :
    print("Largest number is : ",n2)
else:
    print("Largest number is : ",n3)

