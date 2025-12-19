# Ask the users to input a word and count vowel and consonants using a function
word = input("Enter a word:")
def count_vc(word):
    vowels ="aeiouAEIOU"
    v=0
    c=0

    for ch in word:
        if ch.isalpha():
            if ch in vowels:
                v+=1
            else:
                c+=1
        return v,c

v,c= count_vc(word)
print("Vowel=",v)
print("Consonants=",c)