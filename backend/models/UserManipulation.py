from models.UserModel import UserModel
class UserManipulation:
        def __init__(self,cursor):
            self.cursor=cursor
        def insertUserModel(self,userData):
            response=self.cursor.table("usermodel").select("*").eq('email',userData["email"]).execute()
            if len(response.data)==0:
                # create the user 
                self.cursor.table('usermodel').insert(userData).execute()
            else:
                self.updateUserModel(userData,response.data[0])
            return self 
        def updateUserModel(self,userData,response):
            update_user_model=UserModel(userData.get("year"),userData.get("course"),response['email'],userData.get("file_url"),response['user_id'],userData.get("firstName"),userData.get("lastName"),userData.get("uploaded_file"))
            update_user_model={
                  "firstName":update_user_model.getFirstName(),
                  'lastName':update_user_model.getLastName(),
                  "file_url":update_user_model.getFileURL(),
                  "course":update_user_model.getCourse(),
                  "uploaded_file":update_user_model.getUploadedFile(),
                  "year":update_user_model.getYear()
            }
            self.cursor.table("usermodel").update(update_user_model).eq("email",response['email']).execute()
            return self
        
        def readUserModel(self,email):
            return self.cursor.table("usermodel").select("*").eq("email",email).execute().data[0]
        
        def deleteUserModel(self,user_id):
            response=self.cursor("usermodel").delete().eq("user_id",user_id).execute()
            if len(response.data)==0:
                print("User does not exist !!")
            else:
                print("User deleted successfully !!")
                