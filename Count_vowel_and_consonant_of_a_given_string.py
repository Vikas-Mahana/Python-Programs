#Count vowel and consonant of a given string.
Str  = input("enter a string: ")
def vowel_cons(n):
    vowel = 0
    cons = 0
    for i in n:
        if i in 'aeiou':
            vowel = vowel+1
        else:
            cons = cons+1
    print(vowel, cons)
vowel_cons(n)