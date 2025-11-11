from setuptools import setup, find_packages

setup(
    name="conintf_ptk",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "prompt_toolkit>=3.0"
    ],
    python_requires=">=3.8",
    author="Warat Thongsuwan",
    author_email="jimnd55512@gmail.com",
    description="Reusable async console interface with customizable banner and commands",
    url="https://github.com/TonpalmUnmain/conintf_ptk",
    license="GPLv3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
