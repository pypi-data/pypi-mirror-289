from setuptools import setup, find_packages

setup(
    name='get_uuid4',
    version='0.0.1',
    description='Get a random uuid4 per-time',
    packages=find_packages(),
    author_email='Ahmedelmawrdy2@gmail.com',
    author='Ahmed Mohamed',
    entry_points={
        'console_scripts': [
            'get_uuid4 = get_uuid4:main'
        ]
    }
)