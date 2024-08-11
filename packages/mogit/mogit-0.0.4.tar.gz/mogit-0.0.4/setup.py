from setuptools import setup, find_packages

setup(
    name="mogit",  # 包的名称
    version="0.0.4",  # 版本号
    packages=find_packages(exclude=["tests", "tests.*"]),  # 包含的包
    author="MoYan",  # 作者
    author_email="moyan@moyanjdc.top",  # 作者邮箱
    description="一个轻量级的分布式版本控制系统",  # 包的简要描述
    long_description=open("Readme.md").read(),  # 包的详细描述
    long_description_content_type="text/markdown",  # 描述的内容类型
    classifiers=[  # 包的分类信息
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Environment :: Console",
        "Programming Language :: Python :: 3.10",
    ],
    install_requires=open("requirements.txt").read().split("\n"),
    entry_points={
        "console_scripts": ["mogit=mogit.cli:cli"],
    },
)
