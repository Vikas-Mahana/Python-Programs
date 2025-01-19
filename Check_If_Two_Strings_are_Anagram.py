#Check If Two Strings are Anagram
s1 ="listen"
s2 ="silent"
if sorted(s1) == sorted(s2):
    print("Both are anagram")
else:
    print("not anagram")