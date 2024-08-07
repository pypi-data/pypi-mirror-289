from setuptools import setup

setup(
    name='thename',
    version='1.0.3',
    author='Xizhen Du',
    author_email='xizhendu@gmail.com',
    url='https://devnull.cn',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    description='Talking to https://devnull.cn/name',
    install_requires=[
        "requests"
    ]
)
