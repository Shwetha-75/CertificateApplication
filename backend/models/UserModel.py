import uuid
from datetime import timezone

class UserModel:
    
    def __init__(self,year,course,email,file_url,user_id,firstName,lastName,uploaded_file):
        self.__uploaded_file=uploaded_file
        self.__year=year
        self.__firstName=firstName
        self.__course=course
        self.__email=email
        self.__file_url=file_url
        self.__user_id=user_id
        self.__lastName=lastName
    

        
    def setFirstName(self,firstName:str):
        self.__firstName=firstName
        
    def setFileURL(self,file_url:str):
        self.__file_url=file_url 
    
    def setEmail(self,email:str):
        self.__email=email 
        
    def setCourse(self,course:str):
        self.__course=course 
    
    def setYear(self,year:str):
        self.__year=year
        
    def setUserId(self,user_id:uuid):
        self.__user_id=user_id
        
    def setLastName(self,lastName:str):
        self.__lastName=lastName 
    def setUploadedFile(self,uploadedFile:timezone):     
        self.__uploaded_file=uploadedFile
    
    def getUserId(self):
        return self.__user_id
    
    
    def getFirstName(self):
        return self.__firstName
    
    
    def getFileURL(self):
        return self.__file_url
    

    
    def getEmail(self):
        return self.__email 
    
    def getYear(self):
        return self.__year
    def getLastName(self):
        return self.__lastName
    def getUploadedFile(self):
        return self.__uploaded_file
    
    def getCourse(self):
        return self.__course    
    def __str__(self):
        return {
            
                'file_url':self.__file_url,
                "uploaded_file":self.__uploaded_file, 
                'email':self.__email,
                'course':self.__course,
                'year':self.__year,
                "user_id":self.__user_id,
                "firstName":self.__firstName,
                "lastName":self.__lastName,
               
        }