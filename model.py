from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from pydantic import BaseModel

Base = declarative_base()



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    tech_stack = Column(String)
    link = Column (String, nullable=True)
    owner_id = Column(Integer, ForeignKey("user.id"))

    owner = relationship("User")

class ProjectCreate(BaseModel):
    title : str
    description : str
    tech_stack : str
    link: str| None= None

class ProjectOut(BaseModel):
    id : int
    title : str
    description :str
    tech_stack : str
    link: str | None= None
    owner_id: int

    class Config:
        from_attributes = True