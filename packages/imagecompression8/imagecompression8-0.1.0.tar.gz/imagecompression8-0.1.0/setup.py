from setuptools import setup, find_packages

setup(
    name='imagecompression8',
    version='0.1.0',
    packages=find_packages(),
    description='Image compression using REIS algorithms',
    install_requires=[
        'numpy',
        'pillow'
        'scipy',
    ],
    author='Katie Wen-Ling Kuo',
    author_email='katie20030705@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=3.6',
)