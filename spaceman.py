import random
letters_guessed = []
tries = 7
def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    
    for letter in secret_word:
        # print(letter)
        if letter not in letters_guessed:
            return False
        
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    for letter in secret_word:
        if letter in letters_guessed:
            print(letter, "", end=''),
        else:
            print('_ ', end=''),
    print('\n')


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #TODO: check if the letter guess is in the secret word
    global tries
    if guess in secret_word:
        print('Good job! You guessed correctly! Letters guessed:', letters_guessed)
        return True
    else:
        tries -= 1
        print("That's incorrect! Guess again. Letters guessed:", letters_guessed)
        print(f"You have", tries, "guesses left")
        print("                         _______________________")
        print("                       //   __..--~~~~--..__    \\")
        print("                      ||___/  |  |   |  |   \ __/ |")
        print("                      ||  /   ___________    \    |")
        print("                      ||_/   /.......... \    |   |")
        print("                      | |   /..........   \   |   |")
        print(" _____________________| |  /...........    \  |   |________________")
        print("  ;   . . .   .       |_| |...........      | |   | .''.\"...  ... .")
        print(" ___   ..~.         _.' | |..........       | |   |         . ~")
        print("  .      '     .   / \_.| |..........       | |   |\ ~.   ._..---._")
        print("                  |. /| \ \............     / /   |/ .    /\      /\ ")
        print("    '\"\"\" ... ~~~  | \|| _\ \............   / /-.__|      // ~-._./ -\ ")
        print("  ..~             |  |_.~\\ \_____________/ /// '.|     /__       __.\ ")
        print("  ___   ..~.      |_.~   .\\_______________//   _ ~-.  ~~~~..  ~~~~~.")
        print("                 .~ -.     \__.---.________/   ______\.")
        print(" .''.\"...  ... ./\        _|      |---|  = |__ \__\===\   '\"\"\" ... ~~~")
        print("               /  '.  .  |_|=     |---|    | _| \======\ ___   ..~.")
        print("   ..~        / .   \      |=     |___|    ||       __. \ ")
        print("             /           _ |_______________|   _.        \ ")
        print(" .''.\"...  ./                /   \___    ~~  \            \  '\" ..   ~~")
        print("           /          '' /   \      /         \           /\ ")
        print(" ___   .  /     -- .   /'   __\____/       ____\___.'   --  \ ___   ..~.")
        print("         /            /    / \\ --  _____//          ~ - .   \ ")
        print("  ..--  /_..-       ./.   /  _/   _|___  \\       .     -   _/) ")
        print("       /   ___     ./|__  / _/   (_____ / \\  .          \ ~ /   . ")
        print("   .  /___////_   /  |   / _/    (_____ \  \\       _./ ..__/ ")
        print("     /___/__/_ \ /  _|  /__/ _-- (_____  \:_\\_____________/      ._ ")
        print(" _  /         \ /_.' | /  /       (_________/ ~~-| ")
        print("   /           //   _|/  /-              .    __ |..~. _____ -.. '  \" ")
        print(" ..\==========/'   \_/ _/  __      ___..     /  \| ")
        print("     / _____  \'.______/___....------......__\__/| ")
        print(" '  |          \     |\__________________|__|___/|  ~~~~~..   - ~  ' ")
        print("  ~ |        _  \   /~      \     \ --  /         \ ")
        print("    | | | | | \_|  |   \     \ ~      //           | ")
        print(" _. |_| | | | .    |-----..   \       /  /-      __|..~. _____ -.. '  \" ")
        print("      |_|_|_|   _. |       \_  \\ _ ./          ___| ")
        print("  ~~~  ..   - ~  ' |         \__\___/__...------   |  ~~~~~..   - ~  '")
        print("                   |  .-         | | .       __    |")
        print("                   |     __..    | |    ______     |      .     ~")
        print("..~. _  __ -.. '   \           __| |   |      |    | _        .")
        print("                   /             | | ~ |__.___|.   |")
        print("                   |    __       | |   |      |    |              .. '")
        print("  ~~~~~..   - ~  ' | ''          / \   |      |    |___     __.")
        print("  ....   -         |  _____...   | |   \______/    |  ~~~~~..   - ~  '")
        print("                   | /        '--| |      ~~       |")
        print("     ~..   - ~  '  |/            | |    __----  .. |   .      .     _")
        print("                   ||____......._| |               |")
        print("                   |----         | |               |  ~~~~~..   - ~  '")
        print("   '\"\"\" ... ~~~    |       -.    | |       _..     |")
        print("                   | ..         // |               | _~"".    .")
        print("                   |          -  \ | __----.   ..  \ ")
        print("  ~~~..   - ~  '   |_____________| |_______________/ ")
        print("                   \_____________| |______________/   '    ...  __  ~")
        print("                    /     ----- \   /----------- \ ")
        print("   __~~..   - ~  ' /___      ----\ /--...___      \ ")
        print("                  /    ..--      | | __..     ___./  .     .   ~")
        print("      - ~  '..    \  __________./  |_____________/  .   - ~  ' ~~~~")
        print("  ..._____~~~~~~JRO\___________/    \___________/  -_______...._____")
        print("..            ___ . ~~~~~~~~~~~. __\ ~~~~~~~~~~~~~...      _  ~")
        print("__    ....         ''        ...""       ....'''      -_~~~     ~~~...")
        return False



def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''


    #TODO: show the player information about the game according to the project spec
    print('Welcome to spaceman!')
    print('Spaceman is a guessing game. There is a mystery word which you try to guess one letter at a time.')
    print('A placeholder is initially shown, with the number of blanks corresponding to the number of letters in the word.')
    print('If the letter is in the mystery word, the position(s) of the letter(s) are revealed in the placeholders.')
    print('The spaceman is made up of seven parts, and each part is drawn for each incorrect guess.')
    print('If all seven parts get drawn before you guess the word, then you lose.')
    print('Guess the word before you run out of guesses!')
    print("Let's start!")

    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    
    while is_word_guessed(secret_word, letters_guessed) == False:
        global tries
        guess = input('Please enter a letter > ')

        if len(guess) == 1:
            if str(guess) not in letters_guessed:
                letters_guessed.append(guess)
            else: 
                tries += 1
                print("Oops! You've already guessed that letter!")
            # print(letters_guessed)
        else:
            print('Please enter only one letter at a time')

        #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        is_guess_in_word(guess, secret_word)
        #TODO: show the guessed word so far
        get_guessed_word(secret_word, letters_guessed)
        #TODO: check if the game has been won or lost
        is_word_guessed(secret_word, letters_guessed)
        # ends game if player runs out of tries
        if tries == 0:
            print("You Lost! The secret word was", secret_word)
            break
    
    if is_word_guessed(secret_word, letters_guessed) == True:
        print("You win! YAYYYAYAYYAYAYY")

#These function calls that will start the game

secret_word = load_word()
# print(secret_word)
spaceman(secret_word)

# test = is_word_guessed('abc', ['a', 'b', 'c'])
# print(test)
# test = get_guessed_word('paranoia', ['a', 'n'])
# print(test)
# test = is_guess_in_word('f, d, g', 'abc')
# print(test)


