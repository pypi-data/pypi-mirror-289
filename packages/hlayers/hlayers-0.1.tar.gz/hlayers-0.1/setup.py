from setuptools import setup, find_packages

setup(
    name='hlayers',  
    version='0.1', 
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'InquirerPy',
        'ruamel.yaml',
        'datadog_api_client',
        'cachetools',
    ],
    entry_points={
        'console_scripts': [
            'hlayers=hlayers:cli',  # Replace with your command and module name
        ],
    },
)