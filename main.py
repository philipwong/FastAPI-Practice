from enum import Enum
from fastapi import Body, FastAPI, Response, Query, Path
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()

""" 

FastAPI Tutorial Part 10 -> Declare Request Example Data

"""