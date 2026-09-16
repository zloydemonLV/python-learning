from practice.database import SessionLocal
from practice.models import Product
from sqlalchemy import select



def get_product_by_name(product_name):
   db = SessionLocal()
   product = db.scalars(
       select(Product).where(Product.name.ilike(product_name))
   ).first()

   db.close()


   return product



def get_all_products():
    db = SessionLocal()

    products = db.scalars(select(Product)).all()
    db.close()

    return products


def create_product(name, price, stock):
   db=SessionLocal()

   existing_product = db.scalars(
       select(Product).where(Product.name.ilike(name))
   ).first()

   if existing_product:
       db.close()
       return None


   new_product = Product(name=name, price=price, stock=stock)
   db.add(new_product)
   db.commit()
   db.refresh(new_product)

   db.close()

   return new_product

def update_product(product_name, price, stock):
   db = SessionLocal()

   product = db.scalars(
       select(Product).where(Product.name.ilike(product_name))
   ).first()

   if product is None:
       db.close()
       return None

   product.price = price
   product.stock = stock

   db.commit()
   db.refresh(product)

   db.close()
   return product

def delete_product(product_name):
    db = SessionLocal()

    product = db.scalars(
        select(Product).where(Product.name.ilike(product_name))
    ).first()

    if product is None:
        db.close()
        return False

    db.delete(product)
    db.commit()
    db.close()

    return True


