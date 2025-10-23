s1 = "listen"
s2 = "silenth"

for ch in s1:
    # Try to remove ch from s2 manually
    new_s2 = ""
    removed = False
    for c in s2:
        if c == ch and not removed:
            removed = True  # skip this character
            continue
        new_s2 += c
    s2 = new_s2  # update s2 after removing one occurrence

if not s2:
    print("True")
else:
    print("False")


