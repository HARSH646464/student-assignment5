# student-assignment5
``` Student Marks Finder

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
```# 🔄 List Extraction and Reversal

This Python program demonstrates how to:  
1. Create a list of numbers.  
2. Extract the first five elements.  
3. Reverse the extracted list.  

## 📌 Code

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Extract first 5 elements
extracted_list = numbers[0:5]

# Reverse extracted elements
reversed_extracted_list = extracted_list[::-1]

# Print results
print('Original list: ', numbers)
print("Extracted first five elements: ", extracted_list)
print('Reversed extracted elements: ', reversed_extracted_list)

