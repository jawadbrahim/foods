from flask import Flask,request
from controller import add_get_arabicfoods,get_arabicfoods,update_arabicfoods,delete_arabicfoods,add_get_juices,update_juices,get_juices,delete_juices,add_get_sauces,update_sauces,get_sauces,delete_sauces
from controller import add_get_salades,update_salades,get_salades,delete_salades,add_get_icecreams,get_icecreams,delete_icecreams,update_icecreams,add_get_sweets,get_sweets,update_sweets,delete_sweets
from controller import add_get_asianfoods,update_asianfoods,get_asianfoods,delete_asianfoods,add_get_africanfoods,get_africanfoods,delete_africanfoods,update_africanfoods
from controller import add_get_americanfoods,get_americanfoods,delete_americanfoods,update_americanfoods,add_get_europeanfoods,get_europeanfoods,update_europeanfoods,delete_europeanfoods
from model import db
from main import app
@app.route("/arabicfood", methods=["POST", "GET"])
def arabicfoods():
    return add_get_arabicfoods()

@app.route("/arabicfoods/<int:food_id>", methods=["PUT", "GET", "DELETE"])
def food(food_id):
    if request.method == "PUT":
        return update_arabicfoods(food_id)
    elif request.method == "GET":
        return get_arabicfoods(food_id)
    elif request.method == "DELETE":
        return delete_arabicfoods(food_id)
@app.route("/juices", methods=["POST", "GET"])
def juices():
    return add_get_juices()

@app.route("/juice/<int:juice_id>", methods=["PUT", "GET", "DELETE"])
def juice(juice_id):
    if request.method == "PUT":
        return update_juices(juice_id)
    elif request.method == "GET":
        return get_juices(juice_id)
    elif request.method == "DELETE":
        return delete_juices(juice_id)
@app.route("/sauce", methods=["POST", "GET"])
def sauces():
    return add_get_sauces()

@app.route("/sauces/<int:sauce_id>", methods=["PUT", "GET", "DELETE"])
def sauce(sauce_id):
    if request.method == "PUT":
        return update_sauces(sauce_id)
    elif request.method == "GET":
        return get_sauces(sauce_id)
    elif request.method == "DELETE":
        return delete_sauces(sauce_id)
@app.route("/salade", methods=["POST", "GET"])
def salades():
    return add_get_salades()

@app.route("/salades/<int:salade_id>", methods=["PUT", "GET", "DELETE"])
def salade(salade_id):
    if request.method == "PUT":
        return update_salades(salade_id)
    elif request.method == "GET":
        return get_salades(salade_id)
    elif request.method == "DELETE":
        return delete_salades(salade_id)
@app.route("/icecream", methods=["POST", "GET"])
def icecreams():
    return add_get_icecreams()

@app.route("/icecreams/<int:icecream_id>", methods=["PUT", "GET", "DELETE"])
def icecream(icecream_id):
    if request.method == "PUT":
        return update_icecreams(icecream_id)
    elif request.method == "GET":
        return get_icecreams(icecream_id)
    elif request.method == "DELETE":
        return delete_icecreams(icecream_id)
@app.route("/sweet", methods=["POST", "GET"])
def sweets():
    return add_get_sweets()

@app.route("/sweets/<int:sweet_id>", methods=["PUT", "GET", "DELETE"])
def sweet(sweet_id):
    if request.method == "PUT":
        return update_sweets(sweet_id)
    elif request.method == "GET":
        return get_sweets(sweet_id)
    elif request.method == "DELETE":
        return delete_sweets(sweet_id)
@app.route("/asianfoods", methods=["POST", "GET"])
def asianfood():
    return add_get_asianfoods()

@app.route("/asianfood/<int:sweet_id>", methods=["PUT", "GET", "DELETE"])
def asianfood(sweet_id):
    if request.method == "PUT":
        return update_asianfoods(sweet_id)
    elif request.method == "GET":
        return get_asianfoods(sweet_id)
    elif request.method == "DELETE":
        return delete_asianfoods(sweet_id)
@app.route("/africanfoods", methods=["POST", "GET"])
def africanfood():
    return add_get_africanfoods()

@app.route("/africanfood/<int:sweet_id>", methods=["PUT", "GET", "DELETE"])
def africanfood(sweet_id):
    if request.method == "PUT":
        return update_africanfoods(sweet_id)
    elif request.method == "GET":
        return get_africanfoods(sweet_id)
    elif request.method == "DELETE":
        return delete_africanfoods(sweet_id)
@app.route("/americanfoods", methods=["POST", "GET"])
def americanfood():
    return add_get_americanfoods()

@app.route("/americanfood/<int:sweet_id>", methods=["PUT", "GET", "DELETE"])
def americanfood(sweet_id):
    if request.method == "PUT":
        return update_americanfoods(sweet_id)
    elif request.method == "GET":
        return get_americanfoods(sweet_id)
    elif request.method == "DELETE":
        return delete_americanfoods(sweet_id)
@app.route("/europeanfoods", methods=["POST", "GET"])
def europeanfood():
    return add_get_europeanfoods()

@app.route("/europeanfood/<int:sweet_id>", methods=["PUT", "GET", "DELETE"])
def europeanfood(sweet_id):
    if request.method == "PUT":
        return update_europeanfoods(sweet_id)
    elif request.method == "GET":
        return get_europeanfoods(sweet_id)
    elif request.method == "DELETE":
        return delete_europeanfoods(sweet_id)
   