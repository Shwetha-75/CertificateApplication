from flask import Flask, request, render_template
import os
from implementation.UserModelImplementation import UserModelServices
from implementation.GeneratingCertificate import GeneratingCertificate
from flask_cors import CORS
from models.AdminStorage import AdminStorage                    
import pandas as pd
from config import Admin



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

