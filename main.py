from flask import Flask, jsonify
from controller import add_get_arabicfoods,get_arabicfoods,update_arabicfoods,delete_arabicfoods, add_get_juices, update_juices, get_juices, delete_juices
from controller import add_get_sauces,update_sauces,get_sauces,delete_sauces,add_get_salades,get_salades,update_salades,delete_salades
from controller import add_get_icecreams,get_icecreams,update_icecreams,delete_icecreams,add_get_sweets,delete_sweets,update_sweets,get_sweets
from controller import add_get_asianfoods,get_asianfoods,update_asianfoods,delete_asianfoods,add_get_africanfoods,get_africanfoods,delete_africanfoods,update_africanfoods
from controller import add_get_americanfoods,get_americanfoods,update_americanfoods,delete_americanfoods,add_get_europeanfoods,get_europeanfoods,delete_europeanfoods,update_europeanfoods
from model import db
from database import DATABASE_URI
from marshmallow import ValidationError
from flask_babel import Babel
import logging


app = Flask(__name__)
babel = Babel(app)

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/arabicfoods", methods=["POST", "GET"])
def arabicfoods():
    try:
        result = add_get_arabicfoods()
        logger.info('Request successful for arabicfoods.')
        return result
    except Exception as e:
        logger.error(f'Error: {str(e)}', exc_info=True)
        return jsonify({"error": "An error occurred for arabicfoods."}), 500

@app.route("/arabicfoods/<int:arabicfood_id>", methods=["PUT"])
def update_arabicfood(arabicfood_id):
    return update_arabicfoods(arabicfood_id)

@app.route("/arabicfoods/<int:arabicfood_id>", methods=["GET"])
def get_arabicfood(arabicfood_id):
    return get_arabicfoods(arabicfood_id)

@app.route("/arabicfoods/<int:arabicfood_id>", methods=["DELETE"])
def delete_arabicfood(arabicfood_id):
    return delete_arabicfoods(arabicfood_id)

@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400

@app.route("/juices", methods=["POST", "GET"])
def juices():
    try:
        result = add_get_juices()
        logger.info('Request successful for juices.')
        return result
    except Exception as e:
        logger.error(f'Error: {str(e)}', exc_info=True)
        return jsonify({"error": "An error occurred for juices."}), 500

@app.route("/juices/<int:juice_id>", methods=["PUT"])
def update_juice(juice_id):
    return update_juices(juice_id)

@app.route("/juices/<int:juice_id>", methods=["GET"])
def get_juice_info(juice_id):
    return get_juices(juice_id)

@app.route("/juices/<int:juice_id>", methods=["DELETE"])
def delete_juice_info(juice_id):
    return delete_juices(juice_id)
@app.route("/sauces", methods=["POST", "GET"])
def sauces():
    try:
        result = add_get_sauces()
        logger.info('Request successful for sauces.')
        return result
    except Exception as e:
        logger.error(f'Error: {str(e)}', exc_info=True)
        return jsonify({"error": "An error occurred for sauces."}), 500

@app.route("/sauces/<int:sauce_id>", methods=["PUT"])
def update_sauce(sauce_id):
    return update_sauces(sauce_id)

@app.route("/sauces/<int:sauce_id>", methods=["GET"])
def get_sauce(sauce_id):
    return get_sauces(sauce_id)

@app.route("/sauces/<int:sauce_id>", methods=["DELETE"])
def delete_sauce(sauce_id):
    return delete_sauces(sauce_id)
@app.route("/salades", methods=["POST", "GET"])
def salades():
    try:
        result = add_get_salades()
        logger.info('Request successful for salades.')
        return result
    except Exception as e:
        logger.error(f'Error: {str(e)}', exc_info=True)
        return jsonify({"error": "An error occurred for salades."}), 500

@app.route("/salades/<int:salade_id>", methods=["PUT"])
def update_salade(salade_id):
    return update_salades(salade_id)

@app.route("/salades/<int:salade_id>", methods=["GET"])
def get_salade(salade_id):
    return get_salades(salade_id)

@app.route("/salades/<int:salade_id>", methods=["DELETE"])
def delete_salade(salade_id):
    return delete_salades(salade_id)
@app.route("/icecreams", methods=["POST", "GET"])
def icecreams():
    try:
        result = add_get_icecreams()
        logger.info('Request successful for icecreams.')
        return result
    except Exception as e:
        logger.error(f'Error: {str(e)}', exc_info=True)
        return jsonify({"error": "An error occurred for icecreams."}), 500

@app.route("/icecreams/<int:sauce_id>", methods=["PUT"])
def update_icecream(icecream_id):
    return update_icecreams(icecream_id)

