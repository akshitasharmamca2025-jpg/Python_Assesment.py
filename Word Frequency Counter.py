def word_frequency():
    paragraph = input("Enter a paragraph: ")
    # Split into words and convert to lowercase
    words = paragraph.lower().split()
    frequency = {}

    for word in words:
        # Remove basic punctuation
        word = word.strip('.,!?')
        frequency[word] = frequency.get(word, 0) + 1

    # Find the most repeated word
    most_repeated = max(frequency, key=frequency.get)
    
    print(f"\nWord Frequencies: {frequency}")
    print(f"Most Repeated Word: '{most_repeated}' (count: {frequency[most_repeated]})")

word_frequency()

"""
Expected Output:
Enter a paragraph: apple banana apple cherry banana apple
Word Frequencies: {'apple': 3, 'banana': 2, 'cherry': 1}
Most Repeated Word: 'apple' (count: 3)
"""