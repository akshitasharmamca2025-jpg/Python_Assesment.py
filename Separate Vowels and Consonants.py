# Program to separate vowels and consonants from a sentence
def separate_characters():
    sentence = input("Enter a sentence: ")
    vowels_list = []
    consonants_list = []
    
    vowels = "aeiouAEIOU"
    
    for char in sentence:
        if char.isalpha(): # Checking if the character is an alphabet
            if char in vowels:
                vowels_list.append(char)
            else:
                consonants_list.append(char)
                
    print(f"Original Sentence: {sentence}")
    print(f"Vowels found: {vowels_list}")
    print(f"Consonants found: {consonants_list}")

separate_characters()

"""
Expected Output:
Enter a sentence: Hello World
Original Sentence: Hello World
Vowels found: ['e', 'o', 'o']
Consonants found: ['H', 'l', 'l', 'W', 'r', 'l', 'd']
"""s