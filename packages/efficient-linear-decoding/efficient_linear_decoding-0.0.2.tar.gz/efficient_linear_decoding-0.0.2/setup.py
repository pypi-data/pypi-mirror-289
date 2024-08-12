from setuptools import find_packages,setup


setup(
    name="efficient_linear_decoding",
    version = "0.0.2",
    keywords = ["pip", "efficient_linear_decoding"],
    description = "Efficient computation library for linear attention.",
    license = "MIT Licence",
    url = "https://github.com/Computational-Machine-Intelligence/efficient_linear_decoding",
    
    author = "Jiaping Wang",
    author_email = "wjp666.s@gmail.com",
    packages=find_packages(
        exclude=[
            "tests"
        ]
    ),
    platforms = "any",
    install_requires=["torch==2.1.0", "pycuda", "triton==2.1.0","pynvml","numpy"], 
    include_package_data=True,
)