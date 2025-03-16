from flask import Flask, request, render_template
import os
from implementation.UserModelImplementation import UserModelServices
from implementation.GeneratingCertificate import GeneratingCertificate
from flask_cors import CORS
from models.AdminStorage import AdminStorage                    
import pandas as pd
from config import Admin
from implementation.AdminValidation import AdminValidation
from implementation.LoginAdminModel import LoginAdminModel
from implementation.AdminUserNameValidation import AdminUserNameValidation


app = Flask(__name__)
# Configure upload folder
UPLOAD_FOLDER = r"C:\Users\SHWETHA\Desktop\Certificate_Generatoe\Certificate-Generator\uploads"
OUTPUT_FOLDER = r"C:\Users\SHWETHA\Desktop\Certificate_Generatoe\Certificate-Generator\outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

configuration=Admin()
cursor=configuration.accessToken()
CORS(app)
app.secret_key="secret_key_app"

adminValidationObject=AdminValidation(cursor)
loginAdminModel=LoginAdminModel(cursor)
adminUserName=AdminUserNameValidation(cursor) 


@app.route("/register",methods=['GET','POST'])
def registerAdmin():
    if request.method=='POST':
        data=dict(request.form)
        if adminValidationObject.adminValidation(data['email'],data):
            return "ok"
        else:
            return "no"
    return "no"

@app.route("/username",methods=['POST','GET'])
def validatingUserName():
    global response 
    if request.method=='POST':
        data=dict(request.form)
        print(data)
      
        response=adminUserName.validatingUserName(data['username'])
        if response: 
            return "ok"
    return "no"
        
@app.route('/login',methods=['POST','GET'])
def loginAdmin():
    global result
    if request.method=='POST':
       data=dict(request.form) 
       result=loginAdminModel.validatingLogin(data['email'],data['password'])
      
    return result 

@app.route("/data", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the uploaded file and form data
        # file = request.files['image']   
        # get the excel file 
        excel=request.files['excelFile']
        data_frame=pd.read_excel(excel)
        adminStorage=AdminStorage(cursor)
        # generate the certificate
        generatingCertificate=GeneratingCertificate(adminStorage.getFile(),cursor)  
        generatingCertificate.mainActivity(data_frame)
        userServices=UserModelServices(cursor)
        userServices.insertionActivity(generatingCertificate.getUserModels()) 
        # user manipulation
    return render_template("index.html")
     
if __name__ == "__main__":
    app.run(debug=True)

