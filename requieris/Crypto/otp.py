import hmac
import hashlib
import math
import struct
import base64
import time
import datetime

class   OTP:
    @classmethod
    def generate_hotp(cls, secret, counter, digits=6):
        hmac_result = hmac.new(base64.b32decode(secret, True), struct.pack('>Q', counter), hashlib.sha1).digest()
        offset = hmac_result[19] & 0xf
        bin_code = ((hmac_result[offset] & 0x7f) << 24
                    | (hmac_result[offset + 1] & 0xff) << 16
                    | (hmac_result[offset + 2] & 0xff) << 8
                    | (hmac_result[offset + 3] & 0xff))
        return str(bin_code % 10**digits).zfill(digits)
    
    @classmethod
    def generate_totp(cls, secret, digits=6):
        now = time.mktime(datetime.datetime.now().timetuple())
        return cls.generate_hotp(secret, int(math.floor(now/30)), digits)
    
    
        