from setuptools import setup, find_packages

setup(
    name='imagecompression7',
    version='0.1.12',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'pillow'
    ],
    description='Image compression using REIS algorithms',
    author='Katie Wen-Ling Kuo',
    author_email='katie20030705@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=3.6',
)