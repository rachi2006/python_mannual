def palindrome_check(s):
    return s == s[::-1]
s= input("Enter a string: ")
ans = palindrome_check(s)
if ans:
    print(f"{s} is a palindrome.")
else:
    print(f"{s} is not a palindrome.")
