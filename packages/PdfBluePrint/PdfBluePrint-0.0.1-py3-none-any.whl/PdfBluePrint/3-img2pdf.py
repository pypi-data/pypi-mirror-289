import img2pdf
import os
import fitz
import time

doc = fitz.open()  # 创建一个新的PDF文档
imgdir = "output"  # 图片所在的目录

# 获取图片列表和数量
imglist = os.listdir(imgdir)
imgcount = len(imglist)

if imgcount == 0:
    print("没有找到图片。")
else:
    for i, f in enumerate(imglist):
        # 确保文件是图片
        if os.path.splitext(f)[1].lower() in ['.png', '.jpg', '.jpeg', '.bmp', '.tiff']:
            img = fitz.open(os.path.join(imgdir, f))  # 以document形式打开图片
            rect = img[0].rect  # 获取图片尺寸
            pdfbytes = img.convert_to_pdf()  # 将图片转换为PDF流
            img.close()  # 关闭图片文档

            # 以PDF形式打开流
            imgPDF = fitz.open("pdf", pdfbytes)
            # 新建一个页面，尺寸与图片相同
            page = doc.new_page(width=rect.width, height=rect.height)
            # 将图片显示在页面上
            page.show_pdf_page(rect, imgPDF, 0)
            imgPDF.close()  # 关闭图片PDF文档

# 获取当前时间戳并格式化
timeArray = time.localtime()
otherStyleTime = time.strftime("%Y-%m-%d %H-%M-%S", timeArray)

# 仅当文档包含页面时保存PDF
if len(doc) > 0:
    doc.save(otherStyleTime + ".pdf")
    print(f"文档已保存为：{otherStyleTime}.pdf")
else:
    print("没有页面可以保存。")
doc.close()  # 关闭PDF文档