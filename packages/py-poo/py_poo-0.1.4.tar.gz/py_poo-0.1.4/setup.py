from setuptools import setup, find_packages

setup(
    name='py-poo',
    version='0.1.4',
    packages=find_packages(where='src'),
    package_dir={'': 'src'}, 
    install_requires=[],
    author='Gabriel Carvalho',
    author_email='contatotrabalhogab@gmail.com',
    description='Python poo non native features',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/iamgabs/python-poo',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
