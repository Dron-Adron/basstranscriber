from captcha.image import ImageCaptcha  # pip install captcha
import numpy as np
from PIL import Image
import random
import os


def generate_captcha():
    number = ['0','1','2','3','4','5','6','7','8','9']
    image = ImageCaptcha(width=250, height=40, font_sizes=[30])

    captcha_text = []
    for i in range(6):
        c = random.choice(number)
        captcha_text.append(c)

    captcha_text = ''.join(captcha_text)

    captcha = image.generate(captcha_text)
    captcha_image = Image.open(captcha)
    captcha_image = np.array(captcha_image)
    return captcha_image,captcha_text
    