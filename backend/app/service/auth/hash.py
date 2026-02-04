from pwdlib import PasswordHash



class Hasher:

    def __init__(self, hasher: PasswordHash):
        self.hasher = hasher or PasswordHash.recommended()

    def verify_password(
        self,
        plain_password: str,
        hashed_password: str
    ) -> bool:
        return self.hasher.verify(plain_password, hashed_password)

    def hash_password(self, plain_password: str) -> str:
        return self.hasher.hash(plain_password)