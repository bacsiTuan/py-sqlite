#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from typing import Any, List
from sqlalchemy.orm import Session
from loguru import logger
from fastapi import APIRouter, Request, Body, File, Form, UploadFile, Depends, Header
from app.models.job_queue import Todo
from app.sqlite import engine, get_db
from pydantic import BaseModel

router = APIRouter()

# Pydantic schemas for input and output validation
class TodoCreate(BaseModel):
    title: str
    description: str = None
    completed: bool = False

class TodoRead(TodoCreate):
    id: int

    class Config:
        orm_mode = True

@router.get("/ping", status_code=200)
async def ping(header: Request) -> Any:
    return {"ping": "pong1"}

@router.post("/todos", response_model=TodoRead)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    new_todo = Todo(**todo.dict())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

# Read all to-do items
@router.get("/todos", response_model=List[TodoRead])
def read_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Todo).offset(skip).limit(limit).all()


