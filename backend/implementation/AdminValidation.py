from models.AdminManipulation import AdminManipulation
class AdminValidation:
        def __init__(self,cursor):
            self.cursor=cursor 
            self.adminManipulationObject=AdminManipulation(cursor)
        def adminValidation(self,email:str,adminData)->bool:
            
            response=self.cursor.table("admin").select("*").eq("email",email).execute()
            print("Response: ",response)
            if len(response.data)==0:
                #  insert it 
                self.adminManipulationObject.insertAdminModel(adminData)
                return True 
            else:
                return False 
 