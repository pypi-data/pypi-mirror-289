from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PdfBluePrint',  # 包名
    version='0.0.1',  # 版本号
    description='Beautify PDF Colors for CMYK printer without K color',  # 描述
    long_description=long_description,  # 长描述，通常是README文件的内容
    long_description_content_type='text/markdown',  # 长描述内容的类型
    url='https://github.com/jomoly/PdfBluePrint',  # 项目主页
    author='John Lu',  # 作者
    author_email='jomoly@gmail.com',  # 作者邮箱
    license='LGPL',  # 许可证
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # 包含的包
    install_requires=[  # 依赖项
#        'PyMuPDF',
	'Fitz',
        'Pillow',
        'numpy',
        'img2pdf',
    ],
    entry_points={
    'console_scripts': [
        'pdfblueprint = PdfBluePrint.PdfBluePrint:execute_all',  # 命令行工具的名称和对应的模块及函数
    ],
    },
    # 其他元数据...
)
