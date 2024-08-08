from setuptools import setup, find_packages

setup(
    name='companies_shared_clients',
    version='0.1.2',
    author='Bakhodir Ramazonov',
    author_email='boxa.devops@gmail.com',
    description='Shared Clients',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/companiesinfo/companies-shared-clients',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
