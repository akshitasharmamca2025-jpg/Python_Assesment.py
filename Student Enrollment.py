# Program to identify students enrolled in multiple courses using sets
def check_multiple_enrollment():
    # Tuples containing (Student Name, Course)
    enrollments = (
        ("Amit", "Python"),
        ("Sita", "Java"),
        ("Amit", "Data Science"),
        ("Rahul", "Python"),
        ("Sita", "Web Dev")
    )
    
    # Logic to find students in more than one course
    student_counts = {}
    for name, course in enrollments:
        student_counts[name] = student_counts.get(name, 0) + 1
        
    multi_course_students = {name for name, count in student_counts.items() if count > 1}
    
    print(f"Students enrolled in multiple courses: {multi_course_students}")

check_multiple_enrollment()

"""
Expected Output:
Students enrolled in multiple courses: {'Amit', 'Sita'}
"""