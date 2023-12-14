import os
from dotenv import load_dotenv
load_dotenv()

DB_HOSTNAME = os.getenv("DB_HOSTNAME")
DB_PORT = os.getenv("DB_PORT")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_USERNAME = os.getenv("DB_USERNAME")

# Correct the driver name to 'pymysql'
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/{DB_NAME}"
