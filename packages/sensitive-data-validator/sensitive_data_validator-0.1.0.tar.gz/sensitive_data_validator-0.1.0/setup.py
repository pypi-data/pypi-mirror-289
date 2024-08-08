from setuptools import setup, find_packages

setup(
    name='sensitive_data_validator',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pandas',
        'validate-docbr',
        'google-cloud-storage',
        'google-cloud-logging'
    ],
    entry_points={
        'console_scripts': [
            'sensitive_data_validator=sensitive_data_validator.main:main',
        ],
    },
    author='Guilherme Duarte',
    author_email='guilherme.henrique@exa.com.br',
    description='A package to validate sensitive data in various file formats.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://yourrepository.url',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
