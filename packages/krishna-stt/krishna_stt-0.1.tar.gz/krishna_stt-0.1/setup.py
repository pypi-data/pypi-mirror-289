# pip install setuptools

from setuptools import setup,find_packages

setup(
    name = 'krishna_stt',
    version = '0.1',
    author = 'Krishna Lodhi',
    author_email = 'krish9lodhi2004@gmail.com',
    description = 'This is a speech to text package created by Krishna Lodhi'    
)
packages = find_packages(),
install_requiremets = [
    'selenium'
    'webdriver-manager'
    'setuptools'
]