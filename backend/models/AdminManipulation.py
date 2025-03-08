from  models.AdminModel import AdminModel

class AdminManipulation:
    def __init__(self,cursor):
          self.cursor=cursor
          
  
    def insertAdminModel(self,adminData):
        insertData=AdminModel(adminData['userName'],
                              adminData['email'],
                              adminData['linkedInProfile'],
                            adminData['gitHubProfile'],
                            adminData['password'],
                            adminData['confirmPassword']
                            )
        
        self.cursor.table("admin").insert(insertData.__str__()).execute()
     
    
    def updateAdminModel(self,adminData,response):
        pass
        