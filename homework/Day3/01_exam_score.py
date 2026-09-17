test_cases = int(input(""))
for i in range(test_cases):
    ln = int(input())
    arr = list(map(int,input().split()))
    print("Scores")
    for i in range(0,ln,4):
        print(*arr[i:i+4],sep=" ")
        
    print("average")
    print(f"{sum(arr)/ln:.2f}")
    
    print("lowest score")
    print(min(arr))
    
    print("highest score")
    print(max(arr))
    
    print("score deviation")
    for i in arr:
        print(f"{i}   {i-(sum(arr)/ln):.2f}")
        
    print("standard deviation")
    sd = 0
    for i in arr:
        sd += (i- (sum(arr)/ln))**2
        
    
    print((sd/ln)**(1/2))
    
    count = 0
    for i in arr:
        if (((sum(arr)/ln)-((sd/ln)**(1/2)))<=i<=((sum(arr)/ln) + ((sd/ln)**(1/2)))):
            count+=1
            
    print("Scores within one standard deviation: ",count)
