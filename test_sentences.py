from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import pytest


def test_get_determiner():
    # Test the singular determiners.
    singular_determiners = ["the", "one", "that"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert word in singular_determiners

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the plural determiners.
    plural_determiners = ["some", "many", "these"]
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    # Test the singular nouns
    singular_nouns = ["adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]

    for _ in range(4):
        noun = get_noun(1)

        assert noun in singular_nouns
    # Test the plural nouns
    plural_nouns = ["adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]

    for _ in range(4):
        noun = get_noun(2)

        assert noun in plural_nouns

def test_get_verb():
    # Test the past verbs
    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(4):
        verb = get_verb(1, 'past')

        assert verb in past_verbs
    # Test the singular present verbs
    singular_present_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]

    for _ in range(4):
        verb = get_verb(1, 'present')

        assert verb in singular_present_verbs
    # Test the plural present verbs
    plural_present_verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    
    for _ in range(4):
        verb = get_verb(2,'present')

        assert verb in plural_present_verbs
    # Test the future verbs
    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    for _ in range(4):
        verb = get_verb(1, 'future')

        assert verb in future_verbs

def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    for _ in range(4):
        preposition = get_preposition(1)

        assert preposition in prepositions

def test_get_prepositional_phrase():
    phrase = get_prepositional_phrase(1)
    new_phrase = phrase.strip(',')

    assert new_phrase in phrase

# Calls the pytest function as the main function
pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])