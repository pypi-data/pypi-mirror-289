from setuptools import setup, find_packages

setup(
    name='perculus_sdk_python',
    version='0.1.6',
    author='Perculus Dev Team',
    author_email='zafer@perculus.com',
    description='Perculus Python Software Development Kit',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    packages=['perculus_sdk_python'],
    package_dir={'perculus_sdk_python':'perculus_sdk_python'},
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