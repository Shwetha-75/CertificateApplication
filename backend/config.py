import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

class Admin:
    def __init__(self):
        self.url: str = os.getenv("SUPABASE_URL")
        self.key: str = os.getenv("SUPABASE_KEY")
        self.supabase: Client = create_client(self.url, self.key)
        self.resonse=None 
    def accessToken(self):
        self.response=self.supabase.auth.sign_in_with_password(
    {"email": "kshwetha676@gmail.com", "password": "Shwetha@12345"}
    
     
)
        
        
        self.supabase.storage.from_("").get_public_url
        return self.supabase