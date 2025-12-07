from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "0eb6698d376739e33f29b3a12a3c9ab2dc92889e26689426445e5bb0aa92d95e"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
