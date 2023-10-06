from flask import jsonify, request, Response
from model import db,Juice,Icecream,Salade,Sweet,Sauce,Asianfood,Americanfood,Africanfood,Europeanfood,Arabicfood
from schema import JuiceSchema,ArabicfoodSchema
from flask_babel import _
import json

arabicfood_schema = ArabicfoodSchema()
arabicfoods_schema = ArabicfoodSchema(many=True)

def add_get_arabicfoods():
    if request.method == "POST":
       
        arabicfood_id = request.json.get("id")
        arabicfoods_title = request.json.get("title")
        arabicfoods_description = request.json.get("description")
        arabicfoods_picture = request.json.get("picture")
        arabicfoods_ingredients = request.json.get("ingredients")
        
        
        existing_arabicfood = Arabicfood.query.get(arabicfood_id)

        if existing_arabicfood:
            existing_arabicfood.title = arabicfoods_title
            existing_arabicfood.description = arabicfoods_description
            existing_arabicfood.picture = arabicfoods_picture
            existing_arabicfood.ingredients = arabicfoods_ingredients
        else:
            
            new_arabicfood = Arabicfood(
                id=arabicfood_id,  
                title=arabicfoods_title,
                description=arabicfoods_description,
                picture=arabicfoods_picture,
                ingredients=arabicfoods_ingredients,
            )
            db.session.add(new_arabicfood)

        db.session.commit()

        response_data = {
            "message": "created succefuly",
        }
        json_data = json.dumps(response_data, ensure_ascii=False)
        response = Response(json_data, content_type='application/json; charset=utf-8')
        return response, 201

    
    arabicfoods_list = Arabicfood.query.all()
    arabicfoods = []

    for arabicfood in arabicfoods_list:
        arabicfoods.append({
            "title": arabicfood.title,
            "description": arabicfood.description,
            "picture": arabicfood.picture,
            "ingredients": arabicfood.ingredients,
            
        })

    
    response_data = {"arabicfoods": arabicfoods}
    json_data = json.dumps(response_data, ensure_ascii=False)
    response = Response(json_data, content_type='application/json; charset=utf-8')
    return response


def update_arabicfoods(arabicfood_id):
    
    arabicfoods_title = request.json["title"]
    arabicfoods_description = request.json.get("description")
    arabicfoods_picture = request.json.get("picture")
    arabicfoods_ingredients = request.json.get("ingredients")

    arabicfood = Arabicfood.query.get(arabicfood_id)

    if not arabicfood:
        
        return jsonify({"message": "Arabicfood not found"}), 404

    
    arabicfood.title = arabicfoods_title
    arabicfood.description = arabicfoods_description
    arabicfood.picture = arabicfoods_picture
    arabicfood.ingredients = arabicfoods_ingredients

    
    db.session.commit()

    
    return jsonify({"message": "update succefuly"}), 200


 
def get_arabicfoods(arabicfood_id):
    arabicfood = Arabicfood.query.get(arabicfood_id)
    if arabicfood:
         
        return jsonify({
            "title": arabicfood.title,
            "description": arabicfood.description,
            "picture": arabicfood.picture,
            "ingredients": arabicfood.ingredients,
            
        })


def delete_arabicfoods(arabicfood_id):
    arabicfood = Arabicfood.query.get(arabicfood_id)
    if arabicfood:
        
        db.session.delete(arabicfood)
        db.session.commit()
        return jsonify({"message": "delete succefuly"}), 200
juice_schema = JuiceSchema()
juices_schema = JuiceSchema(many=True)



