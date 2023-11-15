import qrcode

data = 'https://vk.com/ofeonttse' #push your link to create QRcode

img = qrcode.make(data)
img.save("qrcode.png")
