import setuptools


setuptools.setup(
    name="fast-knifes",
    version="0.0.6",
    author="knifes",
    author_email="author@example.com",
    description="Fast Swiss Army Knife",
    long_description="`pip install fast-knifes --index-url https://pypi.python.org/simple -U`",
    long_description_content_type="text/markdown",
    url="https://github.com/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.0",
    install_requires=[
        # "python-decouple",
        # "prompt_toolkit",
        # "attrs",
        # "cattrs",
        # "httpx[http2]",
        # 'cryptography',                       #  required by aes
    ],
)
