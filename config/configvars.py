from dotenv import load_dotenv
import os

load_dotenv('config/.env')

DATABASE_HOST=os.getenv("DATABASE_HOST") 
DATABASE_USERNAME=os.getenv("DATABASE_USERNAME")
DATABASE_PASSWORD=os.getenv("DATABASE_PASSWORD")
DATABASE=os.getenv("DATABASE")