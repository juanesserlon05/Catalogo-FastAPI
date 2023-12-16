from fastapi import APIRouter, Path, Query, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from models.modelProducts import product as ProductModel
from config.databaseProducts import Session
from middlewares.jwt_bearer import JWTBearer
from services.queryProducts import ProductService
from schemas.schemaProducts import Product

productRouter = APIRouter()


@productRouter.get("/Products", tags=['Read products'], response_model=List[Product],
                  status_code=200)
def get_products() -> List[Product]:
    result = ProductService(Session()).get_products()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@productRouter.get("/Products/{id}", tags=['Read product'], response_model=Product,
                  status_code=200)
# se cambia y se dice que es igual a Path(int)
def get_product(id: int = Path(ge=1, le=2000)) -> Product:
    result = ProductService(Session()).get_product(id)
    if not result:
        return JSONResponse(status_code=404, content={
            "message": "Product not found"
            })
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@productRouter.post("/Products", tags=['Create a product'], response_model=dict, status_code=201)
def create_product(product: Product) -> dict:
    ProductService(Session()).create_product(product)
    return JSONResponse(content={"message": "Product created successfully"}, status_code=201)


@productRouter.put("/Products/{id}", tags=['Update product'], response_model=dict, status_code=200)
def update_product(id: int, product: Product) -> dict:
    if not ProductService(Session()).get_product(id):
        return JSONResponse(content={"message": "Product not found"}, status_code=404)
    ProductService(ProductService(Session()).get_product(id)).update_product(id, product)
    return JSONResponse(content={"message": "Product updated successfully"}, status_code=200)


@productRouter.delete("/Products/{id}", tags=['Delete Products'], response_model=dict)
def delete_product(id: int) -> dict:
    if not ProductService(Session()).get_product(id):
        return JSONResponse(content={"message": "Product not found"}, status_code=404)
    ProductService(Session()).delete_product(id)
    return JSONResponse(content={"message": "Product deleted successfully"})