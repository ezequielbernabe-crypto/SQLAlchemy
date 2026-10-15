from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tutorial.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price}, stock={self.stock})>"

def init_db():
    with app.app_context():
        db.create_all()
        print("Base de datos creada satisfactoriamente")

def insert_products():
    with app.app_context():

        productos = [
            Product(name="Teclado", price=120.50, stock=10),
            Product(name="Mouse", price=45.00, stock=20),
            Product(name="Cable USB", price=15.00)
        ]

        for producto in productos:
            existente = Product.query.filter_by(
                name=producto.name
            ).first()

            if not existente:
                db.session.add(producto)

        db.session.commit()
        print("Productos registrados correctamente")

def query_products():
    with app.app_context():

        print("\nLISTADO DE PRODUCTOS")

        productos = Product.query.all()

        for item in productos:
            print(item)

if __name__ == "__main__":

    #init_db()
    #insert_products()
    #query_products()
