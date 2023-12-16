from models.modelProducts import product as ProductModel
from schemas.schemaProducts import Product

class ProductService():
    def __init__(self, db) -> None:
        self.db = db

    def get_products(self):
        result = self.db.query(ProductModel).all()
        return result

    def get_product(self, id:int):
        result = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        return result

    def create_product(self, product:Product):
        new_product = ProductModel(**product.model_dump())
        self.db.add(new_product)
        self.db.commit()

    def update_product(self, id:int, data:Product):
        product = self.get_product(id)
        product.name = data.name
        product.description  = data.description
        product.units = data.units
        self.db.commit()

    def delete_product(self, id:int):
        product = self.get_product(id)
        self.db.delete(product)
        self.db.commit()