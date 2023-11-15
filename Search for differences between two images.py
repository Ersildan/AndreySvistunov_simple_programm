from PIL import Image, ImageChops

image_1 = Image.open(r'C:\ ...') # the path to the image
image_2 = Image.open(r'C:\ ...') № the path to the image


result = ImageChops.difference(image_1, image_2)
result.show()

# result.getbbox() в данном случае вернет (0, 0, 888, 666)
result.save('result.jpg')

# Создаст картинку, в которой будет заметно различия между двумя изображениями
