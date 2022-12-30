from enum import Enum
from fastapi import Body, FastAPI, Response, Query, Path
from pydantic import BaseModel

app = FastAPI()

""" 

FastAPI Tutorial Part 7 -> Body - Multiple Parameters

"""
### Use "str | None = None" meaning it is optional field.
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float 
    tax: float | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None

## this is one of the possible solution to define the class for one object (field), or use Body() function
# class Importance(BaseModel):
#    importance: int

@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=10, le=150),
    q: str | None = None,
    item: Item | None = None,
    user: User,
## the following is the alternate function to use "Body()" to define a specific field instead of use "class".
    importance: int = Body(...)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    if user:
        results.update({"user": user})
    if importance:
        results.update({"importance": importance})
    return results
