class AdminUserNameValidation:
        def __init__(self,cursor):
            self.cursor=cursor
        def validatingUserName(self,userName)->bool:
            response=self.cursor.table('admin').select("*").eq('userName',userName).execute()
            return len(response.data)==0

           