from dotenv import load_dotenv
from starlette.config import Config

load_dotenv()
config = Config(".env")

DATABASE_URL = config("YA_DATABASE_URL", cast=str, default="")
