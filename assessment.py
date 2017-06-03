"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    # split phrase on spaces to return list of words
    words = phrase.split(' ')

    # empty dictionary to count unique words
    unique_words = {}

    # iterate through words, add as keys in dict
    # default value 0, increment by 1
    for word in words:
        unique_words[word] = unique_words.get(word, 0) + 1

    return unique_words


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """

    melon_prices = {
        'Watermelon': 2.95,
        'Cantaloupe': 2.50,
        'Musk': 3.25,
        'Christmas': 14.25
        }

    # use .get to return 'No price found' if melon_name not in melon_prices
    return melon_prices.get(melon_name, 'No price found')


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        >>> word_length_sorted(["porcupine", "ok"])
        [(2, ['ok']), (9, ['porcupine'])]
    """

    # empty dict to store word lengths
    word_lengths = {}

    # iterate through words list
    for word in words:
        # keys = word lengths; use .get to set value of each key to empty list
        word_lengths[len(word)] = word_lengths.get(len(word), [])
        # append each word to the values list for its length
        word_lengths[len(word)].append(word)
        # sort values list in place so words are ordered alphabetically
        word_lengths[len(word)].sort()

    # return tuples of word lengths & words of that length in ascending order
    return sorted(word_lengths.items())


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    english_pirate_translation = {
        'sir': 'matey',
        'hotel': 'fleabag inn',
        'student': 'swabbie',
        'man': 'matey',
        'professor': 'foul blaggart',
        'restaurant': 'galley',
        'your': 'yer',
        'excuse': 'arr',
        'students': 'swabbies',
        'are': 'be',
        'restroom': 'head',
        'my': 'me',
        'is': 'be'
        }

    # list of words in phrase split on spaces
    words = phrase.split(' ')

    # iterate through words list by index
    # replace words that are keys in dict with their values
    for i in range(len(words)):
        if words[i] in english_pirate_translation:
            words[i] = english_pirate_translation[words[i]]

    # return words list as string joined by spaces
    return ' '.join(words)


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    # empty dict to hold letters and the words that begin with that letter
    # ex. {'n': ['noon', 'naan', 'nun']}
    words_by_first_letter = {}

    # iterate through names list by index, skipping first word in the list
    for i in range(len(names) - 1):
        # keys are first letters of words in list
        key = names[i + 1][0]
        word = names[i + 1]
        # set initial value of each key to empty list
        words_by_first_letter[key] = words_by_first_letter.get(key, [])
        # append word to value list of key corresponding to word's first letter
        words_by_first_letter[key].append(word)

    # start word chain with first word in passed in list
    word_chain = [names[0]]

    # starting key is last letter of first word in word chain
    current_key = names[0][-1]

    # break if key not in dict or no more words begin with that letter
    while current_key in words_by_first_letter and words_by_first_letter[current_key] != []:
        # next word for chain is first word in values list for the current key
        next_word = words_by_first_letter[current_key][0]
        # append word to chain
        word_chain.append(next_word)
        # new key is last letter of word
        new_key = next_word[-1][-1]
        # remove word from values list
        words_by_first_letter[current_key].remove(next_word)
        # set current key to new key
        current_key = new_key

    return word_chain


#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
