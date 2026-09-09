from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from practice.service import (
    get_all_products,
    get_product_by_name,
    create_product as create_product_service,
    update_product as update_product_service,
    delete_product as delete_product_service,
)


class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: int = Field(ge=0)
    stock: int = Field(ge=0)

class ProductUpdate(BaseModel):
    price: int
    stock: int

class ProductResponse(BaseModel):
    name:str
    price:int
    stock:int

class MessageResponse(BaseModel):
    message:str




app = FastAPI()

@app.get("/")
def root():
    return {"message": "Inventory API is running"}

@app.get("/products", response_model=list[ProductResponse])
def get_products():
    return get_all_products()

@app.get(
    "/products/{product_name}",
    response_model=ProductResponse
)
def get_product(product_name: str):
    products = get_product_by_name(product_name)

    if products is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return products

@app.post("/products", response_model=ProductResponse)
def create_product(product: ProductCreate):
    new_product = create_product_service(
        product.name,
        product.price,
        product.stock,
    )
    if new_product is None:
        raise HTTPException(
            status_code=400,
            detail="Product name already exists",
        )
    return new_product


@app.put(
    "/products/{product_name}",
        response_model=ProductResponse
)
def update_product(product_name: str, product: ProductUpdate):
    updated_product = update_product_service(
        product_name,
        product.price,
        product.stock,
    )
    if updated_product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )
    return updated_product

@app.delete(
    "/products/{product_name}",
        response_model=MessageResponse
)
def delete_product(product_name: str):
    deleted = delete_product_service(product_name)

    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")

    return{"message": "Product deleted"}