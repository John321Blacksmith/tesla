from typing import Union
from fastapi import FastAPI
from engine.central_manager import Manager
from memory.datasets import categories

app = FastAPI()
manager = Manager(source=categories)


@app.get('/{text}')
async def classify(text: str):
    manager.process_input(text)
    result = manager.get_main_context()
    return {"message": "Success", "result": result}