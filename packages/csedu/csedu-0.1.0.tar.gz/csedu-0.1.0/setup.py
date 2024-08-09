from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='csedu',
    version='0.1.0',
    author='Henning Mattes',
    author_email='henning_mattes@gmx.de',
    description='A package for computer science education containing modules for image processing and chart creation.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/henningmattes/csedu',
    packages=find_packages(),
    install_requires=[
        'matplotlib',  
        'numpy',       
        'Pillow'       
    ],
    license='MIT with additional terms',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Education',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='education computer science image processing charts computer science education',
    package_data={
        '': ['LICENSE.txt', 'README.md', 'csedu_package_img_small.png']
    },
    include_package_data=True,
    python_requires='>=3.7',
)