def add_get_juices():
    if request.method == "POST":
        juice_id = request.json.get("id")
        juices_title = request.json.get("title")
        juices_description = request.json.get("description")
        juices_ingredients = request.json.get("ingredients")
        juices_picture = request.json.get("picture")

        existing_juice = Juice.query.get(juice_id)

        if existing_juice:
            existing_juice.title = juices_title
            existing_juice.description = juices_description
            existing_juice.ingredients = juices_ingredients
            existing_juice.picture = juices_picture
        else:
            new_juice = Juice(
                id=juice_id,
                title=juices_title,
                description=juices_description,
                ingredients=juices_ingredients,
                picture=juices_picture
            )
            db.session.add(new_juice)

        db.session.commit()

        response_data = {
            "message": "Juice created successfully",
        }
        json_data = json.dumps(response_data, ensure_ascii=False)
        response = Response(json_data, content_type='application/json; charset=utf-8')
        return response, 201

    juices_list = Juice.query.all()
    juices = []

    for juice in juices_list:
        juices.append({
            "title": juice.title,
            "description": juice.description,
            "ingredients": juice.ingredients,
            "picture": juice.picture
        })

    response_data = {"juices": juices}
    json_data = json.dumps(response_data, ensure_ascii=False)
    response = Response(json_data, content_type='application/json; charset=utf-8')
    return response

def update_juices(juice_id):
    juices_title = request.json.get("title")
    juices_description = request.json.get("description")
    juices_ingredients = request.json.get("ingredients")
    juices_picture = request.json.get("picture")

    juice = Juice.query.get(juice_id)

    if not juice:
        return jsonify({"message": "Juice not found"}), 404

    juice.title = juices_title
    juice.description = juices_description
    juice.ingredients = juices_ingredients
    juice.picture = juices_picture

    db.session.commit()

    return jsonify({"message": "Juice updated successfully"}), 200

def get_juices(juice_id):
    juice = Juice.query.get(juice_id)

    if juice:
        return jsonify({
            "title": juice.title,
            "description": juice.description,
            "ingredients": juice.ingredients,
            "picture": juice.picture
        })
    else:
        return jsonify({"message": "Juice not found"}), 404

def delete_juices(juice_id):
    juice = Juice.query.get(juice_id)

    if juice:
        db.session.delete(juice)
        db.session.commit()
        return jsonify({"message": "Juice deleted successfully"}), 200
    else:
        return jsonify({"message": "Juice not found"}), 404
def add_get_sauces():
    if request.method == "POST":
       
        sauce_id = request.json.get("id")
        sauces_title = request.json.get("title")
        sauces_description = request.json.get("description")
        sauces_picture = request.json.get("picture")
        sauces_ingredients = request.json.get("ingredients")
        
        
        existing_sauce = Sauce.query.get(sauce_id)

        if existing_sauce:
            existing_sauce.title = sauces_title
            existing_sauce.description = sauces_description
            existing_sauce.picture = sauces_picture
            existing_sauce.ingredients = sauces_ingredients
        else:
            
            new_sauce = Sauce(
                id=sauce_id,  
                title=sauces_title,
                description=sauces_description,
                picture=sauces_picture,
                ingredients=sauces_ingredients,
            )
            db.session.add(new_sauce)

        db.session.commit()

        response_data = {
            "message": "created succefuly",
        }
        json_data = json.dumps(response_data, ensure_ascii=False)
        response = Response(json_data, content_type='application/json; charset=utf-8')
        return response, 201

    
    sauces_list = Sauce.query.all()
    sauces = []

    for sauce in sauces_list:
        sauces.append({
            "title": sauce.title,
            "description": sauce.description,
            "picture": sauce.picture,
            "ingredients": sauce.ingredients,
            
        })

    
    response_data = {"sauces": sauces}
    json_data = json.dumps(response_data, ensure_ascii=False)
    response = Response(json_data, content_type='application/json; charset=utf-8')
    return response


def update_sauces(sauce_id):
    
    sauces_title = request.json["title"]
    sauces_description = request.json.get("description")
    sauces_picture = request.json.get("picture")
    sauces_ingredients = request.json.get("ingredients")

    sauce = Sauce.query.get(sauce_id)

    if not sauce:
        
        return jsonify({"message": "sauce not found"}), 404

    
    sauce.title = sauces_title
    sauce.description = sauces_description
    sauce.picture = sauces_picture
    sauce.ingredients = sauces_ingredients

    
    db.session.commit()

    
    return jsonify({"message": "update succefuly"}), 200


 
