test_cases = int(input())
for i in range(test_cases):
    val = input()
    absent = val.count("0")
    total = ((len(val)-1)/2)+1
    percent = val.count("1")/total        
    if absent>0:
        print(f"{absent} students absent out of {total} students with percentage {percent:.2%} ")
    else:
        print("no absentees")