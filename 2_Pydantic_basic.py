from pydantic import BaseModel

# step 1 define pydantic class
         # include fields, types, validation constaints(eg gt=0)
         # Even though you didn't write a constructor (__init__()), the BaseModel from Pydantic automatically creates one behind the scenes — and it includes type validation, parsing, and error handling.
class Patient(BaseModel):    
    name:str 
    age:int

def insert_patient(patient:Patient): 
    print(patient.name)
    print(patient.age)
    print('inserted')


record={'name':'pankaj', 'age':'thirty'}
# step 2 instantiate the class with row input data(usually dictonary or json)
         # pydantic autumatic validate (if data doest't meet model's req then raise validation error)
patient1=Patient(**record)

# step 3 pass the validated object to the function
         # ensoures every part of program works clean, type-safe and logically valid data
insert_patient(patient1)