def get_sauces(sauce_id):
    sauce = Sauce.query.get(sauce_id)
    if sauce:
         
        return jsonify({
            "title": sauce.title,
            "description": sauce.description,
            "picture": sauce.picture,
            "ingredients": sauce.ingredients,
            
        })


def delete_sauces(sauce_id):
    sauce = Sauce.query.get(sauce_id)
    if sauce:
        
        db.session.delete(sauce)
        db.session.commit()
        return jsonify({"message": "delete succefuly"}), 200
def add_get_salades():
    if request.method == "POST":
       
        salade_id = request.json.get("id")
        salades_title = request.json.get("title")
        salades_description = request.json.get("description")
        salades_picture = request.json.get("picture")
        salades_ingredients = request.json.get("ingredients")
        
        
        existing_salade = Salade.query.get(salade_id)

        if existing_salade:
            existing_salade.title = salades_title
            existing_salade.description = salades_description
            existing_salade.picture = salades_picture
            existing_salade.ingredients = salades_ingredients
        else:
            
            new_salade = Salade(
                id=salade_id,  
                title=salades_title,
                description=salades_description,
                picture=salades_picture,
                ingredients=salades_ingredients,
            )
            db.session.add(new_salade)

        db.session.commit()

        response_data = {
            "message": "created succefuly",
        }
        json_data = json.dumps(response_data, ensure_ascii=False)
        response = Response(json_data, content_type='application/json; charset=utf-8')
        return response, 201

    
    salades_list = Salade.query.all()
    salades = []

    for salade in salades_list:
        salades.append({
            "title": salade.title,
            "description": salade.description,
            "picture": salade.picture,
            "ingredients": salade.ingredients,
            
        })

    
    response_data = {"salades": salades}
    json_data = json.dumps(response_data, ensure_ascii=False)
    response = Response(json_data, content_type='application/json; charset=utf-8')
    return response


def update_salades(salade_id):
    
    salades_title = request.json["title"]
    salades_description = request.json.get("description")
    salades_picture = request.json.get("picture")
    salades_ingredients = request.json.get("ingredients")

    salade = Salade.query.get(salade_id)

    if not salade:
        
        return jsonify({"message": "salade not found"}), 404

    
    salade.title = salades_title
    salade.description = salades_description
    salade.picture = salades_picture
    salade.ingredients = salades_ingredients

    
    db.session.commit()

    
    return jsonify({"message": "update succefuly"}), 200


 
def get_salades(salade_id):
    salade = salade.query.get(salade_id)
    if salade:
         
        return jsonify({
            "title": salade.title,
            "description": salade.description,
            "picture": salade.picture,
            "ingredients": salade.ingredients,
            
        })


def delete_salades(salade_id):
    salade = Salade.query.get(salade_id)
    if salade:
        
        db.session.delete(salade)
        db.session.commit()
        return jsonify({"message": "delete succefuly"}), 200
def add_get_icecreams():
    if request.method == "POST":
       
        icecream_id = request.json.get("id")
        icecreams_title = request.json.get("title")
        icecreams_description = request.json.get("description")
        icecreams_picture = request.json.get("picture")
        icecreams_ingredients = request.json.get("ingredients")
        
        
        existing_icecream = Icecream.query.get(icecream_id)

        if existing_icecream:
            existing_icecream.title = icecreams_title
            existing_icecream.description = icecreams_description
            existing_icecream.picture = icecreams_picture
            existing_icecream.ingredients = icecreams_ingredients
        else:
            
            new_icecream = Icecream(
                id=icecream_id,  
                title=icecreams_title,
                description=icecreams_description,
                picture=icecreams_picture,
                ingredients=icecreams_ingredients,
            )
            db.session.add(new_icecream)

        db.session.commit()

        response_data = {
            "message": "created succefuly",
        }
        json_data = json.dumps(response_data, ensure_ascii=False)
        response = Response(json_data, content_type='application/json; charset=utf-8')
        return response, 201

    
    icecreams_list = Icecream.query.all()
    icecreams = []

    for icecream in icecreams_list:
        icecreams.append({
            "title": icecream.title,
            "description": icecream.description,
            "picture": icecream.picture,
            "ingredients": icecream.ingredients,
            
        })

    
    response_data = {"icecreams": icecreams}
    json_data = json.dumps(response_data, ensure_ascii=False)
    response = Response(json_data, content_type='application/json; charset=utf-8')
    return response


