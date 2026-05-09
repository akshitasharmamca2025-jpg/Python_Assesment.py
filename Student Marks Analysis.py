# Read student marks from a file and analyze data
def analyze_marks_file():
    # Creating a sample file for the program to read
    with open("student_marks.txt", "w") as f:
        f.write("Alice:88\nBob:95\nCharlie:70\nDavid:60")

    marks_data = {}
    with open("student_marks.txt", "r") as f:
        for line in f:
            name, score = line.strip().split(':')
            marks_data[name] = int(score)

    avg = sum(marks_data.values()) / len(marks_data)
    topper = max(marks_data, key=marks_data.get)
    below_avg = [name for name, score in marks_data.items() if score < avg]

    print(f"Topper: {topper} ({marks_data[topper]})")
    print(f"Average Marks: {avg}")
    print(f"Students Below Average: {below_avg}")

analyze_marks_file()

