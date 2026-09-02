from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from practice.utils import load_products, save_products

class ProductCreate(BaseModel):
    name: str
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

    new_product = {
        "name": product.name,
        "price": product.price,
        "stock": product.stock,
    }
    products.append(new_product)
    save_products(products)

    return new_product


