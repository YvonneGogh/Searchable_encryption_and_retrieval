import numpy as np
from cv2 import cv2 as cv
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from aes_hash_encrypt import AESCipher

#设置参数
winSize = (128,128)
blockSize = (64,64)
blockStride = (8,8)
cellSize = (16,16)
nbins = 9
winStride = (8,8)
padding = (8,8)


def hog_extractor(path):
    img = cv.imread(path)
    hog = cv.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins)
    hog_feature = hog.compute(img, winStride, padding).reshape((-1,))
    return hog_feature


cipher = AESCipher(get_random_bytes(16))
path = "E:\Frank\\facial_datasets\Mul.ti-Task Fac.al Lan.dmark (MT.FL) dat.a.set\AFLW\\0035-image03265.jpg"
feature=hog_extractor(path)
print(feature)
encrypted_feature =cipher.encrypt(feature)
print(encrypted_feature)


