class AdminModel():
    def __init__(self,userName:str,email:str,linkedInProfile:str,gitHubProfile:str,password:str,confirmPassword:str):
         self.__userName=userName
         self.__email=email
         self.__linkedInProfile=linkedInProfile
         self.__gitHubProfile=gitHubProfile
         self.__password=password
         self.__confirmPassword=confirmPassword 
         
    def setUSerName(self,userName:str):
        self.__userName=userName 
    
    
    def setEmail(self,email:str):
        self.__email=email 
        
    def setlinkedInProfile(self,linkedInProfile:str):
        self.__linkedInProfile=linkedInProfile
    
    def setGitHubProfile(self,gitHubProfile:str):
        self.__gitHubProfile=gitHubProfile 
        
    def setPassword(self,password:str):
        self.__password=password 
        
    def setConfirmPassword(self,confirmPassword:str):
        self.__confirmPassword=confirmPassword  
    
    def getUserName(self):
        return self.__userName 
    
    def getPassword(self):
        return self.__password 
    
    def getConfirmPassword(self):
        return self.__confirmPassword 
    
    def getEmail(self):
        return self.__email 
    
    def getLinkedInProfile(self):
        return self.__linkedInProfile 
    
    def getGitHubProfile(self):
        return self.__gitHubProfile
    
    
    def __str__(self):
        return {
            "userName":self.__userName,
            "email":self.__email,
            "linkedInProfile":self.__linkedInProfile,
            "gitHubProfile":self.__gitHubProfile,
            "password":self.__password,
            "confirmPassword":self.__confirmPassword
        }
    
    