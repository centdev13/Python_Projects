
##done with get_selection() function
def get_selection(prompt, choices):
    """Gets the selection from the user.  They are given the prompt text, and have to enter a valid choice.
    :param prompt: string displayed to the user.  Eg. menu or choices.
    :param choices: list of possible correct choices for the situation.  This is a list of strings ["1", "2", .. ]
    :return: Returns a string or character matching one of the choices.

    Continually prompts the user for the appropriate input.  Will return the choice only when a valid one is retrieved.
    """

    #Add code here


    ##Ask for input
    inp = input(prompt)

    ##Store results of prompt conditional here
    inp_done = ''

    ##While invalid, run this code
    while inp not in choices:
        inp_done = input("You've entered incorrect input. Try again.")


    return inp_done

def return_text_file(prompt, mode="r"):
    """ Returns a valid open file.
    :param prompt: The string to display to the user asking them to open a file.
    :param mode: The filemode to open the file in.
    :return: The file handle for the file.

    If there is an error opening the file, then an error will be displayed and the user will be prompted again.
    """

    #Add code here
    with open(prompt,'w','r') as f:
        for line in f:
            for word in line:
                print(word)

    return f

##done with remove_punctuation function
def remove_punctuation(word):
    """ Removes ending punctuation from a word, returns back the clean word and the punctuation.
    :param word: This is a string with a single word.  It may have punctuation on the end that needs to be removed
    :return: Returns a tuple, the word without the ending punctuation and the punctuation.
    """

    #Add code here

    ##if the input has any punctuation characters at the end of it, record them in a separate variable, but delete them
    ## from the first input string
    a = list(".?!")
    b = list(word)
    c = b



    ending_punc = ''

    ord_values_punct = [33, 46, 63]

    ##loop through the users input string
    for index, iterator in enumerate(b):
        ##at the same time loop through the punctuation characters we'll be looking for in the string
        for ind, it in enumerate(a):
            ##if the letter being iterated over in the user's string matches any one of the punctuation
            ## characters we are looking for, record it's index
            if ord(iterator) == ord(it):
                ending_punc = iterator
                c.remove(iterator)
                last_index_before_punct = index-1
                ##If there are any characters past the first punctuation character, error it out.
                try:
                    if b[index+1] != IndexError:
                        print("There can be no characters following the first punctuation character.")
                        break
                except Exception:
                    pass

            elif ord(iterator) != ord(it):
                pass

    d = ''.join(c)
    # print("String entered was {}".format(d))
    # print("Ending punctuation of string is: \"{}\"".format(ending_punc))

    return d, ending_punc

def pigify(word):
    """  Takes a word and pig latins it
    :param word: This is a word to pig latin
    :return: returns a string with the pig latin version of the word.

    If the word starts with one or more consonants, they are moved to the end of the word and 'ay' is added ot the end
        pig => igpay
        create => eatecray
    If the word starts with a vowel then the 'way' is simply added to the end.
        essay => essayway
    If there was any punction on the word then that is added to the end.
        pig! => igpay!

    http://en.wikipedia.org/wiki/Pig_Latin
    """

    #Add code here


    return ""

def gibberish(word):
    """ Takes a word and makes gibberish out of it.
    :param word: This is the original word to change into gibberish
    :return: returns a string that is the original word changed into gibberish by our rules.

    Gibberish is accomplished by adding 'idig' before each new vowel sound.
        pig => pidigig
        create => cridigeatidige
        essay => idigessidigay
        pig! => pidigig!

    http://en.wikipedia.org/wiki/Gibberish_(language_game)

    """

    #Add code here

    return ""

def ubbi_dubbi(word):
    """ Converts a word into a ubbi dubbi version of it.
    :param word: The original word to change into ubbi dubbi by our ubbi dubbi rules.
    :return: Returns the word after it has been ubbi dubbi fied..

    ubbi_dubbi is accomplished by adding 'ub' before each new vowel sound.
        pig => pubig
        create => crubeatube
        essay => ubessubay
        pig! => pubig!

    http://en.wikipedia.org/wiki/Ubbi_dubbi

    """

    #Add code here

    return ""

def izzle(word):
    """ Converts a word into the izzle dizzle version of it.
    :param word: The original word to change into izzle
    :return: Returns the word after it has been izzled.

    izzle is accomplished by adding 'izzle' from the last vowel to the end of the word
        pig => pizzle
        create => creatizzle
        essay => essizzle
        pig! => pizzle!

    http://en.wikipedia.org/wiki/Ubbi_dubbi

    """

    #Add code here
    ##modify_line

    return ""

def modify_line(line, modification_choice):
    """ Takes a line of text breaks it into words and does the modification requested.
    :param line: string.  This is a line of text.
    :param modification_choice: What modification to be done to the words, '1' pig latin, '2' gibberish, '3' ubbi dubbi
    :return: new string line with all the words having the modification done to them.
    """

    #Add code here

    return ""

if __name__ == "__main__":

    #The main program code goes here.
    get_selection("""
    What translation do you want to perform?/n
        1. Pig Latin
        2. Gibberish
        3. izzle
        4. Quit

        ==> """,['1','2','3','4'])

    #file_name = input("Enter the name of the file to convert ==>  ")

    #remove_punctuation("son?")
    #modify_line(word)

    ##pigify(word)
    ##izzle(word)
    ##ubbi dubbi(word)
    ##gibberish(word)

    #file_name_output = input("Enter the name of the file to output ==>  ")



    pass
