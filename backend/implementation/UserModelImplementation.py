from models.UserManipulation import UserManipulation
class UserModelServices:
    def __init__(self,cursor):
        self.user=UserManipulation(cursor)
    def insertionActivity(self,userDataSet):
        for i in userDataSet:
            self.user.insertUserModel(i)
        