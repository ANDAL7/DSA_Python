word = input()
result = []
current_num = ""  
for char in word:
    if char in "+-%^*/":  
        if current_num:
            result.append(current_num.strip())  
        result.append(char)
        current_num = ""
    else:
        current_num += char

if current_num:
    result.append(current_num.strip())

word_lis = [item for item in result if item.strip() != ""]

for i in range(len(word_lis)):
    if word_lis[i].isdigit():
        continue
    else:
        a = int(word_lis[i-1])
        b = int(word_lis[i+1])

        if word_lis[i] == "+":
            print(a + b)
        elif word_lis[i] == "-":
            print(a - b)
        elif word_lis[i] == "*":
            print(a * b)
        elif word_lis[i] == "^":
            print(a ** b)
        elif word_lis[i] == "%":
            print(a % b)
        elif word_lis[i] == "/":
            if b == 0:
                print("Invalid")
            else:
                c = round(a / b)
                print(c, a % b)
