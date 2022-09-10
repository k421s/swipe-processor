# improve input
# Basic functionality: the happiest path
# qwerty keyboard
# lowercase only with no whitespace or punctuation
# first and last characters of the input string always match first and last characters of input
# word is swiped correctly in that every letter of the word will appear in the input string


#word input for 'airbag'
#swipe_input = "asdfghyuiuytrfgvbcfdsasdfg"



# read the entire file to an array
word_file = open("/Users/karltonsuits/development/python/swipe processor/words.txt", "r")
word_list = word_file.read().splitlines()

#loop through every single word in array and check for matching word

# scrabbilize
# brute force edition

#loop through and check each character (with replacement)
swipe_input = "asdxcvbhjklkjhgfdsazse".upper()
target_word = "ablaze"


# looking for ablaze
# elements: search for character: remove character if found and go to next character
# for each word in the array, make a copy of the character_pool 

word = "gvcs"
print(word.find("z"))


# python method for finding each word
#TODO make it a method
#TODO replace flag strategy

#flag = True
#TODO change replace to list equivalent
#TODO rename character_pool and character_pool_instance

#copy character pool for modification



#TODO break this up into a method
def check_current_word(character_pool, current_word):
    current_character_pool = character_pool
    print("current character pool looks like this:", current_character_pool)
    for letter in current_word:
        if(current_character_pool.find(letter) == -1):
            print(letter, "was not found, word is not a match, ending for letter in current_word loop")
            return False
        else:
            print(letter, "was found in character_pool, deleting from current pool")
            # delete letter - replace letter with empty string
            current_character_pool = current_character_pool.replace(letter, '', 1)
            print("character pool currently looks like this:", current_character_pool)

    print("loop ran all the way through,", current_word, "is a match")
    print("end word pool looks like:")
    print(character_pool, "vs", current_character_pool)
    return True


#loop through a list of current words: 
small_word_group = ["ablaze", "dazed", "zzz", "faze"]
matched_words = []

swipe_input_instance = swipe_input

for word in word_list:
    if(check_current_word(swipe_input_instance, word)):
        matched_words.append(word)
    swipe_input_instance = swipe_input  
print(matched_words)
