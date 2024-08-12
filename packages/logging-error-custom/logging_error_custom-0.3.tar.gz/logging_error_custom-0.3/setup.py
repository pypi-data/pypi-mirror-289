from setuptools import setup, find_packages

setup(
    name='logging_error_custom',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'mysql-connector-python',
        'python-dotenv'
    ],
    description='A library for logging exceptions to a MySQL database.',
    author='Your Name',
    author_email='your.email@example.com',
)
