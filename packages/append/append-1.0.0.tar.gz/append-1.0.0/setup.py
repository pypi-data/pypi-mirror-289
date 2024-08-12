from setuptools import setup, find_packages

setup(
    name='append',
    version='1.0.0',
    description='A simple tool to add a prefix or suffix to every line in a text file.',
    author='Ankit',
    author_email='ashuankitpandey@gmail.com',
    url='https://github.com/4nk1t/appender',  # Replace with your actual GitHub repository
    py_modules=['appender'],
    entry_points={
        'console_scripts': [
            'appender=appender:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
