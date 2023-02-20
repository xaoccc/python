class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []
        
    def __repr__(self):
        output = '\n'.join(sorted(self.products))
        return f"Items in the {self.name} catalogue: {output}"
        
    def add_product(self, product_name):
        self.products.append(str(product_name))
        
    def get_by_letter(self, first_letter):
        return [x for x in self.products if x.startswith(first_letter)]
            
        
#test code        
name = input()        
catalogue = Catalogue(name)
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
    
print(catalogue)
print(catalogue.get_by_letter(input()))
