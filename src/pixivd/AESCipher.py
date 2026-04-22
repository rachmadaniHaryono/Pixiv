import base64

import pyaes


def _get_key():
    import os
    import uuid
    i = int(os.environ.get("PIXIVD_AES_INT", uuid.getnode()))
    return uuid.UUID(int=i).hex


class AESCipher:
    def __init__(self):
        self.key = _get_key().encode('utf-8')

    def encrypt(self, raw):
        cipher = pyaes.AESModeOfOperationCTR(self.key)
        return base64.b64encode(cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = pyaes.AESModeOfOperationCTR(self.key)
        return cipher.decrypt(enc).decode('utf-8')
