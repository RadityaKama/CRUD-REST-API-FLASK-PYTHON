from app import db

class Category(db.Model):
    __tablename__ = 'category_product' 
    
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    
    products = db.relationship('Product', backref='category', lazy=True)

    def __repr__(self):
        return '<Category {}>'.format(self.name)