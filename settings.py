import os
from dotenv import load_dotenv

project_folder = os.getcwd()
load_dotenv(os.path.join(project_folder, '.env'))

API_TOKEN = os.getenv("API_TOKEN")
CONNECTION_ID = os.getenv('CONNECTION_ID')