import random as randi

hangman = [
    '''
    +--------------------+
    |         ||
    |          0
    |          
    |        
    |
====+======================+
    
    ''',
    '''
    +--------------------+
    |         ||
    |          0      
    |          
    |        
    |
====+======================+
    ''',
    '''
    +--------------------+
    |         ||
    |          0      
    |          
    |        
    |
====+======================+
     ''',
    '''
    +--------------------+
    |         ||
    |          0      
    |          |
    |        
    |
====+======================+
     ''',
    '''
    +--------------------+
    |         ||
    |          0      
    |        / |
    |        
    |
====+======================+
     ''',
    '''
    +--------------------+
    |         ||
    |          0      
    |        / | /
    |        
    |
====+======================+
     ''',
    '''
    +--------------------+
    |         ||
    |          0      
    |        / | /
    |         /  /
    |
====+======================+
     ''',
]

'''
GAME LOGIC 
 load the random word
 take the input from the user
 check if the input is a word
 compare the guess with the original word

'''
''' 
FUNCTIONS
1. load random word from the list ,words
2. input guess
3. display all 


'''
# random words for the game

word = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret ' \
       'fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon ' \
       'python rabbit ram rat raven rhino salmon seal shark sheep snake spider stork swan tiger toad trout turkey ' \
       'turtle weasel whale wolf wombat zebra'.split()

# split() converts the string to list


def LoadRandomWord(words):
    index = randi.randint(0, len(word) - 1)
    return words[index]


def Make_A_guess():
    try:
        guess = input("\nEnter a letter:")
    except TypeError:
        print("Please enter a word")
    if len(guess) != 1:
        print("Enter a letter")
    elif not guess.isalpha():
        print("Enter a letter")
    elif guess == 'P':
        print(LoadRandomWord(word))
    else:
        return guess


def display(Hangman, correct_letter, miss_word, correct_word):
    blank = '_' * len(correct_word)
    print(Hangman[len(miss_word)])
    print('Word:', end=' ')
    for i in range(len(correct_word)):
        if correct_word[i] in correct_letter:
            blank = blank[:i] + correct_word[i] + blank[i + 1:]
    for letter in blank:
        print(letter, end=' ')


print('\t\tWelcome to hangman game')

MissWord = ' '
CorrectLetter = ' '
CorrectWord = LoadRandomWord(word)
run = True
GameisDone = False
# main Game loop
while run:
    display(hangman, CorrectLetter, MissWord, CorrectWord)
    guess_word = Make_A_guess()
    if guess_word in CorrectWord:
        CorrectLetter = CorrectLetter + guess_word
        found = True
        for i in range(len(CorrectWord)):
            if CorrectWord[i] in CorrectLetter:
                found = False
                break
        if found:
            print("Congrats!!!")
            GameisDone = True
    elif guess_word not in CorrectWord:
        MissWord = MissWord + guess_word
        if len(MissWord) == len(hangman)-1:
            display(hangman, CorrectLetter, MissWord, CorrectWord)
            GameisDone = True