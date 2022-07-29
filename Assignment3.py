def countLetters(word) :
    letters = {}
    for letter in word :
        if letter not in letters :
            letters[letter] = 1
        else :
            letters[letter] +=1
    return letters

print(countLetters("mississippi")) 
