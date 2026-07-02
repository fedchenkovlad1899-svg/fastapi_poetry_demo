from fastapi import FastAPI
from src.core.router import router

app = FastAPI()


app.include_router(router)

# class ItemPart(BaseModel):
#     name: str
#     description: str
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     parts: list[ItemPart] | None = None
#
# item_parts = [
#     {
#         "name": "part1",
#         "description": "description1",
#     },
#     {
#         "name": "part2",
#         "description": "description2",
#     }
# ]


# @app.post("/items/")
# def create_item(item: Item):
#     item_part_obj = []
#     for items in item_parts:
#         item_part_obj.append(ItemPart(**items))
#         item.parts = item_part_obj
#     return item

# def query_depends(skip: str, limit: int=10):
#     return {"skip": skip, "limit":limit}
#
# @app.get("/items/")
# def read_item(paginate = Depends(query_depends)):
#     return paginate