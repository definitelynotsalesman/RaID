import base64
import gzip

def decrypt_base_64(byte_string):
    decrypted_string = base64.b64decode(byte_string)
    return decrypted_string

def decompress_Gzip(byte_string):
    decompressed_string = gzip.decompress(byte_string)
    return decompressed_string
