

name=input("Enter the student's name: ")
modified_name=name.strip().lower()
dict={'alice':100,'harsh':99,'harry':100,}
b=dict.keys()
if modified_name not in b:
  print('student not found')
else:
  marks=dict[modified_name]
  print(f"{modified_name}'s marks:{marks}")
