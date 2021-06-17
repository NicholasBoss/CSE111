import random

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is a word
    like "the", "a", "one", "two", "some", "many". If quantity == 1,
    this function will return either "the" or "one". Otherwise
    this function will return either "some" or "many".

    Parameter
        quantity: an integer. If quantity == 1, this function will
            return a determiner for a singular noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["the", "one", "that"]
    else:
        words = ["some", "many", "these"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun. If quantity == 1, this
    function will return one of these ten singular nouns:
        "adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"
    Otherwise, this function will return one of these ten
    plural nouns:
        "adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"

    Parameter
        quantity: an integer that determines if the
            returned noun is singular or plural.
    Return: a randomly chosen noun.
    """

    if quantity == 1:
        nouns = ["adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]

    else:
        nouns = ["adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]

    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past", this
    function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this function will
    return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1, this function
    will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of these
    ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameter
        quantity: an integer that determines if the returned
            verb is singular or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

    if tense.lower() == 'past':
        verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    
    elif tense.lower() == 'present' and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]

    elif tense.lower() == 'present' and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]

    elif tense.lower() == 'future':
        verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    verb = random.choice(verbs)
    return verb

def get_preposition(quantity):
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    if quantity == 1:
        prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

        preposition = random.choice(prepositions)
        return preposition
 
def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and nouns are singular or plural.
    Return: a prepositional phrase.
    """

    if quantity == 1:
        phrase = (f"{get_preposition(quantity=1)} {get_determiner(quantity=1)} {get_noun(quantity=1)}")
        
        
    else:
        phrase = (f"{get_preposition(quantity=1)} {get_determiner(quantity=2)} {get_noun(quantity=2)}")
        
        
    
    return phrase 
def main():
   #past
    print(f"{get_determiner(quantity=1)} {get_noun(quantity=1)} {get_verb(quantity=1,tense='past')}.")
    print(f"{get_determiner(quantity=2)} {get_noun(quantity=2)} {get_verb(quantity=2,tense='past')}.")
    #present
    print(f"{get_determiner(quantity=1)} {get_noun(quantity=1)} {get_verb(quantity=1,tense='present')}.")
    print(f"{get_determiner(quantity=2)} {get_noun(quantity=2)} {get_verb(quantity=2,tense='present')}.")
    #future
    print(f"{get_determiner(quantity=1)} {get_noun(quantity=1)} {get_verb(quantity=1,tense='future')}.")
    print(f"{get_determiner(quantity=2)} {get_noun(quantity=2)} {get_verb(quantity=1,tense='future')}.")
    #Prepositional Phrase Past
    print(f"{get_determiner(quantity=1)} {get_noun(quantity=1)} {get_verb(quantity=1,tense='past')} {get_prepositional_phrase(quantity=1)}.")
    print(f"{get_determiner(quantity=2)} {get_noun(quantity=2)} {get_verb(quantity=2,tense='past')} {get_prepositional_phrase(quantity=2)}.")
    #Prepositional Phrase Present
    print(f"{get_determiner(quantity=1)} {get_noun(quantity=1)} {get_verb(quantity=1,tense='present')} {get_prepositional_phrase(quantity=1)}.")
    print(f"{get_determiner(quantity=2)} {get_noun(quantity=2)} {get_verb(quantity=2,tense='present')} {get_prepositional_phrase(quantity=2)}.")
    #Prepositional Phrase Future
    print(f"{get_determiner(quantity=1)} {get_noun(quantity=1)} {get_verb(quantity=1,tense='future')} {get_prepositional_phrase(quantity=1)}.")
    print(f"{get_determiner(quantity=2)} {get_noun(quantity=2)} {get_verb(quantity=1,tense='future')} {get_prepositional_phrase(quantity=2)}.")



main()