from typing import TypedDict

class person(TypedDict):
    name : str
    age : int

new_person:person={"name":"shashi", "age":'23'}  # it will take both '23' and 23 in int place 
print(new_person)