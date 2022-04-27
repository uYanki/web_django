# pip install pillow

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


# 验证码生成
def getCheckCode(length=5, width=120, height=32, fontsize=28, fontfile="ARIAL.TTF"):

    def getRandowChar():
        return chr(random.randint(65, 90))

    def getRandomColor():
        return random.randint(0, 255), random.randint(10, 255), random.randint(64, 255)

    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image, mode='RGB')
    # 绘制 验证码字符
    checkcode = []
    font = ImageFont.truetype(fontfile, fontsize)
    for i in range(length):
        char = getRandowChar()
        checkcode.append(char)
        offset = random.randint(-4, 4)
        draw.text((i / length * width, offset), char,
                  font=font, fill=getRandomColor())
    # 绘制 干扰点
    for i in range(40):
        draw.point((random.randint(0, width), random.randint(
            0, height)), fill=getRandomColor())
    # 绘制 干扰圆圈
    for i in range(40):
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), random.randint(0, 90),
                 random.randint(50, 210), fill=getRandomColor())
    # 绘制 干扰线
    for i in range(5):
        draw.line(
            (random.randint(0, width), random.randint(0, height),
             random.randint(0, width), random.randint(0, height)),
            fill=getRandomColor())
    # 滤波 边界加强
    image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return image, ''.join(checkcode)


'''测试'''
if __name__ == '__main__':
    img, code = getCheckCode()
    # print(code)
    # 1.直接打开
    img.show()
    # 2.写入文件
    # with open('code.png', 'wb') as f:
    #     img.save(f, format='png')
    # 3.写入内存
    # from io import BytesIO
    # stream = BytesIO()
    # img.save(stream,'png')
    # print(stream.getvalue())
