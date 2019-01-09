# 识别测试
import tesserocr
from PIL import Image

image = Image.open('code.jpg')
result = tesserocr.image_to_text(image)
print(result)

# 验证码处理
import tesserocr
from PIL import Image

image = Image.open('code.jpg')
# image = image.convert('L') # 转为灰度图像
# image.show()
# image = image.convert('1') # 二值化处理
# image.show()
# 指定二值化的阀值
image = image.convert('L')
threshold = 160
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table,'1')
image.show()

# 精确识别
import tesserocr
from PIL import Image

image = Image.open('CheckCode.jpeg')
image = image.convert('L')
threshold = 160
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table,'1')
result = tesserocr.image_to_text(image)
print(result)
