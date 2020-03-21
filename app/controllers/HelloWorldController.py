from flask import Blueprint

helloWorldController = Blueprint('helloWorld',__name__)

@helloWorldController.route('/hello-world',methods=['GET'])
def hello_world():
    return 'Hello World'