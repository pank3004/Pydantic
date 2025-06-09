from pydantic import BaseModel

class Patient(BaseModel):    # Even though you didn't write a constructor (__init__()), the BaseModel from Pydantic automatically creates one behind the scenes — and it includes type validation, parsing, and error handling.
    name:str 
    age:int

def insert_patient(patient:Patient): 
    print(patient.name)
    print(patient.age)
    print('inserted')


record={'name':'pankaj', 'age':'thirty'}

patient1=Patient(**record)

insert_patient(patient1)

