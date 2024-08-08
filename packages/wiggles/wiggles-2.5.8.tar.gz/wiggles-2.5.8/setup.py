from setuptools import setup, find_packages
import os

setup(
    name='wiggles',
    version='2.5.8',
    license = "MIT License with attribution requirement",
    author="Ranit Bhowmick",
    author_email='bhowmickranitking@duck.com',
    description='''This library makes signal processing easy! A great tool for students to easily visualise and test their sigals virtually. Whether you're working with continuous or discrete signals, Wiggles provides a wide range of functionalities to make signal processing straightforward and intuitive. It supports operations in both the time domain and frequency domain, including Fast Fourier Transform (FFT) and inverse FFT, and allows for easy conversion between different representations.
Wiggles is designed to be easy to use and integrate into your existing Python workflows, making it a valuable tool for engineers, researchers, and anyone interested in signal processing.''',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Kawai-Senpai/Wiggles',
    download_url='https://github.com/Kawai-Senpai/Wiggles',
    keywords=["Signal Processing",'Education','Discrete signal','Continuous signal','Basic signal operations'],
    install_requires=['sympy==1.11.1', 'numpy==1.24.2', 'matplotlib==3.7.1', 'pyaudio==0.2.14']
)