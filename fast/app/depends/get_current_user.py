import jwt
from settings import SECRET_KEY, ALGORITHM

async def get_current_user(token: str):
    user = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return user
