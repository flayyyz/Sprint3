a = int(input('Кол-во часов: '))
b = int(input('Кол-во семплов: '))
def f(n):
    c=1
    if b == 1 :
        if n > 2:
            c = f(n-1) + f(n-2)
        return c
    elif b == 2:
        if n==1:
            c=1
        elif n==2:
            c=b+1
        elif n%2==0:
            c=(f(n-1)*2)+1
        elif n%2==1:
            c=(f(n-1)*2)-1
        return c
    elif b==3:
        if n==1:
            c=1
        elif n==2:
            c=b+1
        elif n%2==0:
            c=(f(n-2)*f(n-1))-1
        elif n%2==1:
            c=(f(n-2)*f(n-1))+3
        return c
    elif b==4:
        if n==1:
            c=1
        elif n==2:
            c=b+1
        elif n%2==0:
            c=(f(n-1)*3)+2
        elif n%2==1:
            c=(f(n-1)*2)-1
        return c 
    elif b ==5:
        if n==1:
            c=1
        elif n==2:
            c = b+1
        elif n%2==1:
            c=(f(n-1)*2)-1
        elif n%2==0:
            c=(f(n-2)*f(n-1))+5
        return c   
value = f(a)
print(str(value))
