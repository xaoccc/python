from project.product import Product

class ProductRepository:
    def __init__(self):
        self.products = []
        
    def add(self, product: Product):
        self.products.append(product)
    
    def remove(self, product_name: str):
        for p in self.products:
            if p.name == product_name:
                self.products.remove(p)
                
    def find(self, product_name: str):
        for p in self.products:
            if p.name == product_name:
                return p
                
    def __repr__(self):
        result = []
        for p in self.products:
            result.append(f"{p.name}: {p.quantity}")
        return "\n".join(result)
  
