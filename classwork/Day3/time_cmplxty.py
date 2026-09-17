try:
    num = int(input())
    a = int(input())
    b = int(input())
    if num == 1:
        print(a)
    else:
        print(a, b, end=' ')

        
        for i in range(2, num):
            a, b = b, a + b
            print(b, end=' ')
except:
    print("Invalid input")