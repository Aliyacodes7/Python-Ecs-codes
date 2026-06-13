#Code for adding and updating a dictionary 
#Coder:Aliya Shaikh

from pprint import pprint

record={
    "251S015": {"name":"vernon", "grade":"A", "attendance":"85"},
    "251S016": {"name":"Aliya", "grade":"A+", "attendance":"90"},
    "251S017": {"name":"lisa", "grade":"A-", "attendance":"80"}
}

print("Original record:")
pprint(record)

#Add new student record
UIN=input("\nenter the UIN: ")
name=input("enter the name: ")
grade=input("enter the grade: ")
attendance=input("enter the attendance: ")
record[UIN]={"name":name, "grade":grade, "attendance":attendance}

print("\nRecord after adding:")
pprint(record)

#update student record
UIN=input("\nenter the UIN of the student to update: ")
if UIN in record:
    name=input("enter the new name: ")
    grade=input("enter the new grade: ")
    attendance=input("enter the new attendance: ")
    record[UIN]={"name":name, "grade":grade, "attendance":attendance}
    print("\nRecord after updating:")
    pprint(record)
else:
    print(f"\nStudent with UIN {UIN} not found.")

"""
SAMPLE OUTPUT:
Original record:
{'251S015': {'attendance': '85', 'grade': 'A', 'name': 'vernon'},
 '251S016': {'attendance': '90', 'grade': 'A+', 'name': 'Aliya'},
 '251S017': {'attendance': '80', 'grade': 'A-', 'name': 'lisa'}}

enter the UIN: 251S018
enter the name: elizabeth
enter the grade: B
enter the attendance: 75

Record after adding:
{'251S015': {'attendance': '85', 'grade': 'A', 'name': 'vernon'},
 '251S016': {'attendance': '90', 'grade': 'A+', 'name': 'Aliya'},
 '251S017': {'attendance': '80', 'grade': 'A-', 'name': 'lisa'},
 '251S018': {'attendance': '75', 'grade': 'B', 'name': 'elizabeth'}}

enter the UIN of the student to update: 251S017
enter the new name: mina
enter the new grade: B+
enter the new attendance: 70

Record after updating:
{'251S015': {'attendance': '85', 'grade': 'A', 'name': 'vernon'},
 '251S016': {'attendance': '90', 'grade': 'A+', 'name': 'Aliya'},
 '251S017': {'attendance': '70', 'grade': 'B+', 'name': 'mina'},
 '251S018': {'attendance': '75', 'grade': 'B', 'name': 'elizabeth'}}
"""
