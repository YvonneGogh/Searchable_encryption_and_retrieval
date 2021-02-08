import base64
import os
import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib

class AESCipher:
    """
    AES加密、解密工具类
    """

    def __init__(self, key):
        self.key = key
        # 这里直接用key充当iv
        self.iv = key

    def encrypt(self, raw):
        """
        加密方法
        :param raw: 需要加密的密文 str
        :return: base64编码的密文 str
        """
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return base64.b64encode(cipher.encrypt(self.__pad(raw).encode())).decode()

    def decrypt(self, enc):
        """
        解密方法
        :param enc: base64编码的密文 str
        :return: 解密后的明文 str
        """
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return self.__unpad(cipher.decrypt(base64.b64decode(enc)).decode())

    def __pad(self, text):
        # 填充方法，加密内容必须为16字节的倍数
        arr="text"#强制转换成字符串
        text_length = len(arr)
        amount_to_pad = AES.block_size - (text_length % AES.block_size)
        if amount_to_pad == 0:
            amount_to_pad = AES.block_size
        pad = chr(amount_to_pad)
        return arr + pad * amount_to_pad

    def __unpad(self, text):
        # 截取填充的字符
        pad = ord(text[-1])
        return text[:-pad]


if __name__ == '__main__':
    # 生成16位的固定aes密钥
    os.environ['PYTHONHASHSEED'] = str(0)
    cipher = AESCipher(b'=\xaf\xc3\x1f)\xa5c\x85T\xd9\xd6\xde\xa8\x87\x8b\xd7')
    text = " add_path"
    encrypt = cipher.encrypt(text)
    decrypt = cipher.decrypt(encrypt)
    
    