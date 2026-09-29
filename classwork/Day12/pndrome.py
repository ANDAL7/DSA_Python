word = input().lower()
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")