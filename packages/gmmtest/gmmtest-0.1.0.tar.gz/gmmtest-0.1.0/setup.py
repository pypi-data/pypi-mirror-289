from setuptools import setup, find_packages

# 读取README文件作为长描述
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gmmtest",  # 你的包名
    version="0.1.0",  # 版本号
    author="gmm",  # 作者名
    author_email="your.email@example.com",  # 作者邮箱
    description="测试上传pypi.",  # 包的简短描述
    long_description=long_description,  # 长描述，从README.md中读取
    long_description_content_type="text/markdown",  # 指定长描述的格式为Markdown
    url="https://github.com/your_username/gmmtest",  # 包的URL，通常是GitHub仓库地址
    packages=find_packages(),  # 自动发现包
    # 如果你的包有依赖项，请在这里列出它们  
    # install_requires=[
    #     'dependency1>=version',
    #     'dependency2>=version',
    # ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # 如果你的包包含可执行脚本，可以在这里指定
    # entry_points={
    #     'console_scripts': [
    #         'your_script_name = your_package.module:main_func',
    #     ],
    # },
)