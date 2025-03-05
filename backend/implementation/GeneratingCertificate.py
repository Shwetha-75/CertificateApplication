from PIL import Image, ImageDraw, ImageFont  
import nanoid
import os
from datetime import datetime
from uuid import uuid4
class GeneratingCertificate:
    
    def __init__(self,path,cursor):
        self.result=[]
        self.image_path=path
        self.cursor=cursor
      
    def mainActivity(self,dataFrames:list[dict]):
        n=len(dataFrames)
        for i in range(n):
            self.generatingCertificateMethod(dataFrames['firstName'][i],dataFrames['lastName'][i],dataFrames['course'][i],dataFrames['year'][i],dataFrames['email'][i])   
        
    def generatingCertificateMethod(self,firstName,lastName,course,year,email):
        # Pseudo code 
        # for each user 
        
        # we write the text on to the image 
        # we don't save the image in local but 
        # uploading the current image to supabase 
        
        # as response we get key as the path uploaded the image
        # then for each user we extract the information from excel and upload the data including the image path 
        
        # and then we can keep track of image for each user 
        # then we can upload the entries on to the supabase 
        
        img=Image.open(self.image_path)
        draw=ImageDraw.Draw(img)
        try:
            font=ImageFont.truetype("arial.ttf",size=24)
        except IOError:
               font=ImageFont.load_default()
        name_coords=(679,312)
        course_coords=(636,369)
        year_coords=(121,420)
        draw.text(name_coords,firstName+" "+lastName,fill="white",font=font)        
        draw.text(year_coords,year,fill="white",font=font)        
        draw.text(course_coords,course,fill="white",font=font)    
        user_id=str(uuid4()) 
        temp="certify"+firstName+".png"
        file_path=r"C:\Users\SHWETHA\Desktop\Certificate_Generatoe\Certificate-Generator\backend\user"
        save_path=os.path.join(file_path,temp)
        img.save(save_path)
        files=self.cursor.storage.from_("images").list()
        file_exists=any(file['name']==file_path for file in files)
        print(file_exists)
        with open(save_path,"rb") as f:
             response=self.cursor.storage.from_("images").update(
                 path=f"public/{temp}",
                 file=f,
               
                 )
             user_model={
                 "email":email,
                 "lastName":lastName,
                 "firstName":firstName,
                 "file_url":response.path,
                 "course":course,
                 "uploaded_file":str(datetime.now()),
                 "user_id":user_id,
                 "year":year
             }
             self.result.append(user_model)
        # success full 
    def getUserModels(self):
        return self.result    
    
          