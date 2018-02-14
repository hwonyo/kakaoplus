# !/usr/bin/python
from setuptools import setup, find_packages
import kakaoplus

setup_requires = []

install_requires = [
]

dependency_links = [
]

setup(
    name='kakaoplus',
    version=kakaoplus.__version__,
    url='https://github.com/HwangWonYo/kakaoplus',
    license='MIT License',
    description='A Python Library For Kakao Plus Friend Auto Reply API',
    author='wonyoHwang',
    author_email='hollal0726@gmail.com',
    packages=find_packages(exclude=['tests']),
    # include_package_data=True,
    # install_requires=install_requires,
    # setup_requires=setup_requires,
    # dependency_links=dependency_links,
    keywords=['kakao', 'plus friend', 'chatbot'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ]
)