def update_icecreams(icecream_id):
    
    icecreams_title = request.json["title"]
    icecreams_description = request.json.get("description")
    icecreams_picture = request.json.get("picture")
    icecreams_ingredients = request.json.get("ingredients")

    icecream = Icecream.query.get(icecream_id)

    if not icecream:
        
        return jsonify({"message": "icecream not found"}), 404

    
    icecream.title = icecreams_title
    icecream.description = icecreams_description
    icecream.picture = icecreams_picture
    icecream.ingredients = icecreams_ingredients

    
    db.session.commit()

    
    return jsonify({"message": "update succefuly"}), 200


 
def get_icecreams(icecream_id):
    icecream = Icecream.query.get(icecream_id)
    if icecream:
         
        return jsonify({
            "title": icecream.title,
            "description": icecream.description,
            "picture": icecream.picture,
            "ingredients": icecream.ingredients,
            
        })


def delete_icecreams(icecream_id):
    icecream = Icecream.query.get(icecream_id)
    if icecream:
        
        db.session.delete(icecream)
        db.session.commit()
        return jsonify({"message": "delete succefuly"}), 200
def add_get_sweets():
    if request.method == "POST":
       
        sweet_id = request.json.get("id")
        sweets_title = request.json.get("title")
        sweets_description = request.json.get("description")
        sweets_picture = request.json.get("picture")
        sweets_ingredients = request.json.get("ingredients")
        
        
        existing_sweet = Sweet.query.get(sweet_id)

        if existing_sweet:
            existing_sweet.title = sweets_title
            existing_sweet.description = sweets_description
            existing_sweet.picture = sweets_picture
            existing_sweet.ingredients = sweets_ingredients
        else:
            
            new_sweet = Sweet(
                id=sweet_id,  
                title=sweets_title,
                description=sweets_description,
                picture=sweets_picture,
                ingredients=sweets_ingredients,
            )
            db.session.add(new_sweet)

        db.session.commit()

        response_data = {
            "message": "created succefuly",
        }
        json_data = json.dumps(response_data, ensure_ascii=False)
        response = Response(json_data, content_type='application/json; charset=utf-8')
        return response, 201

    
    sweets_list = Sweet.query.all()
    sweets = []

    for sweet in sweets_list:
        sweets.append({
            "title": sweet.title,
            "description": sweet.description,
            "picture": sweet.picture,
            "ingredients": sweet.ingredients,
            
        })

    
    response_data = {"sweets": sweets}
    json_data = json.dumps(response_data, ensure_ascii=False)
    response = Response(json_data, content_type='application/json; charset=utf-8')
    return response


def update_sweets(sweet_id):
    
    sweets_title = request.json["title"]
    sweets_description = request.json.get("description")
    sweets_picture = request.json.get("picture")
    sweets_ingredients = request.json.get("ingredients")

    sweet = Sweet.query.get(sweet_id)

    if not sweet:
        
        return jsonify({"message": "sweet not found"}), 404

    
    sweet.title = sweets_title
    sweet.description = sweets_description
    sweet.picture = sweets_picture
    sweet.ingredients = sweets_ingredients

    
    db.session.commit()

    
    return jsonify({"message": "update succefuly"}), 200


 
def get_sweets(sweet_id):
    sweet = Sweet.query.get(sweet_id)
    if sweet:
         
        return jsonify({
            "title": sweet.title,
            "description": sweet.description,
            "picture": sweet.picture,
            "ingredients": sweet.ingredients,
            
        })


