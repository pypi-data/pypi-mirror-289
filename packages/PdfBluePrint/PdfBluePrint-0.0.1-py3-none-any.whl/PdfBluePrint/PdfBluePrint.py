import subprocess
import os
import datetime
import sys

def execute_all():
    # 获取PdfBluePrint.py文件的目录
    pdfblueprint_dir = os.path.dirname(os.path.abspath(__file__))

    # 定义其他脚本的相对路径
    scripts = [
        os.path.join(pdfblueprint_dir, '1-pdf2img.py'),
        os.path.join(pdfblueprint_dir, '2-black2final.py'),
        os.path.join(pdfblueprint_dir, '3-img2pdf.py'),
        os.path.join(pdfblueprint_dir, '4-dir_clr.py')
    ]

    # 执行脚本并打印输出
    for script in scripts:
        print(f"执行脚本: {script}")
        # 使用exec(open(script).read())或subprocess.run(['python', script], check=True)
        with open(script) as f:
            exec(f.read())
        print(f"{os.path.basename(script).split('.')[0]}-完成")

    # 更改字符编码（如果需要的话）
    # os.system('chcp 65001')  # 注意：Python脚本通常不需要更改字符集

    # 打印完成信息和生成的PDF文件名
    current_time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    pdf_filename = f"output-{current_time}.pdf"
    print(f"成功生成-请查看本目录下{pdf_filename}-任意键退出")

    # 等待用户输入以退出
    input("按任意键退出...")

if __name__ == '__main__':
    execute_all()