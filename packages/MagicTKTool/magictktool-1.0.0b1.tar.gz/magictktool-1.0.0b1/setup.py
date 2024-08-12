import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MagicTKTool",
    version="1.0.0.beta1",
    author="CodeCrafter-TL",
    author_email="1825456084@qq.com",
    description="A UI package by tkinter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codecrafter-tl/magictk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)