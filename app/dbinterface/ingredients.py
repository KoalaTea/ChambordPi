
from bson import ObjectId
from document import Document

class Ingredient(Document):
    def __init__(self, doc):
        #get our settings
        name = doc.get('name', None)
        flavor = doc.get('flavor', None)
        ing_type = doc.get('type', None)
        ing_class = doc.get('class', None)
        measure = doc.get('measure', None)
        stock = doc.get('stock', 0)

        #create the document dictionary
        ingredient_doc = {
                'name': name,
                'flavor': flavor,
                'type': ing_type,
                'class': ing_class,
                'measure': measure,
                'stock': stock
        }


        #create the Document object
        super(Ingredient, self).__init__('Ingredients', ingredient_doc)

    def update_stock(amount):
        #add/remove bottles
        self.stock += stock
        self.commit()

    @staticmethod
    def create_ingredient(name, flavor, ing_type, ing_class, measure, **kwargs):
        #merge the two dictionaries
        kwargs.update({"name": name, "flavor": flavor, "type": ing_type, "class": ing_class, "measure": measure})
        newing = Ingredient(kwargs)
        return newing

    @staticmethod
    def get_available():
        #Ingregient.get()?
        return self.get({'available':True})

    @staticmethod
    def get(search={}):
        return [ i for i in Document.get('Ingredients', search) ]
