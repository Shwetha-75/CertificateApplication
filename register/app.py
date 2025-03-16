from flask import Flask
from flask_cors import CORS 

app=Flask(__name__)
CORS(app)

@app.route("/register",methods=['POST','GET'])
def register():
    pass 