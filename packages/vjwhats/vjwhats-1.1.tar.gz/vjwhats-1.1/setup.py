from setuptools import setup, find_packages

setup(
    name='vjwhats',
    version='1.1',
    author='Fioruci',
    author_email='fiorucit@gmail.com',
    description='A Python library to interact with WhatsApp Web using Selenium.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Fioruci/vjwhats',
    packages=find_packages(),
    install_requires=[
        'selenium>=4.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)