def delete_sweets(sweet_id):
    sweet = Sweet.query.get(sweet_id)
    if sweet:
        
        db.session.delete(sweet)
        db.session.commit()
        return jsonify({"message": "delete succefuly"}), 200
def add_get_asianfoods():
    if request.method == "POST":
       
        asianfood_id = request.json.get("id")
        asianfoods_title = request.json.get("title")
        asianfoods_description = request.json.get("description")
        asianfoods_picture = request.json.get("picture")
        asianfoods_ingredients = request.json.get("ingredients")
        
        
        existing_asianfood = Asianfood.query.get(asianfood_id)

        if existing_asianfood:
            existing_asianfood.title = asianfoods_title
            existing_asianfood.description = asianfoods_description
            existing_asianfood.picture = asianfoods_picture
            existing_asianfood.ingredients = asianfoods_ingredients
        else:
            
            new_asianfood = Asianfood(
                id=asianfood_id,  
                title=asianfoods_title,
                description=asianfoods_description,
                picture=asianfoods_picture,
                ingredients=asianfoods_ingredients,
            )
            db.session.add(new_asianfood)

        db.session.commit()

        response_data = {
            "message": "created succefuly",
        }
        json_data = json.dumps(response_data, ensure_ascii=False)
        response = Response(json_data, content_type='application/json; charset=utf-8')
        return response, 201

    
    asianfoods_list = Asianfood.query.all()
    asianfoods = []

    for asianfood in asianfoods_list:
        asianfoods.append({
            "title": asianfood.title,
            "description": asianfood.description,
            "picture": asianfood.picture,
            "ingredients": asianfood.ingredients,
            
        })

    
    response_data = {"asianfoods": asianfoods}
    json_data = json.dumps(response_data, ensure_ascii=False)
    response = Response(json_data, content_type='application/json; charset=utf-8')
    return response


def update_asianfoods(asianfood_id):
    
    asianfoods_title = request.json["title"]
    asianfoods_description = request.json.get("description")
    asianfoods_picture = request.json.get("picture")
    asianfoods_ingredients = request.json.get("ingredients")

    asianfood = Asianfood.query.get(asianfood_id)

    if not asianfood:
        
        return jsonify({"message": "asianfood not found"}), 404

    
    asianfood.title = asianfoods_title
    asianfood.description = asianfoods_description
    asianfood.picture = asianfoods_picture
    asianfood.ingredients = asianfoods_ingredients

    
    db.session.commit()

    
    return jsonify({"message": "update succefuly"}), 200


 
def get_asianfoods(asianfood_id):
    asianfood = Asianfood.query.get(asianfood_id)
    if asianfood:
         
        return jsonify({
            "title": asianfood.title,
            "description": asianfood.description,
            "picture": asianfood.picture,
            "ingredients": asianfood.ingredients,
            
        })


def delete_asianfoods(asianfood_id):
    asianfood = Asianfood.query.get(asianfood_id)
    if asianfood:
        
        db.session.delete(asianfood)
        db.session.commit()
        return jsonify({"message": "delete succefuly"}), 200
