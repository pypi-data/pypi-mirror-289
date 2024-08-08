from setuptools import setup, find_packages

setup(
    name='gugurelay',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'python-can',
        'python-can[canalystii]',
        'pywin32',
        'pywin32-ctypes',
        # 其他依赖项...
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A short description of the project',
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)