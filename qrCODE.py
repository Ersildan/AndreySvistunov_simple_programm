import qrcode

data = 'https://vk.com/ofeonttse'

img = qrcode.make(data)
img.save("qrcode.png")
