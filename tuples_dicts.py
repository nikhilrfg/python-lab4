# Create a tuple containing the twelve months.
months = (
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
)

# Print the first and last month.
print("First month: " + months[0])
print("Last month: " + months[-1])

# Try to modify the tuple.
try:
    months[0] = "NewMonth"
except TypeError as error:
    print("Tuples are immutable, error: " + str(error))


# Create a dictionary of students and grades.
students = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 78
}

# Add a new student.
students["David"] = 88

print("Students and grades:")

for name, grade in students.items():
    print(name + ": " + str(grade))


# Update an existing student's grade.
students["Bob"] = 92

print("Updated Bob's grade:")
print("Bob: " + str(students["Bob"]))


# Print all students again.
print("Updated student list:")

for name, grade in students.items():
    print(name + ": " + str(grade))