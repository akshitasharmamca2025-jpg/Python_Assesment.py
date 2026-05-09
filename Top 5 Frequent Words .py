# Program to store word frequencies from a file and display top 5
def get_top_five_words(filename):
    try:
        # Creating a dummy file for demonstration
        with open(filename, "w") as f:
            f.write("apple banana apple cherry date elderberry banana apple cherry banana apple")

        word_counts = {}
        with open(filename, "r") as file:
            for line in file:
                # Splitting line into words and cleaning them
                words = line.lower().split()
                for word in words:
                    word = word.strip(".,!?")
                    word_counts[word] = word_counts.get(word, 0) + 1
        
        # Sorting dictionary by value in descending order
        sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        
        print("Top 5 Most Frequent Words:")
        for word, count in sorted_words[:5]:
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("Error: The file was not found.")

get_top_five_words("words_data.txt")

"""
Expected Output:
Top 5 Most Frequent Words:
apple: 4
banana: 3
cherry: 2
date: 1
elderberry: 1
"""