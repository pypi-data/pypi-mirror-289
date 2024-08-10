import argparse
import subprocess
import os
import datetime

def parse_args():
    parser = argparse.ArgumentParser(description="Execute all PDF processing scripts.")
    parser.add_argument("--pdf_in", type=str, help="Input directory for PDF files, used by 1-pdf2img.py")
    parser.add_argument("--pdf_out", type=str, help="Output directory for PDF files, used by 3-img2pdf.py")
    return parser.parse_args()

def execute_script(script_path, **kwargs):
    """
    使用subprocess.run执行指定的脚本文件，并根据提供的关键字参数传递相应的命令行参数，
    只有当参数是脚本能够识别的时候才传递。
    """
    # 明确参数对应的脚本
    param_scripts = {
        'pdf_in': ['1-pdf2img.py'],
        'pdf_out': ['3-img2pdf.py'],
    }

    try:
        # 根据不同的脚本路径构建参数列表
        script_args = ['python', script_path]
        script_name = os.path.basename(script_path)

        # 根据不同脚本传递不同参数
        for key, value in kwargs.items():
            # 检查参数是否适用于当前脚本
            if key in param_scripts and any(script_name == param for param in param_scripts[key]):
                if value is not None:
                    script_args.extend(['--' + key, str(value)])

        subprocess.run(script_args, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing script {script_path}: {e}")

def execute_all(pdf_in=None, pdf_out=None):
    # 获取PdfBluePrint.py文件的目录
    pdfblueprint_dir = os.path.dirname(os.path.abspath(__file__))

    # 定义其他脚本的相对路径
    scripts = [
        '0-temp_del.py',
        '1-pdf2img.py',
        '2-black2final.py',
        '3-img2pdf.py',
        '4-dir_del.py',
    ]

    # 构建脚本的完整路径
    full_script_paths = [os.path.join(pdfblueprint_dir, script) for script in scripts]

    # 执行脚本并打印输出
    for script_path in full_script_paths:
        print(f"Exec: {script_path}")
        # 根据不同脚本传递不同参数
        execute_script(script_path, pdf_in=pdf_in, pdf_out=pdf_out)
        print(f"{os.path.basename(script_path).split('.')[0]}-Complete")

    # 等待用户输入以退出
    input("PdfBluePrint Complete, press any key to continue...")

if __name__ == '__main__':
    args = parse_args()
    execute_all(args.pdf_in, args.pdf_out)