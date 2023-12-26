from PIL import Image

def replace_black_with_white(input_image_path, output_image_path, threshold=30):
    # 打开图片
    img = Image.open(input_image_path)

    # 将图片转换为RGB模式，以便处理透明度
    img = img.convert("RGBA")
    data = img.getdata()

    # 创建一个新的像素数据列表
    new_data = []

    for item in data:
        # 如果像素接近黑色，替换为白色
        if item[0] < threshold and item[1] < threshold and item[2] < threshold:
            new_data.append((255, 255, 255, item[3]))
        else:
            new_data.append(item)

    # 创建新的图片对象
    img.putdata(new_data)

    # 保存新图片
    img.save(output_image_path, "PNG")

if __name__ == "__main__":
    input_image = "public/img/brand/rakeai.png"  # 输入图片路径
    output_image = "public/img/brand/rakeai_white.png"  # 输出图片路径
    replace_black_with_white(input_image, output_image)
