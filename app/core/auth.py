from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(self, hashed_password: str) -> str:
    return self.pwd_context.hash(hashed_password)


def verify_password(self, password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)