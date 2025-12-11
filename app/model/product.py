from app import db

class Product(db.Model):
    __tablename__ = 'product'
    
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    harga = db.Column(db.Float, nullable=False) 
    
    description = db.Column(db.Text, nullable=True)
    category_id = db.Column(db.BigInteger, db.ForeignKey('category_product.id'), nullable=False)

    def __repr__(self):
        return '<Product {}>'.format(self.name)