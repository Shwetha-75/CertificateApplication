class LoginAdminModel:
        def __init__(self,cursor):
            self.cursor=cursor
            self.response=None 
        def validatingLogin(self,email:str,password:str):
            if not self.validEmail(email):
                return 'emailInvalid'
            return self.validPassword(password)
            
        def validEmail(self,email:str):
            self.response=self.cursor.table('admin').select('*').eq('email',email).execute()
            return len(self.response.data)!=0 
        
        def validPassword(self,password:str):
            return 'ok' if password==self.response.data[0]['password'] else 'invalidPassword'
    
            