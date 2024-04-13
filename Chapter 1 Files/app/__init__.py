from flask import  Flask

app = Flask(__name__) #create app as an instance of Flask

from app import routes #import routes last to avoid circular import
