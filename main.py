from enum import Enum
from fastapi import Body, FastAPI, Response, Query, Path
from pydantic import BaseModel, Field

app = FastAPI()

""" 

FastAPI Tutorial Part 8 -> Body - Fields

"""

class Item(BaseModel):
    name: str
    description: str | None = Field(None, title="The dscription of the item", max_length=300)
    price: float = Field(gt=0, description="The price must greater than ZERO.")
    tax: float | None = None

@app.put("/items/{item_id}")
## with the "embed=True", it will carry the Item as key & value pair. Otherwise, it will not like with the class object.
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item": item_id}
    return results