def add_get_americanfoods():
    if request.method == "POST":
       
        americanfood_id = request.json.get("id")
        americanfoods_title = request.json.get("title")
        americanfoods_description = request.json.get("description")
        americanfoods_picture = request.json.get("picture")
        americanfoods_ingredients = request.json.get("ingredients")
        
        
        existing_americanfood = Americanfood.query.get(americanfood_id)

        if existing_americanfood:
            existing_americanfood.title = americanfoods_title
            existing_americanfood.description = americanfoods_description
            existing_americanfood.picture = americanfoods_picture
            existing_americanfood.ingredients = americanfoods_ingredients
        else:
            
            new_americanfood = Americanfood(
                id=americanfood_id,  
                title=americanfoods_title,
                description=americanfoods_description,
                picture=americanfoods_picture,
                ingredients=americanfoods_ingredients,
            )
            db.session.add(new_americanfood)

        db.session.commit()

        response_data = {
            "message": "created succefuly",
        }
        json_data = json.dumps(response_data, ensure_ascii=False)
        response = Response(json_data, content_type='application/json; charset=utf-8')
        return response, 201

    
    americanfoods_list = Americanfood.query.all()
    americanfoods = []

    for americanfood in americanfoods_list:
        americanfoods.append({
            "title": americanfood.title,
            "description": americanfood.description,
            "picture": americanfood.picture,
            "ingredients": americanfood.ingredients,
            
        })

    
    response_data = {"americanfoods": americanfoods}
    json_data = json.dumps(response_data, ensure_ascii=False)
    response = Response(json_data, content_type='application/json; charset=utf-8')
    return response


def update_americanfoods(americanfood_id):
    
    americanfoods_title = request.json["title"]
    americanfoods_description = request.json.get("description")
    americanfoods_picture = request.json.get("picture")
    americanfoods_ingredients = request.json.get("ingredients")

    americanfood = Americanfood.query.get(americanfood_id)

    if not americanfood:
        
        return jsonify({"message": "americanfood not found"}), 404

    
    americanfood.title = americanfoods_title
    americanfood.description = americanfoods_description
    americanfood.picture = americanfoods_picture
    americanfood.ingredients = americanfoods_ingredients

    
    db.session.commit()

    
    return jsonify({"message": "update succefuly"}), 200


 
def get_americanfoods(americanfood_id):
    americanfood = Americanfood.query.get(americanfood_id)
    if americanfood:
         
        return jsonify({
            "title": americanfood.title,
            "description": americanfood.description,
            "picture": americanfood.picture,
            "ingredients": americanfood.ingredients,
            
        })


def delete_americanfoods(americanfood_id):
    americanfood = Americanfood.query.get(americanfood_id)
    if americanfood:
        
        db.session.delete(americanfood)
        db.session.commit()
        return jsonify({"message": "delete succefuly"}), 200
def add_get_africanfoods():
    if request.method == "POST":
       
        africanfood_id = request.json.get("id")
        africanfoods_title = request.json.get("title")
        africanfoods_description = request.json.get("description")
        africanfoods_picture = request.json.get("picture")
        africanfoods_ingredients = request.json.get("ingredients")
        
        
        existing_africanfood = Africanfood.query.get(africanfood_id)

        if existing_africanfood:
            existing_africanfood.title = africanfoods_title
            existing_africanfood.description = africanfoods_description
            existing_africanfood.picture = africanfoods_picture
            existing_africanfood.ingredients = africanfoods_ingredients
        else:
            
            new_africanfood = Africanfood(
                id=africanfood_id,  
                title=africanfoods_title,
                description=africanfoods_description,
                picture=africanfoods_picture,
                ingredients=africanfoods_ingredients,
            )
            db.session.add(new_africanfood)

        db.session.commit()

        response_data = {
            "message": "created succefuly",
        }
        json_data = json.dumps(response_data, ensure_ascii=False)
        response = Response(json_data, content_type='application/json; charset=utf-8')
        return response, 201

    
    africanfoods_list = Africanfood.query.all()
    africanfoods = []

    for africanfood in africanfoods_list:
        africanfoods.append({
            "title": africanfood.title,
            "description": africanfood.description,
            "picture": africanfood.picture,
            "ingredients": africanfood.ingredients,
            
        })

    
    response_data = {"africanfoods": africanfoods}
    json_data = json.dumps(response_data, ensure_ascii=False)
    response = Response(json_data, content_type='application/json; charset=utf-8')
    return response


