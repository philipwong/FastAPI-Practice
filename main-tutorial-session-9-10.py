from enum import Enum
from fastapi import Body, FastAPI, Response, Query, Path
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()

""" 

FastAPI Tutorial Part 8 -> Body - Fields

"""

# class Item(BaseModel):
#     name: str
#     description: str | None = Field(None, title="The dscription of the item", max_length=300)
#     price: float = Field(gt=0, description="The price must greater than ZERO.")
#     tax: float | None = None

# @app.put("/items/{item_id}")
# ## with the "embed=True", it will carry the Item as key & value pair. Otherwise, it will not like with the class object.
# async def update_item(item_id: int, item: Item = Body(..., embed=True)):
#     results = {"item": item_id}
#     return results

""" 

FastAPI Tutorial Part 9 -> Body - Nested Models

"""

class Image(BaseModel):
## when use regex, it shall use "  r'^{put regex here}$'  " such syntax will declare the regex properly in python.
## is it easily to get regex in ihateregex.io
#    url: str = Field(..., regex=r'^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)$')

## if using regex is too complicated, it can use pydantic "HttpUrl" module instead.
    url: HttpUrl
    name: str

## this is the nested models, the "Item" include another data model "Image"
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
## this only allow after python 3.10, otherwise must import "typing" module
    # tags: list[str] = []
## the following use "set", it will deduplicate (nested) the input automatically.
    tags: set[str] = []
    image: list[Image] | None = None

class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    item: list[Item]

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

@app.post("/offers")
async def create_offer(offer: Offer = Body(..., embed=True)):
    return offer

@app.post("/images")
async def create_multiple_images(images: list[Image] = Body(..., embed=True)):
    return images

## this shows how flexiable the model can be
@app.post("/blah")
async def create_some_blahs(blahs: dict[int, float]):
    return blahs