from sqlalchemy import Column, Integer, String

from ...database import Base


class ExampleModel(Base):
    __tablename__ = "examples"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    comment = Column(String, nullable=True)
