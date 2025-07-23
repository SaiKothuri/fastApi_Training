from passlib.context import CryptContext  # Importing CryptoContext for password hashing

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")  # Creating a password context for hashing


class Hash():
    def bcrypt(password: str):
        """Hash a password using bcrypt."""
        hashedpassword = pwd_cxt.hash(password)
        return hashedpassword