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
            update_user_model={
                  "firstName":userData.get("firstName"),
                  'lastName':userData.get("lastName"),
                  "file_url":userData.get("file_url"),
                  "course":userData.get("course"),
                  "uploaded_file":userData.get("uploaded_file"),
                  "year":userData.get("year")
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