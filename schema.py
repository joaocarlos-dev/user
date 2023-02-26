
from typing import Optional
from pydantic import BaseModel, EmailStr, validator

class UserBase(BaseModel):
    name: str
    email: EmailStr
    cpf: str
    pis: str
    password: str
    country: str 
    state:str
    city: str
    street: str
    number: int
    complement: str

    @validator('pis')
    def validate_pis(cls, pis):
        pis_digits = [int(digit) for digit in pis if digit.isdigit()]
        if len(pis_digits) != 11:
            raise ValueError("PIS must have 11 digits")
        return pis
    
    @validator('cpf')
    def validate_cpf(cls, cpf):
        cpf_digits = [int(digit) for digit in cpf if digit.isdigit()]
        if len(cpf_digits) != 11:
            raise ValueError("CPF must have 11 digits")
        return cpf


class UserAdd(UserBase):
    user_id: str    
    
    class Config:
        orm_mode = True


class User(UserAdd):
    id: int
   
    class Config:
        orm_mode = True


class UpdateUser(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    cpf: Optional[str] = None
    pis: Optional[str] = None
    password: Optional[str] = None

    class Config:
        orm_mode = True