from dotenv import load_dotenv
import os

load_dotenv()

# ENV setting
APP_ENV = os.getenv('APP_ENV', 'develop')
SECRET_KEY = os.getenv('APP_ENV', 'develop')
ALGORITHM = os.getenv('APP_ENV', 'develop')
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('APP_ENV', 'develop')


DB_NAME = os.getenv('DB_NAME', 'develop')
DB_USER = os.getenv('DB_USER', 'develop')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'develop')
DB_HOST = os.getenv('DB_HOST', 'develop')
DB_PORT = os.getenv('DB_PORT', 'develop')
TEST_DB_HOST = os.getenv('TEST_DB_HOST')
DB_SQL_DEBUG = os.getenv('DB_SQL_DEBUG') == '1'

DB_URL = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8"
# DB_URL = os.getenv('DATABASE_URL')
print(DB_URL)
TEST_DB_URL = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}_test?charset=utf8"