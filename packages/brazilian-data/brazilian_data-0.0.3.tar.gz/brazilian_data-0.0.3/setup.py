from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='brazilian_data',
    version='0.0.3',
    license='MIT License',
    author='Jeferson Sehnem',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='sehnemjeferson@gmail.com',
    keywords='Brazilian Data',
    description=u'This repository is part of the creation of a package for collecting Brazilian data',
    packages=['brazilian_data'],
    install_requires=['pandas == 2.2.2', 'python-bcb==0.2.0', 'sidrapy==0.1.4','openpyxl==3.1.2','beautifulsoup4==4.12.1','requests==2.31.0',
                      'ipeadatapy==0.1.9','pytrends==4.9.2','python-dotenv==1.0.0','quandl==3.7.0','fredapi==0.5.1','xlrd==2.0.1'],)