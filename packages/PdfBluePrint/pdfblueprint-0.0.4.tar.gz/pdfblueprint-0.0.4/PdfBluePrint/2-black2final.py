import argparse
import os
from PIL import Image
from pathlib import Path

def process_image(input_path, output_path, img_name):
    img = Image.open(input_path)
    if img.mode != 'RGB':
        img = img.convert("RGB")

    width, height = img.size
    for i in range(width):
        for j in range(height):
            data = img.getpixel((i, j))
            if data[0] <= 127 or data[1] <= 127 or data[2] <= 127:
                img.putpixel((i, j), (0, 0, 65, 255))

    img.save(output_path + '/' + img_name)

def main():
    parser = argparse.ArgumentParser(description="Process images to make black and blue.")
    parser.add_argument("--img_in", type=str, default='./img_in',
                        help="Input directory for images. Defaults to './img_in' if not specified.")
    parser.add_argument("--img_out", type=str, default='./img_out',
                        help="Output directory for processed images. Defaults to './img_out' if not specified.")
    args = parser.parse_args()

    # Ensure output directory exists
    if not os.path.exists(args.img_out):
        os.makedirs(args.img_out)

    # 初始化标志变量，用于跟踪是否处理了图片
    processed_images = False
    output_images = []

    # Process each image in the input directory
    pathlist = Path(args.img_in).glob("**/*.jpg")
    for image_path in pathlist:
        img_name = os.path.basename(image_path)
        process_image(image_path, args.img_out, img_name)
        processed_images = True  # 标记至少处理了一张图片
        output_images.append(img_name)  # 记录输出的图片名称

    # 如果没有找到图片，输出提醒信息
    if not processed_images:
        print("THERE IS NO images FOUND input, please check!")

    # 检查输出目录中的图片
    if not output_images:
        print("2 - THERE IS NO images FOUND output, please check!")
    else:
        print(f"2 - All images have been processed and saved to {args.img_out}")

if __name__ == "__main__":
    main()