from app import app

#View functions, below, are mapped to one or more route URLS so that Flask knows what logic to execute when a client requests a given URL.
@app.route('/') #this is a decorator which creates an association between the URL given and the function
@app.route('/index')
def index():
    return "Hello, World!"
