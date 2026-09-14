from practice.service import get_product_by_name

product = get_product_by_name("Cola")

if product:
    print(product.id, product.name, product.price, product.stock)
else:
    print("Product not found")