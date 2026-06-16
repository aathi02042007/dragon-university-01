from sqlalchemy import Column, column,integer,string
from app.database.base import base

class Departmenrt(base):
    __tablename__="departments"
    id=column(integer,primary_key=true,index=true)
    department_name = Column(String(100), nullable=False)