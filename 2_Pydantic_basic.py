from pydantic import BaseModel

class Patient(BaseModel): 
    name:str
    age:int

def insert_patient(patient:Patient): 
    print(patient.name)
    print(patient.age)
    print('inserted')


record={'name':'pankaj', 'age':'thirty'}

patient1=Patient(**record)

insert_patient(patient1)

