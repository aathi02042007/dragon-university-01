from pydantic import BaseModel,EmailStr,Field
from datetime import date
import decimal



# addmission values get pana
class AdmissionRequestSchema(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    Email: EmailStr
    Phone: str = Field(min_length=10, max_length=15)
    DOB: date
    Gender: str

    HSC_Group: str
    HSC_Percentage: decimal.Decimal = Field(ge=0, le=100)
    School_Name: str
    Passing_Year: int

    department_id: int
    course:str

class AdmissionResponseSchema(BaseModel):
    status:str



