from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Arabicfood(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    title = db.Column(db.String(250)) 
    description = db.Column(db.Text)   
    picture = db.Column(db.String(500))
    ingredients = db.Column(db.String(1000)) 

    def __init__(self, title, description, picture, ingredients,id):
        self.title = title
        self.description = description
        self.picture = picture
        self.ingredients = ingredients
        self.id=id
class Juice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    description = db.Column(db.Text)
    picture = db.Column(db.String(500))
    ingredients = db.Column(db.String(1000))

    def __init__(self, title, description, picture, ingredients, id):
        self.title = title
        self.description = description
        self.picture = picture
        self.ingredients = ingredients
        self.id = id
class Sauce(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    description = db.Column(db.Text)
    picture = db.Column(db.String(500))
    ingredients = db.Column(db.String(1000))
    def __init__(self, title, description, picture, ingredients, id):
        self.title = title
        self.description = description
        self.picture = picture
        self.ingredients = ingredients
        self.id = id
class Salade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    description = db.Column(db.Text)
    picture = db.Column(db.String(500))
    ingredients = db.Column(db.String(1000))
    def __init__(self, title, description, picture, ingredients, id):
        self.title = title
        self.description = description
        self.picture = picture
        self.ingredients = ingredients
        self.id = id
class Icecream(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    description = db.Column(db.Text)
    picture = db.Column(db.String(500))
    ingredients = db.Column(db.String(1000))
    def __init__(self, title, description, picture, ingredients, id):
        self.title = title
        self.description = description
        self.picture = picture
        self.ingredients = ingredients
        self.id = id
class Sweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    description = db.Column(db.Text)
    picture = db.Column(db.String(500))
    ingredients = db.Column(db.String(1000))
    def __init__(self, title, description, picture, ingredients, id):
        self.title = title
        self.description = description
        self.picture = picture
        self.ingredients = ingredients
        self.id = id
class Asianfood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    description = db.Column(db.Text)
    picture = db.Column(db.String(500))
    ingredients = db.Column(db.String(1000))

    def __init__(self, title, description, picture, ingredients,id):
        self.title = title
        self.description = description
        self.picture = picture
        self.ingredients = ingredients
        self.id=id
class Africanfood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    description = db.Column(db.Text)
    picture = db.Column(db.String(500))
    ingredients = db.Column(db.String(1000))

    def __init__(self, title, description, picture, ingredients,id):
        self.title = title
        self.description = description
        self.picture = picture
        self.ingredients = ingredients
        self.id=id
class Europeanfood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    description = db.Column(db.Text)
    picture = db.Column(db.String(500))
    ingredients = db.Column(db.String(1000))
    

    def __init__(self, title, description, picture, ingredients,id):
        self.title = title
        self.description = description
        self.picture = picture
        self.ingredients = ingredients
        self.id=id
class Americanfood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    description = db.Column(db.Text)
    picture = db.Column(db.String(500))
    ingredients = db.Column(db.String(1000))

    def __init__(self, title, description, picture, ingredients,id):
        self.title = title
        self.description = description
        self.picture = picture
        self.ingredients = ingredients
        self.id=id
