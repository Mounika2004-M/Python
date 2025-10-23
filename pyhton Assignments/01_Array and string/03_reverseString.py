str = "mounika"
result =""

for char in range(len(str)-1,-1,-1):
    result +=str[char]
print(result)

###########################################################################################

def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev

print(reverse_string("hello"))  # 