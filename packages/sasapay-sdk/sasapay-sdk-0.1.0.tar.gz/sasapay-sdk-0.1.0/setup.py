from setuptools import setup, find_packages

with open("README.md", "r") as ld:
    long_description = ld.read()

setup(
    name='sasapay-sdk',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['requests'],
    url='https://github.com/sasapay/sasapay-python-sdk',
    license='MIT',
    author='Simon Okello',
    author_email='simonokello93@gmail.com',
    description='A Python wrapper for the SasaPay API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
