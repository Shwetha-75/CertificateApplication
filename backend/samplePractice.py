from config import Admin 

from uuid import uuid4
import os
# cursor 
cursor=Admin().accessToken()

# performing the CRUD operations 


# success fully inserted 
new_record = { 
              "email":"nikithak421@gmail.com",
              "firstName": 'Nikil',
              "lastName":"K",
              "file_url":"image",
              "course":"javascript",
              "uploaded_file":"hjhjjdhj",
              "user_id":str(uuid4()),
              "year":"2025"}
response = (cursor.table('usermodel').update({"course":"java"}).eq("email","nikithak421@gmail.com").execute())
print(response)
# print(response)
#    creating the storage bucket and uploading the images 

# file_path = r"C:\Users\SHWETHA\Desktop\Certificate_Generatoe\Certificate-Generator\backend\image.png"  # Replace with the path to your image file

# # response=cursor.storage.create_bucket(
# #   'avatars',
# #   options={"public": True}
# # )
# # print(response)
# # reponse=cursor.storage.create_bucket(
# #   'avatars',
# #   options={"public": True}
# # )
# # print(reponse)

# # response=cursor.storage.list_buckets()
# # print(response)

# # response=cursor.auth.get_user()
# # print(response)

                                                        
# # with open(file_path, 'rb') as f:
# #   response = cursor.storage.from_("images").upload(
# #       file=f,
# #       path="public/avatar1.png",
# #       file_options={"cache-control": "3600", "upsert": "false"},
# #   )
# # print(response)

# # Getting data from the bucket list 
# response=cursor.storage.from_('admin').list('adminMainFolder')
# # Getting list of images from folder 
# response=cursor.storage.from_('admin').list('adminMainFolder')
# # returns the list of images inside the images 
# # print(response)


# file_data=cursor.storage.from_('admin').download('adminMainFolder/mainTemplateImage.png')
# # print(response)


# # success fully downloaded the image 

# save_path=os.path.join(r'C:\Users\SHWETHA\Desktop\Certificate_Generatoe\Certificate-Generator\backend\output',"image.png")
# with open(save_path,"wb") as file:
#         file.write(file_data)