
def get_num_words(book_text):

    text = book_text.split()

    return len(text)


def char_count(str):

    letter_count = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0, 
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0
}
    

    str = str.lower()

    for i in range(len(str)):
        if str[i] == 'a':
            letter_count['a'] = letter_count['a'] + 1
        elif str[i] == 'b':
            letter_count['b'] = letter_count['b'] + 1
        elif str[i] == 'c':
            letter_count['c'] = letter_count['c'] + 1
        elif str[i] == 'd':
            letter_count['d'] = letter_count['d'] + 1
        elif str[i] == 'e':
            letter_count['e'] = letter_count['e'] + 1
        elif str[i] == 'f':
            letter_count['f'] = letter_count['f'] + 1
        elif str[i] == 'g':
            letter_count['g'] = letter_count['g'] + 1
        elif str[i] == 'h':
            letter_count['h'] = letter_count['h'] + 1
        elif str[i] == 'i':
            letter_count['i'] = letter_count['i'] + 1
        elif str[i] == 'j':
            letter_count['j'] = letter_count['j'] + 1
        elif str[i] == 'k':
            letter_count['k'] = letter_count['k'] + 1
        elif str[i] == 'l':
            letter_count['l'] = letter_count['l'] + 1
        elif str[i] == 'm':
            letter_count['m'] = letter_count['m'] + 1
        elif str[i] == 'n':
            letter_count['n'] = letter_count['n'] + 1
        elif str[i] == 'o':
            letter_count['o'] = letter_count['o'] + 1
        elif str[i] == 'p':
            letter_count['p'] = letter_count['p'] + 1
        elif str[i] == 'q':
            letter_count['q'] = letter_count['q'] + 1
        elif str[i] == 'r':
            letter_count['r'] = letter_count['r'] + 1
        elif str[i] == 's':
            letter_count['s'] = letter_count['s'] + 1
        elif str[i] == 't':
            letter_count['t'] = letter_count['t'] + 1
        elif str[i] == 'u':
            letter_count['u'] = letter_count['u'] + 1
        elif str[i] == 'v':
            letter_count['v'] = letter_count['v'] + 1
        elif str[i] == 'w':
            letter_count['w'] = letter_count['w'] + 1
        elif str[i] == 'x':
            letter_count['x'] = letter_count['x'] + 1
        elif str[i] == 'y':
            letter_count['y'] = letter_count['y'] + 1
        elif str[i] == 'z':
            letter_count['z'] = letter_count['z'] + 1

        #count all instances of the char
        #add that count to the dictionary at the index of char
        #return dictionary


    #print(letter_count)
    return letter_count