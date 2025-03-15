def num_letters(file_contents):
    number_of_letters = {}
    for character in file_contents.lower():
        if character in number_of_letters:
            number_of_letters[character] += 1
        else:
            number_of_letters[character] = 1
        
    return number_of_letters


#takes in a string and returns the number of each character in it, lowecase only
#in a dictionary

def num_words(file_contents):
    words = len(file_contents.split())
    return words
#takes in a string and returns the number of words in it

def sort_on(dict):
    return dict["number"]

def dictionary(number_of_letters):
    list_of_numbers = []
    for char, number in number_of_letters.items():
        list_of_numbers.append({"char": char, "number": number})
    list_of_numbers.sort(reverse=True, key=sort_on)
    for number_of_letters in list_of_numbers:
        character = number_of_letters["char"]
        number = number_of_letters["number"]
        if character.isalpha():
            print(f"{character}: {number}")
    


