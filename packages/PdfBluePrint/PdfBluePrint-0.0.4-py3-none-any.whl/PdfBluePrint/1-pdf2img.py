import fitz
import os
import argparse

# 创建目录的函数
def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)

# 将PDF转换为图像的函数
def pdf_image(pdfPath, imgPath, zoom_x, zoom_y, rotation_angle):
    pdf = fitz.open(pdfPath)
    name = os.path.splitext(os.path.basename(pdfPath))[0]
    for pg in range(0, pdf.page_count):
        page = pdf[pg]
        trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotation_angle)
        pm = page.get_pixmap(matrix=trans, alpha=False)
        pm._writeIMG(os.path.join(imgPath, name + str(pg + 1) + ".jpg"), "jpg", 1)
    pdf.close()

# 解析命令行参数
def parse_args():
    parser = argparse.ArgumentParser(description="Convert PDF to images with specified zoom and rotation.")
    parser.add_argument("--pdf_in", type=str, default=os.getcwd(), help="Directory containing the PDF files. Defaults to the current working directory if not specified.")
    parser.add_argument("--img_in", type=str, default="img_in", help="Directory to save the output images. Defaults to 'img_in' in the current working directory if not specified.")
    parser.add_argument("--zoom_x", type=float, default=5, help="Zoom factor in the x direction (default: 5)")
    parser.add_argument("--zoom_y", type=float, default=5, help="Zoom factor in the y direction (default: 5)")
    parser.add_argument("--rotation_angle", type=float, default=0, help="Rotation angle in degrees (default: 0)")
    return parser.parse_args()

# 主函数
def main():
    args = parse_args()
    pdf_dir = args.pdf_in  # 使用--pdf_in参数或默认工作目录
    img_dir = args.img_in  # 使用--img_in参数或默认的img_in文件夹
    zoom_x = args.zoom_x
    zoom_y = args.zoom_y
    rotation_angle = args.rotation_angle

    # 确保输出目录存在
    mkdir(img_dir)

    # 记录是否处理了PDF文件
    processed_pdfs = False
    # 记录是否生成了图片
    images_generated = False

    # 遍历PDF目录中的所有文件
    for file_path in os.listdir(pdf_dir):
        if file_path.endswith(".pdf"):
            pdf_path = os.path.join(pdf_dir, file_path)
            print(f"Processing {pdf_path}...")
            pdf_image(pdf_path, img_dir, zoom_x, zoom_y, rotation_angle)
            processed_pdfs = True
            # 假设每个PDF至少生成一张图片
            images_generated = True

    # 如果没有找到PDF文件，输出提醒信息
    if not processed_pdfs:
        print("1 - THERE IS NO pdf FILES input, please check!")

    # 检查输出目录中的图片数量
    if not images_generated or len(os.listdir(img_dir)) == 0:
        print("1 - THERE IS NO images FOUND output, please check!")

if __name__ == "__main__":
    main()