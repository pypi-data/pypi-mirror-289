from setuptools import setup, find_packages

setup(
    name='samotpravil_smtp',
    version='0.0.1a',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    url='https://github.com/yourusername/samotpravil_smtp',
    license='MIT',
    author='Samotpravil',
    author_email='support@samotpravil.ru',
    description='Python client for Samotpravil SMTP API'
)
