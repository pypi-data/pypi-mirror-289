import hashlib
from django.db import DatabaseError, connections
from django.db.models import Func, BinaryField, CharField
from .get_schema import get_current_schema

class DatabaseUtils():
    def __init__(self):
        self.connection = connections['sym_keys']
        self.cursor = self.connection.cursor()
    
    @staticmethod
    def get_keys():
        try:
            with connections['sym_keys'].cursor() as cursor:
                cursor.execute(f"SELECT key FROM sym_keys.aes_keys")
                rows = cursor.fetchall()
                keys = [row[0] for row in rows]
            return keys
        except DatabaseError as e:
            print(f"Error while getting keys: {e}")

    @staticmethod
    def save_key(key):
        try:
            with connections['sym_keys'].cursor() as cursor:
                cursor.execute(f"INSERT INTO sym_keys.aes_keys (key, created_at) VALUES (%s, NOW())", [key])
        except DatabaseError as e:
            print(f"Error while saving key: {e}")
            raise DatabaseError(f"Error while saving key: {e}")
    
    @staticmethod
    def calculate_checksum(value):
        if value is not None:
            checksum = hashlib.sha256(value.encode('utf-8')).hexdigest()
            return checksum
        return None
    
class AesEncrypt(Func):
    template = "%(function)s(%(expressions)s::text, '%(key)s'::text, 'cipher-algo=aes256'::text)"
    output_field = BinaryField()

    def __init__(self, expression, key, **extra):
        super().__init__(expression, **extra)
        self.extra['key'] = key
        self.function = f"{get_current_schema()}.pgp_sym_encrypt"

class AesDecrypt(Func):
    template = "%(function)s(%(expressions)s::text, '%(key)s'::text)"
    output_field = CharField()

    def __init__(self, expression, key, **extra):
        super().__init__(expression, **extra)
        self.extra['key'] = key
        self.function = f"{get_current_schema()}.pgp_sym_decrypt"
