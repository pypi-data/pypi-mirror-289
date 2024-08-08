from setuptools import setup, find_packages

setup(
    name="tar_display",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "tkinter",
    ],
    entry_points={
        "console_scripts": [
            "tar_paint=tar_paint.display:display",
        ],
    },
    author="Your Name",
    author_email="jaroenpronprasit@gmail.com",
    description="tar display application",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/natthphong/display.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)