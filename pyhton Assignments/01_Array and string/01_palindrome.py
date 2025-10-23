str="madam"
n=len(str)
result= ""

for char in range(n-1,-1,-1):
    result += str[char]
# print(result)

if str == result :
   print("palindrome")

else:
    print(" not palindrome")