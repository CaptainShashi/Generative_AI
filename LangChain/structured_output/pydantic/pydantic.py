from pydantic import BaseModel, EmailStr,Field
from typing import Optional


class Student(BaseModel):
    name:str
    age:Optional[int]=None      # if no value is given None is default
    price:int
    email:EmailStr
    cgpa:float=Field(gt=0,ld=10 , default=7 , description="decimal value")   # gt=greater than, ld=less than


new_student={"name":"shashi","price":'2000'}   # pydantic can identify '2000' and 2000 and convert '2000' as 2000

student=Student(**new_student)
print(student)