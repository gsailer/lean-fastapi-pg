from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .schemas.example import Example
from .models.example import ExampleModel

router = APIRouter()


@router.get("/")
def read_examples(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
) -> List[Example]:
    db_examples = db.query(ExampleModel).offset(skip).limit(limit).all()
    if db_examples is None:
        raise HTTPException(status_code=404, detail="No examples found.")
    return db_examples


@router.get("/{example_id}")
def read_example(example_id: str, db: Session = Depends(get_db)) -> Example:
    db_example = db.query(ExampleModel).filter(ExampleModel.id == example_id).first()
    if db_example is None:
        raise HTTPException(status_code=404, detail="Example not found.")
    return db_example


@router.post("/", status_code=201)
def create_example(example: Example, db: Session = Depends(get_db)) -> Example:
    existing_example = db.query(ExampleModel).filter(ExampleModel.id == example.id).first()
    if existing_example:
        raise HTTPException(status_code=400, detail="Example with id already exists.")
    db_example = ExampleModel(**example.dict())
    db.add(db_example)
    db.commit()
    db.refresh(db_example)
    return db_example
