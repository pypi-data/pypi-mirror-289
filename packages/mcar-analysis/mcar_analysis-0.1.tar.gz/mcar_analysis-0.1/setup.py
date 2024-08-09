from setuptools import setup, find_packages

setup(
    name='mcar_analysis',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'scipy',
        'pyampute',
        'seaborn',
        'matplotlib',
        'numpy',
        'pandas'
    ],
    author='Jahanzeb Ahmed',  # Replace with your name
    author_email='jahanzebahmed.mail@gmail.com',  # Replace with your email
    description='A library for MCAR analysis with additional statistical tests',
    url='https://github.com/Jahanzeb-git/mcar_analysis',  # Replace with your GitHub repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
