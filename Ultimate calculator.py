print("Hello World")
print("1st number \n")
n1=int(input())

print("2nd number /n")
n2=int(input())
print('So what you want?' '+,-,%,*,/')
n3=input()
if n3=='+':
    n4=n1+n2
    print(n4)
if n3=='/':
    n4=n1/n2
    print(n4)
if n3 == '*':
    n4 = n1 * n2
    print(n4)
if n3 == '%':
    n4 = n1 % n2
    print(n4)
if n3 == '-':
    n4 = n1 - n2
    print(n4)
