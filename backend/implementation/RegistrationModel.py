from models.AdminManipulation import AdminManipulation
from models.AdminModel import AdminModel

class RegistrationModelValidation: 
    def __init__(self):
        self.objectValidatesAdmin=AdminManipulation() 
    def validateEmail(self,adminData,email):
        # if self.objectValidatesAdmin.checkEmailExist(email):
        #    return [False,"AdminExits"]
        # else:
        #     adminData=AdminModel(adminData["userName"],adminData["email"],adminData["linkedInProfile"],adminData["gitHubProfile"],adminData["password"],adminData["confirmPassword"])
        #     self.objectValidatesAdmin.insertAdminModel(adminData.__str__())
        pass
        
        