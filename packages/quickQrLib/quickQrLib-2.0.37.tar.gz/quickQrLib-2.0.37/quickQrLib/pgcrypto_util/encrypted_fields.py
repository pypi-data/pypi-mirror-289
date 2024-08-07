from django.db import models, connection
from django.conf import settings
from .get_schema import get_current_schema
from .database_encryption import DatabaseUtils

#from django.db.models import F

# # Encrypting a field
# MyModel.objects.update(encrypted_field=AesEncrypt(F('plain_text_field'), 'my_secret_key'))

# # Decrypting a field in a query
# decrypted_values = MyModel.objects.annotate(decrypted_field=AesDecrypt(F('encrypted_field'), 'my_secret_key')).values('decrypted_field')

class EncryptedTextField(models.BinaryField):
    def __init__(self, *args, **kwargs):
        self.db_utils = DatabaseUtils()
        self.all_keys = DatabaseUtils.get_keys()
        # self.encrypt_key = self.all_keys[0] if self.all_keys else settings.PGCRYPTO_DEFAULT_KEY
        self.encrypt_key = self.all_keys[1].strip()
        self.schema = get_current_schema()
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        if value is not None:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {self.schema}.pgp_sym_encrypt(%s::text, %s::text)", [value, self.encrypt_key])
                result = cursor.fetchone()
                if result:
                    # Ensure the encrypted value is properly returned
                    encrypted_value = result[0]
                    if isinstance(encrypted_value, memoryview):
                        value = encrypted_value.tobytes()  # Convert memoryview to bytes
                        return value
                else:
                    # Handle the case where encryption returns no value
                    print(f"\n============================================\nEncryption failed or returned no value.\n============================================\n")
                    return None
        return value

    def from_db_value(self, value, expression, connection):
        print("\n===============================================\n INSIDE ENCRYPTED TEXT FIELD\nfrom_db_value()\n===============================================\n")
        if value is not None:
            with connection.cursor() as cursor:
                for key in self.all_keys:
                    try:
                        cursor.execute(f"SELECT {self.schema}.pgp_sym_decrypt(%s::bytea, %s::text)", [value, key.strip()])
                        result = cursor.fetchone()
                        if result:
                            string_value = result[0]
                            if isinstance(string_value, memoryview):
                                return string_value.tobytes()
                            if isinstance(string_value, bytes):
                                return string_value.decode('utf-8')  # Convert bytes to string
                            return string_value
                    except Exception as e:
                        print(f"Decryption with key {key} failed: {e}")
        return value

class EncryptedCharField(models.BinaryField):
    def __init__(self, *args, **kwargs):
        self.db_utils = DatabaseUtils()
        self.all_keys = DatabaseUtils.get_keys()
        # self.encrypt_key = self.all_keys[0] if self.all_keys else settings.PGCRYPTO_DEFAULT_KEY
        self.encrypt_key = self.all_keys[0].strip()
        self.schema = get_current_schema()
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        if value is not None:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {self.schema}.pgp_sym_encrypt(%s::text, %s::text)", [value, self.encrypt_key])
                result = cursor.fetchone()
                if result:
                    # Ensure the encrypted value is properly returned
                    encrypted_value = result[0]
                    if isinstance(encrypted_value, memoryview):
                        value = encrypted_value.tobytes()  # Convert memoryview to bytes
                        return value
                else:
                    # Handle the case where encryption returns no value
                    print(f"\n============================================\nEncryption failed or returned no value.\n============================================\n")
                    return None
        return value


    def from_db_value(self, value, expression, connection):
        print("\n===============================================\n INSIDE ENCRYPTED CHAR FIELD\nfrom_db_value()\n===============================================\n")
        if value is not None:
            with connection.cursor() as cursor:
                for key in self.all_keys:
                    try:
                        cursor.execute(f"SELECT {self.schema}.pgp_sym_decrypt(%s::bytea, %s::text)", [value, key.strip()])
                        result = cursor.fetchone()
                        if result:
                            string_value = result[0]
                            if isinstance(string_value, memoryview):
                                return string_value.tobytes()
                            if isinstance(string_value, bytes):
                                return string_value.decode('utf-8')  # Convert bytes to string
                            return string_value
                    except Exception as e:
                        print(f"Decryption with key {key} failed: {e}")
        return value

class EncryptedEmailField(models.BinaryField):
    def __init__(self, *args, **kwargs):
        self.db_utils = DatabaseUtils()
        self.all_keys = DatabaseUtils.get_keys()
        # self.encrypt_key = self.all_keys[0] if self.all_keys else settings.PGCRYPTO_DEFAULT_KEY
        self.encrypt_key = self.all_keys[0].strip()
        self.schema = get_current_schema()
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        if value is not None:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {self.schema}.pgp_sym_encrypt(%s::text, %s::text)", [value, self.encrypt_key])
                result = cursor.fetchone()
                if result:
                    # Ensure the encrypted value is properly returned
                    encrypted_value = result[0]
                    if isinstance(encrypted_value, memoryview):
                        value = encrypted_value.tobytes()  # Convert memoryview to bytes
                        return value
                else:
                    # Handle the case where encryption returns no value
                    print(f"\n============================================\nEncryption failed or returned no value.\n============================================\n")
                    return None
        return value

    def from_db_value(self, value, expression, connection):
        print("\n===============================================\n INSIDE ENCRYPTED EMAIL FIELD\nfrom_db_value()\n===============================================\n")
        if value is not None:
            with connection.cursor() as cursor:
                for key in self.all_keys:
                    try:
                        cursor.execute(f"SELECT {self.schema}.pgp_sym_decrypt(%s::bytea, %s::text)", [value, key.strip()])
                        result = cursor.fetchone()
                        if result:
                            string_value = result[0]
                            if isinstance(string_value, memoryview):
                                return string_value.tobytes()
                            if isinstance(string_value, bytes):
                                return string_value.decode('utf-8')  # Convert bytes to string
                            return string_value
                    except Exception as e:
                        print(f"Decryption with key {key} failed: {e}")
        return value

