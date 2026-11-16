from flask import Flask, render_template, request, jsonify 
import datetime
import random
 
app = Flask(__name__) # create Flask application instance with name 'app' (name of python file)
#app.debug = True
 
# HTTP REQUESTS AND RESPONSES
# return root resource index.html for first get request "GET /"
@app.route('/') # '/' means that this fcn responds to request for URL /, which is main URL
def index():
    return render_template('index.html') # can also pass dictionary with data as argument: ...('index.html', data=data_dict)
 
@app.route('/interactWithServer', methods = ['POST'])
def do_something(): # is executed whenever client sends request with "let response = await fetch('/interactWithServer', {...."
    data = request.json['data'] # save data sent by JS in variable
    # do something with data
    # e.g. create dictionary with response data
    data_response = {"name":"Ioanna", "age":42}
    return data_response
 
if __name__ == '__main__':
    app.run()
 
"""
typical shape
@app.route(...) # this decorator turns a ...
def some_fcn(): # ... regular Python function into a Flask view function which ...
    ...
    return ...  # ... converts the function's return value into an HTTP response)
"""