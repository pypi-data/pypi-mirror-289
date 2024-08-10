from setuptools import setup, find_packages

setup(
    name="dilog",  # 包的名称
    version="0.1.6",  # 版本号
    author="didiwangluo",  # 作者名称
    author_email="didiwangluo@outlook.com",  # 作者邮箱
    description="私有的log以及log的oss上传包",  # 简短描述
    long_description=open('README.md', encoding='utf-8').read(),  # 详细描述，指定编码为UTF-8
    long_description_content_type="text/markdown",
    url="https://gitee.com/didi_nj/dilog",  # 项目主页（私有仓库的 URL）
    packages=find_packages(),  # 自动发现包
    include_package_data=True,  # 包括package_data中的所有文件
    package_data={
        'dilog': ['logging_config.yaml'],  # 确保包含配置文件
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Python 版本要求
    install_requires=[  # 依赖项
        "PyYAML>=5.3.1",
        "oss2>=2.13.0",
    ],
)
