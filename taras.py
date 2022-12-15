import math
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def random_letters():
    alp = ["a", "e", "i", "o", "u", "y", "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
    massLetters = []
    for i in range(7):
        massLetters.append(random.choice(alp))
    return massLetters

def check_letters(word, letters):
    dict = get_frequency_dict(letters)
    for letter in word:
        try:
            if dict[letter] > 0:
                dict[letter] -= 1
            else:
                return False
        except:
            return False
    return True

def check_word(wordsList, word):
    for word1 in wordsList:
        if word1 == word:
            return True
    return False


def user_input(letters, wordsList):
    word = input("Enter word, or “!!” to indicate that you are finished: ").lower()
    if word == "!!":
        return "!!"
    if check_letters(word, letters):
        if check_word(wordsList, word):
            return word
        else:
            return "Error: 102"
    else:
        return "Error: 101"

def user_score(word, n):
    score = 0
    SCRABBLE_LETTER_VALUES = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
    if (7 - len(word) - 3 * (n - len(word))) > 1:
        score = score * (7 - len(word) - 3 * (n - len(word)))
    print("“out” earned ",score," points.")
    return score


def error_check(code):
    if code == "Error: 101":
        print("Error 101: Not valid letters")
        return True
    elif code == "Error: 102":
        print("Error 102: Not valid word")
        return True
    elif code == "!!":
        return True
    return False

def clear_letters(userWord, randomLetters):
    dict = get_frequency_dict(randomLetters)
    massWord = []
    for letter in userWord:
        dict[letter] -= 1
    for letter in randomLetters:
        if dict[letter] > 0:
            dict[letter] -= 1
            massWord.append(letter)
    return massWord

def user_ui(letters,score,totalscore):
    print("Current hand:" , letters)

def wild_card():
    c = ""
    while c != "N":
        c = input("Do you want use WILD CARD ???????? (Y/N)").upper()

def start_game():
    score = 0
    totalscore = 0
    wordsList = load_words()
    randomLetters = random_letters()

    wild_card()
    print("Current hand:" , randomLetters)
    userWord = user_input(randomLetters, wordsList)
    while not error_check(userWord):
        score += user_score(userWord, len(randomLetters))
        randomLetters = clear_letters(userWord, randomLetters)
        print("Current hand:" , randomLetters)
        userWord = user_input(randomLetters, wordsList)
    user_ui(randomLetters,score,totalscore)

start_game()