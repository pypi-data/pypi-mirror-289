from setuptools import setup, find_packages

setup(
    name='postman_sync',
    version='0.1.2',
    description='A tool to synchronize Postman collections with Swagger (OpenAPI) specifications',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Oluwaseyi Ajadi',  # Replace with your name
    author_email='oluwaseyinexus137@gmail.com',  # Replace with your email
    url='https://github.com/BlazinArtemis/postman-swagger-automatic-sync',  # URL of your project
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'argparse'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'postman_sync=postman_sync.main_script:main',  # Entry point for your CLI
        ],
    },
)
