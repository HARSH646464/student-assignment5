# student-assignment5
```# Student Marks Finder

This is a simple Python program that allows you to look up a student's marks from a predefined dictionary.

## 📌 Features
- Accepts user input for a student’s name.  
- Strips leading/trailing spaces and converts the name to lowercase for consistency.  
- Searches for the student in the dictionary.  
- Prints the student’s marks if found, otherwise notifies that the student is not found.  

## 🖥️ Code

```python
# Student Marks Finder

# Input student name
name = input("Enter the student's name: ")

# Normalize input
modified_name = name.strip().lower()

# Predefined student dictionary
students = {
    'alice': 100,
    'harsh': 99,
    'harry': 100,
}

# Check if student exists
if modified_name not in students:
    print('Student not found')
else:
    marks = students[modified_name]
    print(f"{modified_name}'s marks: {marks}")
```
```
