test_case = int(input("number of test_cases \n"))
for i in range(0,test_case):
    arr = input().split(" ")
    sum_odd = 0.00
    count_odd = 0.00
    sum_even = 0.00
    count_even = 0.00

    for i in arr:
        i = int(i)
        if(i%2==0):
            sum_even += i
            count_even +=1
        else:
            sum_odd += i
            count_odd +=1

    if(count_odd!=0):
        avg = round(sum_odd/count_odd ,2)
        print("average_odd",avg)
    else:
        print("average_odd : 0.00")
    if(count_even!=0):
        avg1 = round(sum_even/count_even ,2)
        print("average_even",avg1)
    else:
        print("average_even : 0.00")