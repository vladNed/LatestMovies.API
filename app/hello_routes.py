from flask import Blueprint,jsonify

hello_routes = Blueprint('helloWorld',__name__)

@hello_routes.route('/hello',methods=['GET'])
def hello():
    return 'Hello, World!'