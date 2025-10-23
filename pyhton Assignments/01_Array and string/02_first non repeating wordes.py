def first_non_repeating(s):
    freq = {}             # Step 1: Create an empty dictionary
    for ch in s:          # Step 2: Traverse the string
        if ch in freq:    
            freq[ch] += 1 # If char exists, increase count
        else:
            freq[ch] = 1  # Else, initialize count as 1

    for ch in s:          # Step 3: Traverse string again
        if freq[ch] == 1: # Find first character with count 1
            return ch
    return None           # If no non-repeating char found

print(first_non_repeating("swiss"))  #


# example all non repeating characters withusing append
def all_non_repeating(s):
    freq = {}  # Step 1: Count frequency of each character
    
    # Count frequencies
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # Collect all characters with frequency 1
    result = []
    for ch in s:
        if freq[ch] == 1:
            result.append(ch)
    
    return result

# Example
print(all_non_repeating("swiss"))  # ['w', 'i']

# without using append
def all_non_repeating_no_append(s):
    freq = {}  # Step 1: Count frequency of each character
    
    # Count frequencies
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # Collect all non-repeating characters in a string
    result = ""   # empty string instead of list
    for ch in s:
        if freq[ch]  == 1:
            result = result + ch  # concatenate instead of append
    
    return result

# Example
print(all_non_repeating_no_append("swiss"))  # wi




def repeated_chars_only(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    result = ""
    for ch in freq:
        if freq[ch] > 1:
            result = result + ch

    return result

# Example
s = "kjhfhhhhhhhhhhhhhbbbbbbb"
print(repeated_chars_only(s))
    