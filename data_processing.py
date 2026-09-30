# This function calculates the average of a tuple of grades.
def get_average_grade(grades_tuple):
    try:
        total = sum(grades_tuple)
        average = total / len(grades_tuple)
        return average

    except ZeroDivisionError:
        print("Warning: No grades are available.")
        return None


# Dictionary containing courses and grade tuples.
course_grades = {
    "Math": (90, 85, 88, 92),
    "Science": (80, 82, 85, 87),
    "History": (75, 78, 80, 82),
    "English": ()
}


# Process each course.
for course, grades in course_grades.items():

    average = get_average_grade(grades)

    if average is not None:
        print(
            "The average grade for " +
            course +
            " is " +
            str(round(average, 2))
        )
    else:
        print("No average available for " + course + ".")