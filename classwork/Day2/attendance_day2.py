test_cases = int(input())
for i in range(test_cases):
    val = input()
    count = 0
    total =0
    for j in val:
        if j!=" ":
            total+=1
            if j == "0":
                count+=1
    
    percent = (total-count)/total        
    if count>0:
        print(count," students absent out of ",total," students with percentage", percent*100,"%")
    else:
        print("no absentees")