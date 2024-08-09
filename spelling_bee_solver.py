import sys, os
# Code run with: python3 spelling_bee_solver.py LETTERS

# Word list in UNIX systems
_word_list = '/usr/share/dict/words'

# Scrabble word list
word_list = os.getcwd()+"/resources/sowpods.txt"

def parse_words():
    with open(word_list) as wl:
        # Extract and homogenize words from list
        words = [word.strip().upper() for word in wl]

        return words

def solve(letters, min_length=4):
    # Letters is a string of characters len:7, first character
    # needs to be included in the word
    
    middle_letter = letters[0]
    letter_set = set(letters)
    words = parse_words()

    possible_words = []
    for word in words:

        # As first exit case it is faster
        if len(word) < min_length:
            continue
        # Rules of the game
        if middle_letter not in word:
            continue

        # set(word) considers unique letters in the word,
        # and asks .issubset() if word has any that are not 
        # included in the letter set
        if set(word).issubset(letter_set):
            possible_words.append(word)
    
    print(f'{len(possible_words)} words found:')
    
    for w in sorted(possible_words, key=lambda word: (len(word), word)):
        print(f'{len(w)} - {w}',end="")
        if len(set(w)) == len(letter_set):
            print("  *****")
        else:
            print()
    

    
if __name__ == '__main__':
    letters = sys.argv[1] # first entry after file to run
    letters = letters.upper()
    assert(len(letters)==7)
    solve(letters)
