import os
class AdminStorage:
      
        def __init__(self,cursor):
            self.cursor=cursor 
          
        def downloadingImage(self):
            file_data=self.cursor.storage.from_('admin').download('adminMainFolder/mainTemplateImage.png')
            save_path=os.path.join(r'C:\Users\SHWETHA\Desktop\Certificate_Generatoe\Certificate-Generator\backend\output',"image.png")
            with open(save_path,"wb") as file:
                 file.write(file_data)
        def getFile(self):
            return r"C:\Users\SHWETHA\Desktop\Certificate_Generatoe\Certificate-Generator\backend\output\image.png"