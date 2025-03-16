from flask import Flask,request

from flask_cors import CORS
from dbConfiguration.config import Configuration

app=Flask(__name__)
CORS(app)

configuration=Configuration()




@app.route("/username",methods=['GET','POST'])
def validatingUserName()->bool:
    if request.method=='POST':
        data=dict(request.form)
        print(data)
        response=configuration.getToken().table('admin').select("*").eq('userName',data['userName']).execute()
        print(response)
        if len(response.data)==0:
            return "ok"
        
    return "no"

import os 
result=os.path.exists(r"C:\Users\SHWETHA\Desktop\NewCertifyApplication\Certificate-Generator\dbConfiguration\__init__.py")

if __name__=='__main__':
    app.run(port=8081,debug=True)