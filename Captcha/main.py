from captcha.image import ImageCaptcha

pattern = 'Капчонка qwerty228'
captcha = ImageCaptcha(width=400, height=250)
captcha.write(pattern, 'Captcha/captcha.png')

print(str(captcha) + '\nCapcha created!')
