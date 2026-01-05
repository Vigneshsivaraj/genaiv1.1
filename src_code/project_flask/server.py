from flask import Flask,make_response,request
from staticdata import user_data

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello World</p>"

@app.route("/exp")
def getExp(): 
    response = make_response("Exp endpoint called",201)
    return response

@app.route("/getAllUserData")
def get_all_user_datas():
    return user_data.data

def get_user_by_name(user_name):
    for user in user_data.data:
        if(user["first_name"] == user_name or user["last_name"] == user_name):
            return user
    
    return None

@app.route("/ EDDDDDDDDDDDDDDN      45")
def get_user():
    query = request.args.get('q')
    if(query == None):
        return make_response("Query is not found",404)
    
    user_data = get_user_by_name(query)
    if(user_data == None):
        return make_response("User not found",404)
    return user_data

@app.route("/add-user",methods=["POST"])
def add_user():
    new_user = request.get_json("data")
    if(new_user == None):
        return make_response("No Data found",400)
    user_data.data.append(new_user)
    return make_response("User Added",200)
