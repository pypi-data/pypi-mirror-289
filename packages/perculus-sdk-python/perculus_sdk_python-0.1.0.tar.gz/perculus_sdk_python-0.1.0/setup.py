from setuptools import setup, find_packages

setup(
    name='perculus-sdk-python',
    version='0.1.0',
    author='Perculus Dev Team',
    author_email='zafer@perculus.com',
    description='Perculus Python Software Development Kit',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    url='https://github.com/perculus/perculus-sdk-python',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'python-dotenv==1.0.1',
        'requests==2.32.3',
        'urllib3==2.2.2'
    ],
)