@app.route("/icecreams/<int:icecream_id>", methods=["GET"])
def get_icecream(icecream_id):
    return get_icecreams(icecream_id)

@app.route("/icecreams/<int:icecream_id>", methods=["DELETE"])
def delete_icecream(icecream_id):
    return delete_icecreams(icecream_id)
@app.route("/sweets", methods=["POST", "GET"])
def sweets():
    try:
        result = add_get_sweets()
        logger.info('Request successful for sweets.')
        return result
    except Exception as e:
        logger.error(f'Error: {str(e)}', exc_info=True)
        return jsonify({"error": "An error occurred for sweets."}), 500

@app.route("/sweets/<int:sauce_id>", methods=["PUT"])
def update_sweet(sweet_id):
    return update_sweets(sweet_id)

@app.route("/sweets/<int:sweet_id>", methods=["GET"])
def get_sweet(sweet_id):
    return get_sweets(sweet_id)

@app.route("/sweets/<int:sweet_id>", methods=["DELETE"])
def delete_sweet(sweet_id):
    return delete_sweets(sweet_id)
@app.route("/asianfoods", methods=["POST", "GET"])
def asianfoods():
    try:
        result = add_get_asianfoods()
        logger.info('Request successful for asianfoods.')
        return result
    except Exception as e:
        logger.error(f'Error: {str(e)}', exc_info=True)
        return jsonify({"error": "An error occurred for asianfoods."}), 500

@app.route("/asianfoods/<int:sauce_id>", methods=["PUT"])
def update_asianfood(asianfood_id):
    return update_asianfoods(asianfood_id)

@app.route("/asianfoods/<int:asianfood_id>", methods=["GET"])
def get_asianfood(asianfood_id):
    return get_asianfoods(asianfood_id)

@app.route("/asianfoods/<int:asianfood_id>", methods=["DELETE"])
def delete_asianfood(asianfood_id):
    return delete_asianfoods(asianfood_id)
@app.route("/americanfoods", methods=["POST", "GET"])
def americanfoods():
    try:
        result = add_get_americanfoods()
        logger.info('Request successful for americanfoods.')
        return result
    except Exception as e:
        logger.error(f'Error: {str(e)}', exc_info=True)
        return jsonify({"error": "An error occurred for americanfoods."}), 500

@app.route("/americanfoods/<int:sauce_id>", methods=["PUT"])
def update_americanfood(americanfood_id):
    return update_americanfoods(americanfood_id)

@app.route("/americanfoods/<int:americanfood_id>", methods=["GET"])
def get_americanfood(americanfood_id):
    return get_americanfoods(americanfood_id)

@app.route("/americanfoods/<int:americanfood_id>", methods=["DELETE"])
def delete_americanfood(americanfood_id):
    return delete_americanfoods(americanfood_id)
@app.route("/africanfoods", methods=["POST", "GET"])
def africanfoods():
    try:
        result = add_get_africanfoods()
        logger.info('Request successful for africanfoods.')
        return result
    except Exception as e:
        logger.error(f'Error: {str(e)}', exc_info=True)
        return jsonify({"error": "An error occurred for africanfoods."}), 500

@app.route("/africanfoods/<int:sauce_id>", methods=["PUT"])
def update_africanfood(africanfood_id):
    return update_africanfoods(africanfood_id)

@app.route("/africanfoods/<int:africanfood_id>", methods=["GET"])
def get_africanfood(africanfood_id):
    return get_africanfoods(africanfood_id)

@app.route("/africanfoods/<int:africanfood_id>", methods=["DELETE"])
def delete_africanfood(africanfood_id):
    return delete_africanfoods(africanfood_id)
@app.route("/europeanfoods", methods=["POST", "GET"])
def europeanfoods():
    try:
        result = add_get_europeanfoods()
        logger.info('Request successful for europeanfoods.')
        return result
    except Exception as e:
        logger.error(f'Error: {str(e)}', exc_info=True)
        return jsonify({"error": "An error occurred for europeanfoods."}), 500

@app.route("/europeanfoods/<int:europeanfood_id>", methods=["PUT"])
def update_europeanfood(europeanfood_id):
    return update_europeanfoods(europeanfood_id)

@app.route("/europeanfoods/<int:europeanfood_id>", methods=["GET"])
def get_europeanfood(europeanfood_id):
    return get_europeanfoods(europeanfood_id)

@app.route("/europeanfoods/<int:europeanfood_id>", methods=["DELETE"])
def delete_europeanfood(europeanfood_id):
    return delete_europeanfoods(europeanfood_id)
if __name__ == '__main__':
    app.run(debug=True)