class EncryptedIntegerField(models.BinaryField):
    def __init__(self, *args, **kwargs):
        self.db_utils = DatabaseUtils()
        self.all_keys = DatabaseUtils.get_keys()
        self.encrypt_key = self.all_keys[0] if self.all_keys else settings.PGCRYPTO_DEFAULT_KEY
        self.schema = get_current_schema()
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        if value is not None:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {self.schema}.pgp_sym_encrypt(%s::text, %s::text)", [value, self.encrypt_key])
                result = cursor.fetchone()
                if result:
                    # Ensure the encrypted value is properly returned
                    encrypted_value = result[0]
                    if isinstance(encrypted_value, memoryview):
                        value = encrypted_value.tobytes()  # Convert memoryview to bytes
                        return value
                else:
                    # Handle the case where encryption returns no value
                    print(f"\n============================================\nEncryption failed or returned no value.\n============================================\n")
                    return None
        return value


    def from_db_value(self, value, expression, connection):
        print("\n===============================================\n INSIDE ENCRYPTED INTEGER FIELD\nfrom_db_value()\n===============================================\n")
        if value is not None:
            with connection.cursor() as cursor:
                for key in self.all_keys:
                    try:
                        cursor.execute(f"SELECT {self.schema}.pgp_sym_decrypt(%s::bytea, %s::text)", [value, key.strip()])
                        result = cursor.fetchone()
                        if result:
                            string_value = result[0]
                            if isinstance(string_value, memoryview):
                                return string_value.tobytes()
                            if isinstance(string_value, bytes):
                                return string_value.decode('utf-8')  # Convert bytes to string
                            return string_value
                    except Exception as e:
                        print(f"Decryption with key {key} failed: {e}")
        return value

class EncryptedFloatField(models.BinaryField):
    def __init__(self, *args, **kwargs):
        self.db_utils = DatabaseUtils()
        self.all_keys = DatabaseUtils.get_keys()
        self.encrypt_key = self.all_keys[0] if self.all_keys else settings.PGCRYPTO_DEFAULT_KEY
        self.schema = get_current_schema()
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        if value is not None:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {self.schema}.pgp_sym_encrypt(%s::text, %s::text)", [value, self.encrypt_key])
                result = cursor.fetchone()
                if result:
                    # Ensure the encrypted value is properly returned
                    encrypted_value = result[0]
                    if isinstance(encrypted_value, memoryview):
                        value = encrypted_value.tobytes()  # Convert memoryview to bytes
                        return value
                else:
                    # Handle the case where encryption returns no value
                    print(f"\n============================================\nEncryption failed or returned no value.\n============================================\n")
                    return None
        return value


    def from_db_value(self, value, expression, connection):
        print("\n===============================================\n INSIDE ENCRYPTED FLOAT FIELD\nfrom_db_value()\n===============================================\n")
        if value is not None:
            with connection.cursor() as cursor:
                for key in self.all_keys:
                    try:
                        cursor.execute(f"SELECT {self.schema}.pgp_sym_decrypt(%s::bytea, %s::text)", [value, key.strip()])
                        result = cursor.fetchone()
                        if result:
                            string_value = result[0]
                            if isinstance(string_value, memoryview):
                                return string_value.tobytes()
                            if isinstance(string_value, bytes):
                                return string_value.decode('utf-8')  # Convert bytes to string
                            return string_value
                    except Exception as e:
                        print(f"Decryption with key {key} failed: {e}")
        return value

class EncryptedDecimalField(models.BinaryField):
    def __init__(self, *args, **kwargs):
        self.db_utils = DatabaseUtils()
        self.all_keys = DatabaseUtils.get_keys()
        self.encrypt_key = self.all_keys[0] if self.all_keys else settings.PGCRYPTO_DEFAULT_KEY
        self.schema = get_current_schema()
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        if value is not None:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {self.schema}.pgp_sym_encrypt(%s::text, %s::text)", [value, self.encrypt_key])
                result = cursor.fetchone()
                if result:
                    # Ensure the encrypted value is properly returned
                    encrypted_value = result[0]
                    if isinstance(encrypted_value, memoryview):
                        value = encrypted_value.tobytes()  # Convert memoryview to bytes
                        return value
                else:
                    # Handle the case where encryption returns no value
                    print(f"\n============================================\nEncryption failed or returned no value.\n============================================\n")
                    return None
        return value


    def from_db_value(self, value, expression, connection):
        print("\n===============================================\n INSIDE ENCRYPTED DECIMAL FIELD\nfrom_db_value()\n===============================================\n")
        if value is not None:
            with connection.cursor() as cursor:
                for key in self.all_keys:
                    try:
                        cursor.execute(f"SELECT {self.schema}.pgp_sym_decrypt(%s::bytea, %s::text)", [value, key.strip()])
                        result = cursor.fetchone()
                        if result:
                            string_value = result[0]
                            if isinstance(string_value, memoryview):
                                return string_value.tobytes()
                            if isinstance(string_value, bytes):
                                return string_value.decode('utf-8')  # Convert bytes to string
                            return string_value
                    except Exception as e:
                        print(f"Decryption with key {key} failed: {e}")
        return value

