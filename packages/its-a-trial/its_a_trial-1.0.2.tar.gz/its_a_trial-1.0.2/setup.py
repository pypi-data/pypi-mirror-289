from setuptools import setup, find_packages

setup(
    name='its_a_trial',
    version='1.0.2',
    packages=find_packages(),
    install_requires=[
        'tensorflow',
        'numpy',
        'Pillow',
    ],
    author='MM21B038',
    author_email='mm21b038@smail.iitm.ac.in',
    description='A package for your DL model',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MM21B038/my_first_trial_model',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
