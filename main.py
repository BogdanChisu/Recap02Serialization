"""
WHAT IS SERIALIZATION?

Objects, variables, data in the program are volatile i.e. they are stored in the RAM memory only. After switching off
the computer they will disappear. Serialization is about saving an existing object to permanent memory - either a file
or a database, etc.

THE PICKLE MODULE

The easiest way to serialize is to use the pickle module. It transforms any object into a series of bytes. This byte
stream can be transferred or saved and later reconstructed to create a new object with the same properties.

e.g.
"""
# import pickle
# data = {
#     'a' : [1, 2.0, 3, 4+6j],
#     'b' : ("Alice has a cat", "Python programming is great"),
#     'c' : ['False', 'True', 'False']
# }
#
# with open('data.pickle', 'wb') as f:
#     pickle.dump(data, f)

"""
DESERIALIZATION EXAMPLE
"""

# import pickle
# data = {
#     'a' : [1, 2, 3, 4,],
#     'b' : ("Alice has a cat", "Python programming is great"),
#     'c' : ["False", "True", "False"]
# }
#
# with open('data.pickle', 'rb') as f:
#     data = pickle.load(f)
# print(data)

"""
-------------------------------------
CSV
-------------------------------------
Another file format to which we can save data in Python is CSV (comma-separated-values). This is a format for storing 
data in text files

e.g. Reading a csv file
"""
import csv

with open("employees.csv") as in_file:
    reader = csv.reader(in_file)
    for row in reader:
        print(row)
"""
To be able to process CSV files, we must use the csv module. We use the open function to open and access the
employees.csv file, then create a csv.reader object that allows us to iterate through the contents of that file line by
line.
"""
# import csv
with open("employees.csv", "a") as out_file:
    writer = csv.writer(out_file)
    writer.writerow(["Jenniffer Lawrence", "65000"])

"""
-------------------------------------
JSON
-------------------------------------
JSON (Javascript Object Notation) is another way to store and transmit text data. Often used for communication and 
transmit text data. Often used for communication and information transfer when creating and using web APIs (for instance
in the REST standard).
-------------------------------------
READING FROM A JSON FILE
"""
import json
with open("animals.json") as in_file:
    data = json.load(in_file)

print("Before pretty printing.")
print(data["dogs"])
print("After pretty printing")
data_pretty = json.dumps(data, indent=2)
print(data_pretty)

"""
-------------------------------------
WRITING TO A JSON FILE
"""
students =[
    {
        'name': 'John',
        'surname': 'Smith',
        'score': 20
    },
    {
        'name': 'Kevin',
        'surname': 'Scoot',
        'score': 17
    }
]
with open("students.json", "w") as out_file:
    json.dump(students, out_file, indent=2)