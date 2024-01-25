import qrcode

data = 'https://vk.com/ofeonttse' #push your link to create QRcode

img = qrcode.make(data)

№save new png on your download
img.save("qrcode.png")

print('Hello guys')
print('nice program')
