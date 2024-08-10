import argparse
import img2pdf
import os
import fitz
import time

def convert_images_to_pdf(img_out='img_out', pdf_out=None):
    # 检查图片目录是否存在
    if not os.path.exists(img_out):
        print(f"3 - The specified image directory does not exist: {img_out}")
        return  # 如果目录不存在，返回

    # 检查图片目录是否存在图片
    imglist = [f for f in os.listdir(img_out) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]
    if not imglist:
        print("3 - THERE IS NO IMAGE FOUND IN THE INPUT DIRECTORY, please check!")
        return  # 如果没有找到图片，返回

    # 创建一个新的PDF文档
    doc = fitz.open()

    # 转换图片到PDF
    for f in imglist:
        img_path = os.path.join(img_out, f)
        img = fitz.open(img_path)
        pdf_bytes = img.convert_to_pdf()
        img.close()

        img_pdf = fitz.open("pdf", pdf_bytes)
        page = doc.new_page(width=img_pdf[0].rect.width, height=img_pdf[0].rect.height)
        page.show_pdf_page(img_pdf[0].rect, img_pdf, 0)
        img_pdf.close()

    # 如果文档中没有页面，不保存PDF并返回
    if doc.page_count == 0:
        print("3 - No pages to save in the PDF document.")
        doc.close()
        return

    # 生成时间戳
    timeArray = time.localtime()
    otherStyleTime = time.strftime("%Y-%m-%d %H-%M-%S", timeArray)

    # 设置PDF输出目录
    if pdf_out is None:
        pdf_out = os.getcwd()

    # 确保输出目录存在
    os.makedirs(pdf_out, exist_ok=True)

    # 保存PDF文件
    output_path = os.path.join(pdf_out, f"output-{otherStyleTime}.pdf")
    doc.save(output_path)
    print(f"3 - PDF document has been saved as: {output_path}")

    # 检查PDF文件是否成功创建
    if not os.path.exists(output_path):
        print("3 - THERE IS NO PDF FILE OUTPUT, please check!")
    doc.close()

def main():
    parser = argparse.ArgumentParser(description="Convert images to a single PDF document.")
    parser.add_argument("--img_out", type=str, default='img_out', help="Directory containing the images to convert. Defaults to 'img_out' if not specified.")
    parser.add_argument("--pdf_out", type=str, default=None, help="Directory to save the output PDF. Defaults to the current working directory if not specified.")
    args = parser.parse_args()

    # 转换图片到PDF
    convert_images_to_pdf(args.img_out, args.pdf_out)

if __name__ == "__main__":
    main()