from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from practice.utils import load_products, save_products

class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: int = Field(ge=0)
    stock: int = Field(ge=0)

class ProductUpdate(BaseModel):
    price: int
    stock: int





app = FastAPI()

@app.get("/")
def root():
    return {"message": "Inventory API is running"}

@app.get("/products")
def get_products():
    products = load_products()

    return products

@app.get("/products/{product_name}")
def get_product(product_name: str):
    products = load_products()

    for product in products:
        if product["name"].lower() == product_name.lower():
            return product

    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/products")
def create_product(product: ProductCreate):
    products = load_products()

    for existing_product in products:
        if existing_product["name"].lower == product.name.lower():
            raise HTTPException(
                status_code=400,
                detail="Product name already exists",

             )

        new_product = {
        "name": product.name,
        "price": product.price,
        "stock": product.stock,
    }
        products.append(new_product)
        save_products(products)

        return new_product


@app.put("/products/{product_name}")
def update_product(product_name: str, product: ProductUpdate):
    products = load_products()
    for existing_product in products:
        if existing_product["name"].lower() == product_name.lower():
            existing_product["price"] = product.price
            existing_product["stock"] = product.stock

            save_products(products)
            return existing_product

    raise HTTPException(status_code=404, detail="Product not found")