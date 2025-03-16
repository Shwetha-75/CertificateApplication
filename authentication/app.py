from flask import Flask,request
from flask_cors import CORS
from AdminValidation import LoginAdminModel
from dbConfiguration.config import Configuration
app=Flask(__name__)
CORS(app)


database=Configuration().getToken()
loginAdminModel=LoginAdminModel(database)

@app.route("/login",methods=['POST','GET'])
def login():
    global result 
    if request.method=='POST':
        data=dict(request.form)
        result=loginAdminModel.validatingLogin(data['email'],data['password'])
        
    return result 


if __name__=='__main__':
    app.run(port=7676,debug=True)