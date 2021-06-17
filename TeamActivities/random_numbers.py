"""
Team 1B Activity # 7

random_numbers.py
"""
import random

def append_random_numbers(numbers_list, quantity=1):
   
    for i in range(quantity):
        
        random_number = random.uniform(1, 100)
        new_random_number = random_number.__round__(1)
        numbers_list.append(new_random_number)

def append_random_words(words_list, quantity=1):
    words = ['join', 'love', 'smile', 'love', 'cloud', 'head']
    
    for i in range(quantity):

        random_word = random.choice(words)
        words_list.append(random_word)
 

def main():
    randnums = [16.2, 75.1, 52.3]
    print(randnums)
    append_random_numbers(randnums)
    print(randnums)
    append_random_numbers(randnums, 3)
    print(randnums)
    
    wordslist = ["tree", "face"]
    print(wordslist)
    append_random_words(wordslist)
    print(wordslist)
    append_random_words(wordslist, 3)
    print(wordslist)
    
    

main()