def update_africanfoods(africanfood_id):
    
    africanfoods_title = request.json["title"]
    africanfoods_description = request.json.get("description")
    africanfoods_picture = request.json.get("picture")
    africanfoods_ingredients = request.json.get("ingredients")

    africanfood = Africanfood.query.get(africanfood_id)

    if not africanfood:
        
        return jsonify({"message": "africanfood not found"}), 404

    
    africanfood.title = africanfoods_title
    africanfood.description = africanfoods_description
    africanfood.picture = africanfoods_picture
    africanfood.ingredients = africanfoods_ingredients

    
    db.session.commit()

    
    return jsonify({"message": "update succefuly"}), 200


 
def get_africanfoods(africanfood_id):
    africanfood = Africanfood.query.get(africanfood_id)
    if africanfood:
         
        return jsonify({
            "title": africanfood.title,
            "description": africanfood.description,
            "picture": africanfood.picture,
            "ingredients": africanfood.ingredients,
            
        })


def delete_africanfoods(africanfood_id):
    africanfood = Africanfood.query.get(africanfood_id)
    if africanfood:
        
        db.session.delete(africanfood)
        db.session.commit()
        return jsonify({"message": "delete succefuly"}), 200
def add_get_europeanfoods():
    if request.method == "POST":
       
        europeanfood_id = request.json.get("id")
        europeanfoods_title = request.json.get("title")
        europeanfoods_description = request.json.get("description")
        europeanfoods_picture = request.json.get("picture")
        europeanfoods_ingredients = request.json.get("ingredients")
        
        
        existing_europeanfood = Europeanfood.query.get(europeanfood_id)

        if existing_europeanfood:
            existing_europeanfood.title = europeanfoods_title
            existing_europeanfood.description = europeanfoods_description
            existing_europeanfood.picture = europeanfoods_picture
            existing_europeanfood.ingredients = europeanfoods_ingredients
        else:
            
            new_europeanfood = Europeanfood(
                id=europeanfood_id,  
                title=europeanfoods_title,
                description=europeanfoods_description,
                picture=europeanfoods_picture,
                ingredients=europeanfoods_ingredients,
            )
            db.session.add(new_europeanfood)

        db.session.commit()

        response_data = {
            "message": "created succefuly",
        }
        json_data = json.dumps(response_data, ensure_ascii=False)
        response = Response(json_data, content_type='application/json; charset=utf-8')
        return response, 201

    
    europeanfoods_list = Europeanfood.query.all()
    europeanfoods = []

    for europeanfood in europeanfoods_list:
        europeanfoods.append({
            "title": europeanfood.title,
            "description": europeanfood.description,
            "picture": europeanfood.picture,
            "ingredients": europeanfood.ingredients,
            
        })

    
    response_data = {"europeanfoods": europeanfoods}
    json_data = json.dumps(response_data, ensure_ascii=False)
    response = Response(json_data, content_type='application/json; charset=utf-8')
    return response


def update_europeanfoods(europeanfood_id):
    
    europeanfoods_title = request.json["title"]
    europeanfoods_description = request.json.get("description")
    europeanfoods_picture = request.json.get("picture")
    europeanfoods_ingredients = request.json.get("ingredients")

    europeanfood = Europeanfood.query.get(europeanfood_id)

    if not europeanfood:
        
        return jsonify({"message": "europeanfood not found"}), 404

    
    europeanfood.title = europeanfoods_title
    europeanfood.description = europeanfoods_description
    europeanfood.picture = europeanfoods_picture
    europeanfood.ingredients = europeanfoods_ingredients

    
    db.session.commit()

    
    return jsonify({"message": "update succefuly"}), 200


 
def get_europeanfoods(europeanfood_id):
    europeanfood = Europeanfood.query.get(europeanfood_id)
    if europeanfood:
         
        return jsonify({
            "title": europeanfood.title,
            "description": europeanfood.description,
            "picture": europeanfood.picture,
            "ingredients": europeanfood.ingredients,
            
        })


def delete_europeanfoods(europeanfood_id):
    europeanfood = Europeanfood.query.get(europeanfood_id)
    if europeanfood:
        
        db.session.delete(europeanfood)
        db.session.commit()
        return jsonify({"message": "delete succefuly"}), 200